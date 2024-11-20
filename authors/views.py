from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from posts.models import Post
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request,'profile.html', {'data': data})
def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations! Your Account Created Successfully!')
            form.save()
            return redirect('login')
    else:
        form = forms.RegisterForm()
    return render(request, 'register.html', {'form': form, 'type': 'Register'})        

        
 
class UserLogin(LoginView):
    template_name ='register.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self,form):
        messages.success(self.request, 'Logged in successfully!')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request, 'Login information is incorrect!')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'login'
        return context

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = forms.UpdateUserData(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile Updated Successfully!')
            return redirect('profile')
    else:
        form = forms.UpdateUserData(instance = request.user)
    return render(request, 'update_profile.html', {'form':form})    

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! Your Password Changed Successfully!')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request, 'pass_change.html', {'form': form})


@login_required

def user_logout(request):
    messages.warning(request, 'Logout Successfully!')
    logout(request)
    return redirect('home')