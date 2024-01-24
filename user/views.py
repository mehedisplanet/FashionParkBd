from django.shortcuts import render, redirect   
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.template.loader import render_to_string
from .forms import UserRegistrationForm  
from django.utils.encoding import force_bytes   
from django.core.mail import EmailMessage  
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from django.views.generic import ListView
from product.models import Purchase,WishList


# Create your views here.
def signup(request):  
    if request.method == 'POST':  
        form = UserRegistrationForm(request.POST)  
        if form.is_valid():   
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('user/conEmail.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':default_token_generator.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return redirect('home')
    else:  
        form = UserRegistrationForm()  
    return render(request, 'user/userReg.html', {'form': form}) 

def activate(request, uidb64, token):  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and default_token_generator.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return redirect('home')
    else:
        return redirect('register')


class UserLoginView(LoginView):
    template_name = 'user/userLogin.html'
    def get_success_url(self):
        messages.success(self.request, "Login successfully")
        return reverse_lazy('home')
    
def UserLogout(request):
    logout(request)
    return redirect('home')


class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'user/profile.html'

    def get(self, request):
        user_purchases = Purchase.objects.filter(user=request.user)

        return render(request, self.template_name, {
            'user_purchases': user_purchases,
        })
    
class BasketView(LoginRequiredMixin, ListView):
    template_name = 'user/basket.html'

    def get(self, request):
        user_purchases = Purchase.objects.filter(user=request.user)

        return render(request, self.template_name, {
            'user_purchases': user_purchases,
        })
    
class WishlistView(LoginRequiredMixin, ListView):
    template_name = 'user/wishlist.html'

    def get(self, request):
        user_purchases = WishList.objects.filter(user=request.user)

        return render(request, self.template_name, {
            'user_wishlist': user_purchases,
        })


