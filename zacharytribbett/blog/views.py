from django.shortcuts import render
from django.views import generic

from .models import Post

class IndexView(generic.ListView):
	template_name = 'blog/post_list.html'

	def get_queryset(self):
		"""
		Return the last five published posts 
		"""
		return Post.objects.filter(
			published__isnull=False
		).order_by('-published')[:5]