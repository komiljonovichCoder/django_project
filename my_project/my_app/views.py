from django.shortcuts import render

names = {
    'Ikromjon': {
        "name": "Ikromjon",
        "surname": "Odiljonov",
        "age": 23,
        "profession": "Math Teacher",
        "contact": "+998916813162",
        "about": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    }, 
    'Murodjon': {
        "name": "Murodjon",
        "surname": "Tohirov",
        "age": 26,
        "profession": "Programmer",
        "contact": "+998977777777",
        "about": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    },
    'Boburjon': {
        "name": "Boburjon",
        "surname": "G'ulomov",
        "age": 25,
        "profession": "3D Designer",
        "contact": "+998955555555",
        "about": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    },
    'A\'zamjon': {
        "name": "A'zamjon",
        "surname": "Usmonaliyev",
        "age": 22,
        "profession": "IT Teacher",
        "contact": "+998933333333",
        "about": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    },
}

def index(request):
    return render(request, 'index.html', context={"names": names})

def main(request):
    return render(request, 'main.html', context={"names": names})

def about(request):
    return render(request, 'about.html', context={"names": names})

def contact(request):
    return render(request, 'contact.html', context={"names": names}) 