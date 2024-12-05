from django.http import HttpResponse
from django.template import loader
from .forms import UserForm, CustomerForm, OrderForm
from .models import *





def customer(request):
    template = loader.get_template("sales/index.html")
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        u = {'name': name, 'age': age, 'lastname': lastname, 'phone': phone, 'email': email}
        content = get_context('Customer', u)
        u = Customer(name=name, age=age, lastname=lastname, phone=phone, email=email)
        print(1)
        u.save()
    else:
        userform = CustomerForm()
        content = get_context('Customer', {"form": userform})

    return HttpResponse(template.render(content, request))

def order(request):
    template = loader.get_template("sales/index.html")
    if request.method == "POST":
        date = request.POST.get("date")
        total = request.POST.get("total")
        customer = request.POST.get("customer")
        seller = request.POST.get("seller")
        item = request.POST.get("item")

        u = {'date': date, 'total': total, 'customer': customer, 'seller': seller, 'item': item}
        content = get_context('Order', u)
        u = Order(date=date, total=total, customer=customer, seller=seller, item=item)
        print(1)
        u.save()
    else:
        orderform = OrderForm()
        content = get_context('Order', {"form": orderform})

    return HttpResponse(template.render(content, request))


def user_age(request):
    template = loader.get_template("sales/index.html")
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        u = {'name': name, 'age': age}
        content = get_context('Пользователь', u)
        u = Customer(name=name, age=age)
        u.save()
    else:
        userform = UserForm()
        content = get_context('Пользователь', {"form": userform})
    return HttpResponse(template.render( content,request))


# def seller(request):
#     template = loader.get_template("sales/seller.html")
#     userform = UserForm()
#     context = get_context('Имя продавца', {"form": userform})
#     return HttpResponse(template.render(context, request ))

def get_context(title, d=None):
    context = {'title': title,
               'pages': [('Главная страница', 'Имя продавца'),
                         ]
               }
    if d:
        for k in d:
            context[k] = d[k]
    return context