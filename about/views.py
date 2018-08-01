import os
from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from django.conf import settings
# Create your views here.


def index(request):
    request.session['flag'] = False
    return render(request, 'about/about.html')


def about(request):
    request.session['flag'] = False
    return render(request, 'about/about.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['UIN']
        password = request.POST['password']
        try:
            user = Student.objects.get(UIN=username, password=password)
            request.session['flag'] = True
            request.session['UIN'] = user.UIN
            request.session['link'] = user.Link
            return HttpResponseRedirect("upload.html")
        except Student.DoesNotExist:
            msg = "Either the username or the password is incorrect. To retry,"
            title = "Error!"
            lnk = "about:login"
            context = {
                'msg': msg,
                'lnk': lnk,
                'title': title,
            }
            return render(request, 'about/fgerr.html', context=context)

    else:
        return render(request, 'about/login.html')
# '/home/abhinav/EAD Project/Version/Vr1.1/media'


def change(request):
    if request.session.get('flag'):
        if request.method == 'POST':
            old = request.POST['oldpass']
            new = request.POST['password']
            user = Student.objects.get(UIN=request.session.get('UIN'))
            if old == user.password:
                user.password = new
                user.save()
                msg = "The password was changed successfully! To see QR code, "
                title = "Success!"
                lnk = "about:qrcode"
                context = {
                    'msg': msg,
                    'lnk': lnk,
                    'title': title,
                }
                return render(request, 'about/fgerr.html', context=context)
            else:
                msg = "The old password did not match! To retry,"
                title = "Error!"
                lnk = "about:change"
                context = {
                    'msg': msg,
                    'lnk': lnk,
                    'title': title,
                }
                return render(request, 'about/fgerr.html', context=context)

        else:
            return render(request, 'about/cng_pwd.html')

    else:
        return HttpResponseRedirect("login.html")


def forgot(request):
    if request.method == 'POST':
        ans = request.POST['answer']
        uin = request.POST['UIN']
        lnk = "about:forgot"
        try:
            user = Student.objects.get(UIN=uin)
            pwd = request.POST['password']
            if ans == user.sec_ans:
                user.password = pwd
                user.save()
                msg = "The password was changed successfully! To log in,"
                title = "Success!"
                lnk = "about:login"
                context = {
                    'msg': msg,
                    'lnk': lnk,
                    'title': title,
                }
                return render(request, 'about/fgerr.html', context=context)
            else:
                msg = "The answer did not match! To retry,"
                title = "Error!"
                context = {
                    'msg': msg,
                    'lnk': lnk,
                    'title': title,
                }
                return render(request, 'about/fgerr.html', context=context)
        except Student.DoesNotExist:
            msg = "The UIN does not exist. To retry,"
            title = "Error!"
            context = {
                'msg': msg,
                'lnk': lnk,
                'title': title,
            }
            return render(request, 'about/fgerr.html', context=context)

    else:
        return render(request, 'about/forgot.html')
    #
    # else:
    #     return render(request, 'about/forgot.html')


def fgerr(request):
    return render(request, 'about/fgerr.html')


def display(request, uin):
    request.session['flag'] = False
    list_url = []
    name = []
    path = "/home/abhinav/EAD Project/Version/Vr1.1/media/student/" + str(uin)
    for file in os.listdir(path):
        list_url.append('/media/student/' + str(uin) + '/' + file)
        name.append(str(file))
    list_fin = zip(list_url, name)
    context = {
        'list': list_fin,
    }
    #print("Sending context")
    return render(request, 'about/display.html', context=context)


def upload(request):
    if request.session.get('flag'):
        # user = Student.objects.get(UIN=request.session.get('UIN'))
        # context = {'user': user}
        # return render(request, 'about/upload.html', context=context)
        if request.method == 'POST':
            user = Student.objects.get(UIN=request.session.get('UIN'))
            exten = '.jpg'
            request.session['sum'] = 0
            # try:
            #     os.makedirs(os.path.join(settings.MEDIA_ROOT + '/' + str(user.UIN)))
            # except OSError as e:
            #     if e.errno == 17:
            #         request.session['sum'] += 1
            #         exten = str(request.session.get('sum')) + exten
            for count, x in enumerate(request.FILES.getlist("files")):
                user.images = x
                print(str(user.images.url))
                user.save()
            # for count, x in enumerate(request.FILES.getlist("files")):
            #     def handle_uploaded_file(f):
            #         with open(settings.MEDIA_ROOT + '/' + str(user.UIN) + '/file_' + str(count) + str(exten), 'wb+') as destination:
            #             for chunk in f.chunks():
            #                 destination.write(chunk)
            #     handle_uploaded_file(x)
            user.Link = 'http://127.0.0.1:8000/media/student/' + str(user.UIN) + '/'
            request.session['link'] = user.Link
            user.save()
            return HttpResponseRedirect("qrcode.html")
        else:
            return render(request, 'about/upload.html')
    else:
        return HttpResponseRedirect("login.html")
            #render(request, 'about/login.html')


def qrcode(request):
    if request.session.get('flag'):
        qr_link = request.session.get('link')
        # print(qr_link)
        # print("After qr link")
        return render(request, 'about/qrcode.html', {'qr_link': qr_link})
    else:
        return HttpResponseRedirect("login.html")
            #render(request, 'about/login.html')


def logout(request):
    request.session['flag'] = False
    return render(request, 'about/about.html')