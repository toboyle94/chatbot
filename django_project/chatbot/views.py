from difflib import ndiff

from django.views.generic import ListView, DetailView
from chatbot.models import Question, QuestionText


class QuestionList(ListView):
    model = Question
    template_name = 'question_list.html'
    context_object_name = 'questions'


class QuestionDetail(DetailView):
    model = Question
    template_name = 'question.html'
    slug_url_kwarg = 'id'
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()

        previous_text_version_diffs = []
        for question_text in self.object.text_variations.order_by('-created')[1:]:
            text_diff = ndiff(question_text.text.split(), self.object.current_text.split())
            previous_text_version_diffs.append(text_diff)

        context_data['previous_text_version_diffs'] = previous_text_version_diffs
        return context_data
