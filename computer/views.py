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
def checkout2(request,id):
  template=loader.get_template('checkout2.html')
  currentUser=request.user
  print(currentUser.id)
  computer=itemDetails.objects.select_related('itemsid').filter(id=id)
  context={
    'computer':computer,
    'request':request
  }
  return HttpResponse(template.render(context))

def shopcomputer(request):
  template=loader.get_template('shopcomputer.html')
  computer=itemDetails.objects.select_related('itemsid')
  context={''}
  return HttpResponse(template.render({'computer':computer,'request':request}))
  
def detail(request , id):
  template=loader.get_template('detail.html')
  computer=itemDetails.objects.select_related('itemsid').filter(id=id)
  print(computer.query)
  context={
    'computer':computer,
    'request':request
  }
  return HttpResponse(template.render(context))

def add_to_card(request,id):
  currentuser=request.user
  discount=2
  state=False
  computer=itemDetails.objects.select_related('itemsid').filter(id=id)
  count=0
  for item in computer:
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
     
