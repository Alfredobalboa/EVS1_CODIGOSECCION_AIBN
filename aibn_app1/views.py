from django.shortcuts import render
from django.http import HttpResponse


def vista1(request):
    html = """
    <style>
    h1 {
        background-color: black;
        color: black;
    }
    h1:hover {
        color: white;
    }
    img {
        width: 200px;
        height: auto;
    }
    </style>
    <h1>esta es la vista 1</h1>
    <img src="https://i.kinja-img.com/gawker-media/image/upload/s--zuGpIoEo--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/arcpyf4oh7wtrwlbjn04.jpg" alt="aqui deberia haber una imagen xd">
    <br>
    <input type="text">
    """
    return HttpResponse(html)

def vista2(request):
    html = """
    <style>
    h1 {
        background-color: black;
        color: black;
    }
    h1:hover {
        color: white;
    }
    img {
        width: 200px;
        height: auto;
    }
    </style>
    <h1>esta es la vista 2</h1>
    <img src="https://th.bing.com/th/id/OIP.dQO-VTn5GVuANksPgEBxgAHaKK?pid=ImgDet&rs=1" alt="aqui deberia haber una imagen xd">
    <br>
    <input type="text">
    """
    return HttpResponse(html)