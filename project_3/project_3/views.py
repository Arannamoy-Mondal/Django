from django.shortcuts import render

def home(request):
    data=[
        {
"userId": 1,
"id": 1,
"title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
"body": "quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam nostrum rerum est autem sunt rem eveniet architecto"
},
{
"userId": 1,
"id": 2,
"title": "qui est esse",
"body": "est rerum tempore vitae sequi sint nihil reprehenderit dolor beatae ea dolores neque fugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis qui aperiam non debitis possimus qui neque nisi nulla"
},
{
"userId": 1,
"id": 3,
"title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
"body": "et iusto sed quo iure voluptatem occaecati omnis eligendi aut ad voluptatem doloribus vel accusantium quis pariatur molestiae porro eius odio et labore et velit aut"
},
{
"userId": 1,
"id": 4,
"title": "eum et est occaecati",
"body": "ullam et saepe reiciendis voluptatem adipisci sit amet autem assumenda provident rerum culpa quis hic commodi nesciunt rem tenetur doloremque ipsam iure quis sunt voluptatem rerum illo velit"
},
{
"userId": 1,
"id": 5,
"title": "nesciunt quas odio",
"body": "repudiandae veniam quaerat sunt sed alias aut fugiat sit autem sed est voluptatem omnis possimus esse voluptatibus quis est aut tenetur dolor neque"
},
{
"userId": 1,
"id": 6,
"title": "dolorem eum magni eos aperiam quia",
"body": "ut aspernatur corporis harum nihil quis provident sequi mollitia nobis aliquid molestiae perspiciatis et ea nemo ab reprehenderit accusantium quas voluptate dolores velit et doloremque molestiae"
},
{
"userId": 1,
"id": 7,
"title": "magnam facilis autem",
"body": "dolore placeat quibusdam ea quo vitae magni quis enim qui quis quo nemo aut saepe quidem repellat excepturi ut quia sunt ut sequi eos ea sed quas"
}
    ]
    return render(request,"home.html",{'data':data})


def aboutPage(request,id):
    return render(request,'index.html',{'id':id})

def contact(request):
    data=[
{
"albumId": 1,
"id": 1,
"title": "accusamus beatae ad facilis cum similique qui sunt",
"url": "https://via.placeholder.com/600/92c952",
"thumbnailUrl": "https://via.placeholder.com/150/92c952"
},
{
"albumId": 1,
"id": 2,
"title": "reprehenderit est deserunt velit ipsam",
"url": "https://via.placeholder.com/600/771796",
"thumbnailUrl": "https://via.placeholder.com/150/771796"
},
{
"albumId": 1,
"id": 3,
"title": "officia porro iure quia iusto qui ipsa ut modi",
"url": "https://via.placeholder.com/600/24f355",
"thumbnailUrl": "https://via.placeholder.com/150/24f355"
},
{
"albumId": 1,
"id": 4,
"title": "culpa odio esse rerum omnis laboriosam voluptate repudiandae",
"url": "https://via.placeholder.com/600/d32776",
"thumbnailUrl": "https://via.placeholder.com/150/d32776"
},
{
"albumId": 1,
"id": 5,
"title": "natus nisi omnis corporis facere molestiae rerum in",
"url": "https://via.placeholder.com/600/f66b97",
"thumbnailUrl": "https://via.placeholder.com/150/f66b97"
},
{
"albumId": 1,
"id": 6,
"title": "accusamus ea aliquid et amet sequi nemo",
"url": "https://via.placeholder.com/600/56a8c2",
"thumbnailUrl": "https://via.placeholder.com/150/56a8c2"
},
{
"albumId": 1,
"id": 7,
"title": "officia delectus consequatur vero aut veniam explicabo molestias",
"url": "https://via.placeholder.com/600/b0f7cc",
"thumbnailUrl": "https://via.placeholder.com/150/b0f7cc"
},
{
"albumId": 1,
"id": 8,
"title": "aut porro officiis laborum odit ea laudantium corporis",
"url": "https://via.placeholder.com/600/54176f",
"thumbnailUrl": "https://via.placeholder.com/150/54176f"
},
    ]
    return render(request,"contact.html",{'data': data })