from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.


def user_login(req):
    if req.method == 'POST':
        username = req.POST['uname']
        password = req.POST['passw']
        user_exists = Userlogin.objects.filter(username=username).exists()
        if user_exists:
            user_obj = Userlogin.objects.get(username=username)
            if user_obj.password == password:
                req.session['userId'] = user_obj.id
                req.session['username'] = user_obj.username
                if user_obj.role == 'designer':
                    return render(req, 'designer.html')
                return render(req, 'customer.html')
            return HttpResponse('incorrect password')
        return HttpResponse('no user found')


def user_detail(req):
    if req.method == 'POST':
        fname = req.POST['fname']
        lname = req.POST['lstname']
        username = req.POST['uname']
        password = req.POST['passw']
        role = req.POST['select']
        dob = req.POST['date']
        gender = req.POST['gender']
        mobile = req.POST['mbl']
        user_exists = Userlogin.objects.filter(username=username).exists()
        if not user_exists:
            user_obj = Userlogin(username=username,password=password,role=role)
            user_obj.save()
            if user_obj.id>0:
                userdet_obj = Userdetails(firstname=fname,lastname=lname,dob=dob,gender=gender,mobile=mobile,fk_login=user_obj)
                userdet_obj.save()
            if role =='designer':
                boutique = req.POST['dsgn']
                qualification = req.POST['qualif']
                about = req.POST['about']
                userdes_obj = Designerdetails(boutiquename=boutique,qualification=qualification,about=about,fk_login=user_obj)
                userdes_obj.save()
                return HttpResponse('designer saved')
            return HttpResponse('customer saved')
        return HttpResponse('user already exist')
    return render(req, 'home.html')


def profile(req):
    user_id = req.session['userId']
    user_details = Userdetails.objects.get(fk_login__id=user_id)
    designer_details = Designerdetails.objects.get(fk_login__id=user_id)
    return render(req, 'profile.html', {'details': user_details, 'designerDetail': designer_details})

def fabric(req):
    if req.method == 'POST':
        fab_name = req.POST['fbrname']
        fab_des = req.POST['fbrdes']
        fab_cost = req.POST['fbrcost']
        image = req.FILES['img']
        designer_detail_obj = Designerdetails.objects.get(fk_login__id=req.session['userId'])
        desginer_fabric_obj = DesginerFabrics(fabric_name=fab_name, fabric_desc=fab_des, fabric_cost=fab_cost, fabric_image=image, fk_login=designer_detail_obj)
        desginer_fabric_obj.save()
        if desginer_fabric_obj.id > 0:
            return render(req, 'fabric.html', {'status': True, 'fab_name': fab_name})
    return render(req, 'fabric.html')

def work(req):
    return render(req, 'work.html')    

def fn_viewdesigner(req):
    designers = Userlogin.objects.filter(role='designer')
    return render(req, 'viewdesign.html', {'designers': designers})

def fn_designer_details(req):
    designer_id = req.GET['id']
    user_detail = Userdetails.objects.get(fk_login__id=designer_id)
    designr_detail = Designerdetails.objects.get(fk_login__id=designer_id)
    return render(req, 'designerdetails.html', {'userdetail':user_detail, 'designerdetail':designr_detail})


def fn_logout(req):
    del req.session['userId']
    del req.session['username']
    return redirect('/fadapp/')


def fn_edit_profile(req):
    user_detail_obj = Userdetails.objects.get(fk_login__id=req.session['userId'])
    user_detail_obj.firstname = req.POST['fname']
    user_detail_obj.lastname = req.POST['lname']
    user_detail_obj.mobile = req.POST['phone']
    user_detail_obj.save()

    designer_detail_obj = Designerdetails.objects.get(fk_login__id=req.session['userId'])
    designer_detail_obj.boutiquename = req.POST['boutiqueName']
    designer_detail_obj.qualification = req.POST['qualification']
    designer_detail_obj.about = req.POST['about']
    designer_detail_obj.save()

    return HttpResponse('1')

def fn_viewfabrics(req):
    fabrics = DesginerFabrics.objects.all()
    return render(req, 'viewfabrics.html', {'fabs': fabrics})   