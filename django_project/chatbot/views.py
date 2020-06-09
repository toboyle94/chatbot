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

    def post(self, request, *args, **kwargs):
        new_question_text = request.POST['question_text']
        question = self.get_object()

        QuestionText.objects.create(text=new_question_text, question=question)
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()

        diffs_to_current = []
        for old_text in self.object.previous_text_versions:
            text_diff = ndiff(old_text.split(), self.object.current_text.split())
            diffs_to_current.append(text_diff)

        context_data['previous_text_version_diffs'] = diffs_to_current
        return context_data
