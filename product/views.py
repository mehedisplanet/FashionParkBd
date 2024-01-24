from django.contrib import messages
from .models import Product
from django.shortcuts import redirect
from django.views import View
from django.views.generic import DetailView
from .forms import ReviewForm
from product.models import Purchase,WishList
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
# Create your views here.



class DetailsPostView(DetailView):
    model = Product
    pk_url_kwarg = 'id'
    template_name = 'productDetails.html'
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = ReviewForm(request.POST, product=post, user=request.user)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.success(request, 'Your review has been added successfully!')
            return self.get(request, *args, **kwargs)
        
        else:
            if not Purchase.objects.filter(user=request.user, product=post).exists():
                messages.error(request, 'Can not added your review , if you can give this Product review must be purchased it')
            return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        reviews = post.comments.all()
        review_form=ReviewForm()
            
        context['reviews']= reviews
        context['review_form']= review_form
        return context
    


class PurchaseView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        Purchase.objects.create(user=request.user, product=product)
        request.user.save()
        messages.success(request, "Purchase successful.")
        return redirect('/')
    
class WishlistView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        WishList.objects.create(user=request.user, product=product)
        request.user.save()
        messages.success(request, "Wishlist Add Successful.")
        return redirect('/')