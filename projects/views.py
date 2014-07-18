from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from projects.forms import ProjectUserCreationForm, UserForm, CompanyForm, DeveloperForm, ProjectForm
from projects.models import Project, Company, Developer


def home(request):
    open_projects = Project.objects.filter(date__gt=datetime.today())
    completed_projects = Project.objects.filter(date__lt=datetime.today())
    data = {'open_projects': open_projects, 'completed_projects': completed_projects}
    return render(request, "home.html", data)

"""
USER PROFILES
"""

def register(request):
    if request.method == 'POST':
        form = ProjectUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("profile")
    else:
        form = ProjectUserCreationForm()
    data = {"form", form}
    return render(request, "registration/register.html", data)


@login_required
def profile(request):
    data = {'user': request.user}
    return render(request, 'profile/profile.html', data)


@login_required
def profile_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserForm(instance=user)
    data = {"user": request.user, "form": form}
    return render(request, "profile/profile_update.html", data)


"""
COMPANIES
"""


def companies(request):
    companies = Company.objects.all()
    return render(request, "company/companies.html", {'companies': companies})




def view_company(request, company_id):
    company = Company.objects.get(id=company_id)
    data = {"company": company}
    return render(request, "company/view_company.html", data)



def new_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/companies")
    else:
        form = CompanyForm()
    data = {'form': form}
    return render(request, "company/new_company.html", data)



@staff_member_required
def edit_company(request, company_id):
    company = Company.objects.get(id=company_id)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            if form.save():
                return redirect("/companies/{}".format(company_id))
    else:
        form = CompanyForm(instance=company)
    data = {"company": company, "form": form}
    return render(request, "company/edit_company.html", data)



@staff_member_required
def delete_company(request, company_id):
    company = Company.objects.get(id=company_id)
    company.delete()
    return redirect("/companies")





"""
PROJECTS
"""

def projects(request):
    all_projects = Project.objects.all()
    data = {"projects": all_projects}
    return render(request, "projects/projects.html", data)


def view_project(request, project_id):
    project = Project.objects.get(id=project_id)
    data = {"project": project}
    return render(request, "projects/view_project.html", data)


def new_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/projects")
    else:
        form = ProjectForm()
    data = {"form": form}
    return render(request, "projects/new_project.html", data)



@staff_member_required
def edit_project(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            if form.save():
                return redirect("/projects/{}".format(project_id))
    else:
        form = ProjectForm(instance=project)
    data = {"project": project, "form": form}
    return render(request, "projects/edit_project.html", data)


@staff_member_required
def delete_project(request, project_id):
    project = Project.objects.get(id=project_id)
    project.delete()
    return redirect("/projects")




"""
DEVELOPERS
"""

def developers(request):
    developers = Developer.objects.all()
    data = {"developers", developers}
    return render(request, "developer/developers.html", data)



def view_developer(request, developer_id):
    developer = Developer.objects.get(id=developer_id)
    data = {"developer": developer}
    return render(request, "developer/view_developer.html", data)



def new_developer(request):
    if request.method == "POST":
        form = DeveloperForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/developers")
    else:
        form = DeveloperForm()
    data = {"form": form}
    return render(request, "developer/new_developer.html", data)


@staff_member_required
def edit_developer(request, developer_id):
    developer = Developer.objects.get(id=developer_id)
    if request.method == "POST":
        form = DeveloperForm(request.POST, instance=developer)
        if form.is_valid():
            if form.save():
                return redirect("/developers/{}".format(developer_id))
    else:
        form = DeveloperForm(instance=developer)
    data = {"developer": developer, "form": form}
    return render(request, "developer/edit_developer.html", data)


@staff_member_required
def delete_developer(request, developer_id):
    developer = Developer.objects.get(id=developer_id)
    developer.delete()
    return redirect("/developers")
