from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import items,itemDetails, cart
from .forms import CreateUserForm,LoginUserForm
from django.contrib.auth import login , logout ,  authenticate
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/auth_login/')
def checkout(request,id):
  template=loader.get_template('checkout.html')
  currentuser=request.user
  print(currentuser.id)
  phone=itemDetails.objects.select_related('itemsid').filter(id=id)
  context={
    'phone':phone,
    'request':request
  }
  return HttpResponse(template.render(context))

def index(request):
  template=loader.get_template('index.html')
  return HttpResponse(template.render({'request':request}))

def add_to_card(request,id):
  currentuser=request.user
  discount=2
  state=False
  phone=itemDetails.objects.select_related('itemsid').filter(id=id)
  count=0
  for item in phone:
     net=item.total-discount
  Cart = cart(
    id_product=item.id, 
    id_user=currentuser.id,
    price=item.price,
    qty=item.qty,
    tax=item.tax,
    total=item.total,
    discount=discount,
    net=net,
    state=state
  )
  currentuser=request.user.id
  count=cart.objects.filter(id_user=currentuser).count()
  print(count)
  Cart.save()
  request.session['countcart']=count
  return redirect("/")


def showphone(request):
  template=loader.get_template('showphone.html')
  phone=itemDetails.objects.select_related('itemsid')
  print(phone.query)
  return HttpResponse(template.render({'phone':phone , 'request':request}))

def details(request,id):
  template=loader.get_template('details.html')
  currentuser=request.user
  print(currentuser.id)
  phone=itemDetails.objects.select_related('itemsid').filter(id=id)
  print(phone.query)
  context={
    'phone':phone,
    'request':request
  }
  return HttpResponse(template.render(context))


@csrf_exempt
def auth_register(request):
  template=loader.get_template('auth_register.html')
  form=CreateUserForm()
  if request.method=="POST":
    form=CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('auth_login')
  context={'registerform':form}
  return HttpResponse(template.render(context=context))
@csrf_exempt
def auth_logout(request):
   if request.method=="POST":
    logout(request)
    return redirect("/")

@csrf_exempt
def auth_login(request):
  form=LoginUserForm()
  if request.method=="POST":
    form=LoginUserForm(data=request.POST)
    if form.is_valid():
      username=form.cleaned_data['username']
      password=form.cleaned_data['password']
      user=authenticate(username=username,password=password)
      if user:
        if user.is_active:
          login(request,user)
          return render(request, 'index.html')
  context={'form':form}
  return render(request,'auth_login.html',context)
     
