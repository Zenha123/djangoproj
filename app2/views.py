from django.shortcuts import render,redirect
from . models import MovieInfo
from . forms import MovieForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create(request):
    frm=MovieForm()
    if request.POST:

        #print(request.POST)
        frm=MovieForm(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('list')
           
        else:
            frm=MovieForm()
    return render(request,'create.html',{'frm':frm })

def edit(request,pk):
    instance_edit=MovieInfo.objects.get(pk=pk)
    if request.POST:
        title=request.POST.get('title')
        year=request.POST.get('year')
        description=request.POST.get('description')
        instance_edit.title=title
        instance_edit.year=year
        instance_edit.description=description
        instance_edit.save()
    frm=MovieForm(instance=instance_edit)
    return render(request,'create.html',{'frm':frm })

def list(request):
    data=MovieInfo.objects.all()
    print(data)
    return render(request,'list.html',{'movies':data})

def delete (request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()
    data=MovieInfo.objects.all()
    return render(request,'list.html',{'movies':data}) 