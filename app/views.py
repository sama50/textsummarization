from django.shortcuts import render
from transformers import pipeline

# Create your views here.


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def home(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        summarizer_ans =  summarizer(input_text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        return render(request,'index.html',{'summarizer_ans':summarizer_ans})
    return render(request,'index.html')