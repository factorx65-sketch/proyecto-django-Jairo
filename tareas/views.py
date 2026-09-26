from django.shortcuts import render
from .models import Tareas
from django.shortcuts import get_object_or_404


def inicio(request):
    tareas = Tareas.objects.all()
    
    return render(request,"inicio.html",{'tareas':tareas})
def crearTarea(request):
    if request.method == 'GET':
        print(request.GET)
        return render(request,"crear_tarea.html")
    else:
        try:
           tareas = Tareas(
               Titulo = request.POST.get('titulo'),
               descripcion = request .POST.get('descripcion',''),
               fecha = request.POST.get('fecha',"2026-01-01")
            )
           tareas.save()
           redirec('crearTarea')
        except ValueError as e:
             return render(request,"crear_tarea.html",{
            "error" : e
            })
def detalleTarea(request,tarea_id):
    if request.method == 'GET' :
        tarea = get_object_or_404(Tareas,pk =tarea_id)
        return render(request,'detalle_tarea.html',{
            'tarea':tarea
        })
    else:
           tarea = get_object_or_404(Tareas,pk = tarea_id)
           tarea.Titulo = request.POST.get('titulo')
           tarea.descripcion= request.POST.get('descripcion')
           tarea.fecha = request.POST.get('fecha')
           tarea.save()
           return redirect('inicio')
     
def eliminarTarea(request, tarea_id):
         tarea = get_object_or_400(tareas,pk=tarea_id)
         tarea.delete()
         return redirect('inicio')
         
    

