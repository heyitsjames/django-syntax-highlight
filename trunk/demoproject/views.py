from django.shortcuts import render_to_response
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
styles = list(get_all_styles())
syntaxes = [lexer[0] for lexer in get_all_lexers()]

def demo(request):
    context = {'syntaxes': syntaxes,'styles': styles}
    if request.method == 'POST':
        context.update({'code' : request.POST.get('code'),'syntax' : request.POST.get('syntax'), 'style':request.POST.get('style')})
        return render_to_response('demo.html', context)
    return render_to_response('demo.html', context)