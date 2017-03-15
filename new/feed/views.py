from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import story, comment
from .forms import CommentForm


class IndexView(generic.ListView):
	template_name = 'feed/index.html'
	context_object_name = 'all_stories'


	def get_queryset(self):
		return story.objects.all()

'''class DetailView(generic.DetailView):
	model = story
	template_name = 'feed/detail.html'
'''

def story_detail(request, pk):
	story_obj = get_object_or_404(story, pk=pk)
	#list of active comments for story
	comments = story_obj.comments.filter(active=True)

	if request.method == 'POST':
		# if a comment was posted
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			#create comment object but don't save to DB yet
			new_comment = comment_form.save(commit=False)
			#Assign the current story to comment
			new_comment.story = story_obj
			#save the comment to DB
			new_comment.save()
	else:
		comment_form = CommentForm()
	return render(request, 'feed/detail.html', {'story': story_obj, 'comments': comments, 'comment_form': comment_form})

'''def comment(request):
	#list of active comments for story
	comments = story.comments.filter(active=True)

	if request.method == 'POST':
		# if a comment was posted
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			#create comment object but don't save to DB yet
			new_comment.story = story
			#save the comment to DB
			new_comment.save()
	else:
		comment_form = CommentForm()
	return render(request, 'feed/detail.html', {'comments':comments,'comment_form':comment_form})
'''


class AddStory(CreateView):
	model = story
	fields = ['author', 'story_title', 'genre', 'content', 'story_logo']

class StoryUpdate(UpdateView):
	model = story
	fields = ['author', 'story_title', 'genre', 'content', 'story_logo']

class StoryDelete(DeleteView):
	model = story
	success_url = reverse_lazy('feed:index')



def about(request):
	return render(request, 'feed/about.html')


def profile(request):
	return render(request, 'feed/profile.html')


def story_like(request, pk):
	story_obj = get_object_or_404(story, pk=pk)
	story_obj.likes += 1
	story_obj.save()
	context = story.objects.all()
	return render(request, 'feed/index.html', {'all_stories': context})


'''def publish(request):
	if request.method == 'POST':
		form = PublishForm(request.POST,request.FILES)
		if form.is_valid():
			author = form.cleaned_data['author']
			story_title = form.cleaned_data['story_title']
			genre = form.cleaned_data['genre']
			content = form.cleaned_data['content']
			story_logo = request.FILES['story_logo']
			obj = story()
			obj.author = author
			obj.story_title = story_title
			obj.genre = genre
			obj.content = content
			obj.story_logo = story_logo
			obj.save()
			all_stories = story.objects.all()
			context = {'all_stories': all_stories}
			return render(request, 'feed/index.html', context)

	else:
		form = PublishForm()
	return render(request,'feed/publish.html',{'form': form})
'''