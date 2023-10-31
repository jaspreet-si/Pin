from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):

        data=Pin.objects.all().order_by("?")
        return render(request,'home.html',{'data':data})

def user_profile(request):
    # Assuming you have a user object associated with the profile
    user = request.user
    user_pictures = Pin.objects.filter(Pin_by=user)
    
    # context = {
    #     'user_pictures': user_pictures,
    #     'user': user,
    # }
    
    return render(request, 'profilepage.html',{"v":user_pictures})




def Login(request):
    
    if request.method=="GET":

       return render(request,'login.html')
       
    else:
        username=request.POST['username']
       
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')

        else:
            messages.warning(request,'invalid username or password ')
            return redirect('signin')

def Signup(request):
    if request.method=='GET':
         return render(request,'signup.html')
    else:
         username=request.POST['username']
         pass1=request.POST['password']    
         pass2=request.POST['conf-password']    

         if pass1==pass2:
              
              if User.objects.filter(username=username).exists():

                messages.warning(request,'Username already exists')
                return redirect('signup')
              else:

                User.objects.create_user(username=username,password=pass1)
                messages.success(request,'account has been created')
                return redirect('signin')
         else:
           messages.warning(request,'password does not match')
           return redirect('signup')


def logout(request):
    auth.logout(request)
    return redirect('signin')        
  
@login_required(login_url='signin')

def addpin(request):
    if request.method=='GET':
        return render(request,'upload.html')
    else:
        by=request.user
        title=request.POST['title']
        Disc=request.POST['disc']
        img=request.FILES['pin']

        addpin=Pin(Pin_by=by,Pin_name=title,Pin_img=img,Pin_discription=Disc)
        addpin.save()

        return redirect('home')




@login_required(login_url='signin')
def profilepage(request):
    
    account=profile.objects.all()
    return render(request,'profilepage.html',{'account':account})

@login_required(login_url='signin')
def addprofile(request):
    if request.method=='GET':

        return render(request,'addprofile.html')
    else:
        Dp=request.FILES['DP']
        

        Profile=profile(profile_picture=Dp)
        Profile.save()
        return redirect('profileprofile')

def search(request):
    if request.method=='POST':
        search=request.POST['search']
        if Pin.objects.filter(Pin_name__contains=search).exists():
            data=Pin.objects.filter(Pin_name__contains=search)
            return render(request,'home.html',{'data':data})
        else:
            messages.warning(request,'invalid search')
            return redirect('home')
    else:
        return redirect('home')
    
def readMore(request,id):
    data = Pin.objects.get(id=id)
    commentbox = Comments.objects.filter(Comment_on=data)
    number_of_likes = data.number_of_likes()

    liked=False
    if data.Likes.filter(id=request.user.id).exists():
        liked=True

    return render (request,'readMore.html',{'data':data,'comment':commentbox,'number_of_likes':number_of_likes,'liked':liked})

@login_required(login_url='signin')
def CommentBox(request,id,Post):
    if request.method == 'POST':
        Post = int(request.POST['postid'])
        Comment = request.POST['comment']
        Comment_by = int(request.POST['profileid'])

        dataid = Pin.objects.get(id=Post)
        print(dataid)
        dataname = User.objects.get(id=Comment_by)
        Comments.objects.create(Comment_on=dataid,Comment=Comment,Comment_by=dataname)
        return redirect('readMore',id=Post )
    else:
        messages.error(request,'Comment Failed')
        return redirect('readMore',id=Post)


@login_required(login_url='signin')

def DeleteCommentById(request,id,postid):
    
    id=Comments.objects.get(id=id).delete()
    return redirect('readMore',id=postid)


@login_required(login_url='signin')
def LikePin(request,id):
    pin = get_object_or_404(Pin,id=request.POST['Pin_id'])
    liked=False
    if pin.Likes.filter(id=request.user.id).exists():
        pin.Likes.remove(request.user)
        liked=False

    else:
        pin.Likes.add(request.user)
        liked=True
    return redirect('readMore',id=id)

@login_required(login_url='signin')
def deletePin(request,id):
    Pin.objects.get(id=id).delete()

    return redirect('home')

@login_required(login_url='signin')
def update_profile(request,id):
    data = profile.objects.get(id=id)
    if request.user.is_authenticated:
        if profile.objects.filter(name__exact=request.user).exists():
            if request.method == "POST":
                profile_photo = request.FILES['profile_photo']
                profile(id=id,name=data.username,profile_photo=profile_photo).save()
                return redirect('profileprofile')
            else:
                return render(request,'addProfile.html')
        else:
            return redirect('profileprofile')
    else:
        return redirect('signin')