from django.db import connection
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.contrib.auth import login, logout
from users.forms import CreateUserForm, CreatePost
from grups.models import Company, PopularityCompany
from django.contrib.auth.decorators import login_required
from users.utils import (
    GetCompanyUserPost,
    autentic,
    CalculateRatingCompany,
)



def lgout(request):
    """Համակարգից դուրս գալու ֆունկցիա"""
    logout(request)
    return redirect("home")


def singin(request):
    """Համակարգ մուտք գործելու ֆունկցիա։"""
    if request.method == "POST":
        user = autentic(request, "username", "password")
        if user is not None:
            login(request, user)
            return redirect("home")
        # messages.info(request, 'username or password is incorrent')
    return render(request, "users/singin.html")


def registerPage(request):
    """կայքում Գրանցվելու ֆունկցիա"""
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #             # user = form.cleaned_data.get('username')
            #             # messages.success(request, 'akaunt created' + user)
            user = autentic(request, "email", "password1")
            login(request, user)
            return redirect("home")
    context = {"form": form}
    return render(request, "users/login.html", context)


def post(request, slug):
    """Կարծիքների կոնտռոիլեր"""
    posts = GetCompanyUserPost(slug=slug, request=request)
    context = posts.get_company_user_post()
    context["title"] = _("Post")
    return render(request, "users/post.html", context=context)

@login_required
def add_post(request, slug: str):
    """Կարծիք ավելացնելու կոնտրոիլեր։"""
    post = PopularityCompany.objects.filter(user=request.user, company__slug=slug)
    if post.exclude():
        return Http404("<p>դուք ցհեք կարող</p>")

    if request.method == "POST":
        form = CreatePost(data=request.POST)
        if form.is_valid():
            new_rating = form.cleaned_data["gnahatakan"]
            user = request.user
            comp = Company.objects.get(slug=slug)

            post = PopularityCompany.objects.create(
                gnahatakan=new_rating,
                post=form.cleaned_data["post"],
                user=user,
                company=comp,
            )
            ubdate_rating = CalculateRatingCompany(slug=slug, new_rating=new_rating)
            ubdate_rating.calculate_rating_new_post()
            return redirect('post', slug)
    form = CreatePost()

    context = {"form": form}
    return render(request, "users/add_post.html", context=context)

@login_required
def change_post(request, slug, user_id):
    """կարծիքի փոփոխման կոնտրոիլեր"""
    if request.user.id == user_id:
        post = (
            PopularityCompany.objects.filter(user=request.user, company__slug=slug)
        )[0]
        if request.user == post.user:
            old_reting = post.gnahatakan
            data = {"post": post.post, "gnahatakan": old_reting}

            if request.method == "POST":
                print(request.POST)
                form = CreatePost(data=request.POST)
                if form.is_valid():
                    new_rating = form.cleaned_data["gnahatakan"]
                    post.post = form.cleaned_data["post"]
                    post.gnahatakan = new_rating
                    post.save(update_fields=['post' , 'gnahatakan'])
                    ubdate_rating = CalculateRatingCompany(
                        slug=slug, old_rating=old_reting, new_rating=new_rating
                    )
                    ubdate_rating.ubdate_rating()
                    return redirect('post', slug)
            else: print(request.method)
            form = CreatePost(data)
            context = {
                "form": form,
                'title': _('Կարծիքներ'),
                "delete": _("Հեռացնել"),
                "update": _("Թարմացնել"),
                }
            return render(request, "users/add_post.html", context=context)


