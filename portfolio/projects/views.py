from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required


def projects(request):
    projects = Project.objects.all()
    context={'projects':projects}
    return render(request, "projects/projects.html", context)

def project(request, pk):
    projectOBj = Project.objects.get(id = pk)
    return render(request, "projects/single-project.html", {'project': projectOBj})

@login_required(login_url='login')

# ensures projects are associated with a specific user
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        profile = request.user.profile
        if form.is_valid():
            project = form.save(commit = False)
            project.owner = profile
            project.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context )

# ensures a user can update only his project
@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form  = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
           
    context = {'form': form}
    return render(request, 'projects/project_form.html', context )

# ensures only a user can delete his project
@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    # the delete template is in the root directory and used across the project when needed.
    return render(request, 'delete_template.html', context)
    