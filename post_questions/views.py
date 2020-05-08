from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from post_questions.models import PostQuestion, Comment
from post_questions.forms import QuestionForm, CommentForm



class PostListView(ListView):
    model = PostQuestion

    def get_queryset(self):
        return PostQuestion.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')  # __lte less than or equal to field lookups sql query to filter queries


class PostDetailView(DetailView):
    model = PostQuestion


class PostCreateView(CreateView, LoginRequiredMixin):
    model = PostQuestion
    login_url = '/'
    redirect_field_name = 'post_questions/questions_detail.html'

# Decorators @login_required only work for function based views so here we use LoginrequiredMixin
# LoginRequiredMixin Require two Attributes 'login_url' if the user is not logged in
# and 'redirect_field_name'  if the user is logged in we redirect the user to the detail view.

    form_class = QuestionForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = PostQuestion
    login_url = '/'
    redirect_field_name = 'post_questions/questions_detail.html'

    # Decorators @login_required only work for function based views so here we use LoginrequiredMixin
    # LoginRequiredMixin Require two Attributes 'login_url' if the user is not logged in
    # and 'redirect_field_name'  if the user is logged in we redirect the user to the detail view.

    form_class = QuestionForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = PostQuestion
    success_url = reverse_lazy('post_list')

# Similar to post list view


class PostDraftListView(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = 'post_questions/post_list.html'
    model = PostQuestion

    def get_queryset(self):
        PostQuestion.objects.filter(published_date__isnull=True).order_by('created_date')


# refer forms


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(PostQuestion, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = CommentForm()
        return render(request, 'post_questions/comment_form.html', {'form': form})


@login_required
def comment_approved(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


@login_required
def post_publish(request, pk):
    post = get_object_or_404(PostQuestion, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

