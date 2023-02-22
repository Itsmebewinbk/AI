
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import openai

# Set up OpenAI API key and model engine
openai.api_key = "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"
model_engine = "text-davinci-003"

@csrf_exempt
def generate_text(request):
    if request.method == 'POST':
        # Get the text from the form data
        text = request.POST.get('text')

        # Use OpenAI API to generate text based on the input
        completion = openai.Completion.create(engine=model_engine,
            prompt=text,
            temperature=0.9,
            max_tokens=1024,
            n=1,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=None
        )
        response = completion.choices[0].text

        # Return the generated text as a response
        return HttpResponse(response)
    else:
        # Render the template with the form
        return render(request, 'form_template.html')
