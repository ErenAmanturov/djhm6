from django.shortcuts import render
from posts.models import Post, Comment
from posts.forms import PostForms, CommentForms
from django.http import HttpResponse
from django.shortcuts import redirect


def get_user_from_request(request):
    return request.user if not request.user.is_anonymous else None


def main(request):
    if request.method == 'GET':

        posts = Post.objects.all()

        data = {
            "posts": posts,
            'user': get_user_from_request(request)
        }

        return render(request, 'posts.html', context=data)


def post_detail(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        comments = Comment.objects.filter(post=post)
        data = {
            'post': post,
            'comments': comments,
            'comment_form': CommentForms,
            'user': get_user_from_request(request)
                }
        return render(request, 'detail.html', context=data)

    if request.method == 'POST':
        form = CommentForms(request.POST)
        if form.is_valid():
            Comment.objects.create(
                author=form.cleaned_data.get('author'),
                text=form.cleaned_data.get('text'),
                post_id=id
            )
            return redirect(f'/posts/{id}/')
        else:
            return render(request, 'detail.html', context={
                'comment_form': form,
                'user': get_user_from_request(request)
            })


def create_post(request):

    if request.method == 'GET':
        return render(request, 'create_post.html', context={
            'post_form': PostForms,
            'user': get_user_from_request(request)})

    if request.method == 'POST':
        form = PostForms(request.POST)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                stars=form.cleaned_data.get('stars'),
                type=form.cleaned_data.get('type')
            )
            return redirect('/')
        else:
            return render(request, 'create_post.html', context={
                'post_form': form,
                'user': get_user_from_request(request)
            })


# def edit_post(request, posts_id):
#     if request.method == 'GET':
#         return render(request, 'edit_post.html', context={
#             'edited_post_form': PostForms,
#             'post': posts_id
#         })
#     if request.method == 'POST':
#         form = PostForms(request.POST)
#         if form.is_valid():
#             Post.title = request.data.get('title')
#             Post.description = request.data.get('description')
#             Post.type = request.data.get('type')
#             Post.date = request.data.get('date')
#             Post.stars = request.data.get('stars')
#
#             Post.save()
#
#             return Response(data={"message": "Successfully updated product",
#                                 "product":  ProductListSerializer(product).data})
#         else:
#             return render(request, 'edit_post.html', context={
#                 'edited_post_form': form,
#                 'posts': posts_id
#             })
