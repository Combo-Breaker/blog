from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.utils import timezone
from .models import Post, Board, Comment
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.db.models import Count
from django.contrib.sites.models import Site
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _
from django.utils.six.moves.urllib.parse import urlparse
from django.contrib.syndication.views import Feed


def board_list(request):
    boards = Board.objects.all()
    return render(request, 'blog/board_list.html', {'boards': boards})

def board_detail(request, pk):
    boards = Board.objects.all()
    posts = Post.objects.filter(board=pk).order_by('-published_date')
    board = Board.objects.get(pk=pk)
    return render(request, 'blog/post_list.html', {'posts': posts, 'board':board, 'boards': boards})

def post_new(request, bd):
        board_get=Board.objects.get(pk=bd)
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.board = board_get
                post.published_date = timezone.now()
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def comment_new(request, post):
        post_get=Post.objects.get(pk=post)
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post_get
                comment.published_date = timezone.now()
                comment.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        '''
        else:
            form = CommentForm()
        return render(request, 'blog/post_edit.html', {'form': form})
'''

def post_detail(request, pk):
    boards = Board.objects.all()
    comments = Comment.objects.filter(post=pk).order_by('-published_date')
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'comments' : comments, 'boards': boards})


def e404(request):
    return render(request, 'blog/404.html', {}, status=404)

# class post_list(ListView):
#     model = Post
#     paginate_by = 2

#     def get_queryset(self):
#         qs = super(post_list, self).get_queryset()
#         return qs.annotate(Count('comment')).all()


# class board_list(post_list):
#     def get_board(self):
#         return get_object_or_404(Board, slug=self.kwargs['slug'])

#     def get_queryset(self):
#         qs = super(board_list, self).get_queryset()
#         return qs.filter(board=self.get_board())

#     def get_context_data(self, **kwargs):
#         ctx = super(board_list, self).get_context_data(**kwargs)
#         ctx['board'] = self.get_category()
#         return ctx

'''
def post_list(request):
    board = Board.objects.get(name = 'Flood') #ПЕРЕДЕЛАТЬ
    posts = Post.objects.filter(board = board).filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

#def comment_list(request):
#    post = Board.objects.get(title = 'Sample title')
#    comments = Comment.objects.filter(post = post).filter(published_date__lte=timezone.now()).order_by('published_date')
#    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def board_list(request):
    boards = Board.objects.all()
    return render(request, 'blog/board_list.html', {'boards': boards})


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('blog.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'blog/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
'''