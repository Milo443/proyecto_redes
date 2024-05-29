from django.shortcuts import render
from django.http import HttpResponse
from ftplib import FTP
from django.shortcuts import redirect
# Create your views here.

ip_ftp ='192.168.1.104'

def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.quit()

        request.session['user'] = user
        request.session['password'] = password
        return redirect('/archivos/')
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def upload(request):
    if 'user' in request.session:
        user = request.session['user']
        password = request.session['password']
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.cwd('~/upload/')
        if request.method == 'POST':
            file = request.FILES['file']
            ftp.storbinary(f'STOR {file.name}', file)
        ftp.quit()
    return render(request, 'home.html')

def archivos(request):
    if 'user' in request.session:
        user = request.session['user']
        password = request.session['password']
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.cwd('~/upload/')
        files = ftp.nlst()
        ftp.quit()
        if len(files) > 0:
            return render(request, 'archivos.html', {'files': files})
        else:
            return redirect('/upload/')
    return redirect('/')

def download(request, file_name):
    if 'user' in request.session:
        user = request.session['user']
        password = request.session['password']
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.cwd('~')
        local_file_path = f'./{file_name}'
        ftp.retrbinary(f'RETR {file_name}', open(local_file_path, 'wb').write)
        ftp.quit()
        with open(local_file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/force-download')
            response['Content-Disposition'] = f'attachment; filename={file_name}'
            return response
    return redirect('/')

def delete(request, file):
    if 'user' in request.session:
        user = request.session['user']
        password = request.session['password']
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.cwd('~')
        ftp.delete(file)
        ftp.quit()
    return redirect('/archivos/')

def rename(request, file):
    if 'user' in request.session:
        user = request.session['user']
        password = request.session['password']
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.cwd('~')
        if request.method == 'POST':
            new_name = request.POST.get('new_name')
            ftp.rename(file, new_name)
            ftp.quit()
            return redirect('/archivos/')
        ftp.quit()
        return render(request, 'rename.html', {'file': file})

    return render(request, 'rename.html')



