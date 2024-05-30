from django.shortcuts import render
from django.http import HttpResponse
from ftplib import FTP
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.

ip_ftp ='192.168.43.246'

def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.quit()

        request.session['user'] = user
        request.session['password'] = password
        request.session['directory'] = '~/upload/'
        return redirect('/archivos/')
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def upload(request):
    if 'user' in request.session:
        user = request.session['user']
        password = request.session['password']
        directory = request.session['directory']
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.cwd(directory)
        if request.method == 'POST':
            file = request.FILES['file']
            ftp.storbinary(f'STOR {file.name}', file)
        ftp.quit()
    return render(request, 'home.html')

def upload_directory(request, directory):
    if 'user' in request.session:
        user = request.session['user']
        password = request.session['password']
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.cwd(f'~/upload/{directory}/')
        if request.method == 'POST':
            file = request.FILES['file']
            ftp.storbinary(f'STOR {file.name}', file)
        ftp.quit()
    return render(request, 'upload_directory.html' , {'directory': directory})


def archivos(request):
    if 'user' in request.session:
        user = request.session['user']
        password = request.session['password']
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.cwd('~/upload/')
        #file = ftp.nlst()
        directories = []
        files = []
        for item in ftp.nlst():
            try:
                ftp.cwd(item)  # Try to change to directory
                directories.append(item)
                ftp.cwd('..')  # Change back to parent directory
            except Exception as e:
                files.append(item)
        ftp.quit()

        if len(files) > 0 or len(directories) > 0:
            return render(request, 'archivos.html', {'files': files , 'directories': directories})
        else:
            return redirect('/upload/')
    return redirect('/')

def download(request, file_name):
    if 'user' in request.session:
        user = request.session['user']
        password = request.session['password']
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.cwd('~/upload/')
        local_file_path = f'./{file_name}'
        ftp.retrbinary(f'RETR {file_name}', open(local_file_path, 'wb').write)
        ftp.quit()
        with open(local_file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/force-download')
            response['Content-Disposition'] = f'attachment; filename={file_name}'
            return response
    return redirect('/')

def download_files(request,directory,file_name):
    if 'user' in request.session:
        user = request.session['user']
        password = request.session['password']
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.cwd(f'~/upload/{directory}/')
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
        ftp.cwd(f'~/upload/')
        ftp.delete(file)
        ftp.quit()
    return redirect('/archivos/')

def delete_files(request,directory, file):
    if 'user' in request.session:
        user = request.session['user']
        password = request.session['password']
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.cwd(f'~/upload/{directory}/')
        ftp.delete(file)
        ftp.quit()
    return redirect('/archivos/')

def delete_directory(request, directory):
    if 'user' in request.session:
        user = request.session['user']
        password = request.session['password']
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.cwd('~/upload/')
        ftp.rmd(directory)
        ftp.quit()
    return redirect('/archivos/')

def rename(request, file):
    if 'user' in request.session:
        user = request.session['user']
        password = request.session['password']
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.cwd('~/upload/')
        if request.method == 'POST':
            new_name = request.POST.get('new_name')
            ftp.rename(file, new_name)
            ftp.quit()
            return redirect('/archivos/')
        ftp.quit()
        return render(request, 'rename.html', {'file': file})

    return render(request, 'rename.html')

def create_directory(request):
    if 'user' in request.session:
        user = request.session['user']
        password = request.session['password']
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.cwd('~/upload/')
        if request.method == 'POST':
            directory = request.POST.get('directory')
            ftp.mkd(directory)
            ftp.quit()
            return redirect('/archivos/')
        ftp.quit()
        return render(request, 'create_directory.html')
    return render(request, 'create_directory.html')

def directory(request, directory):
    if 'user' in request.session:
        user = request.session['user']
        password = request.session['password']
        ftp = FTP(ip_ftp)
        ftp.login(user, password)
        ftp.cwd(f'~/upload/{directory}/')
        directories = []
        files = []
        for item in ftp.nlst():
            if ftp.nlst(item) == []:
                directories.append(item)
            else:
                files.append(item)
        ftp.quit()
        return render(request, 'directory.html', {'files': files , 'directories': directories, 'directory': directory})
       
    return render(request, 'directory.html', {'files': files , 'directories': directories,'directory': directory})
    






