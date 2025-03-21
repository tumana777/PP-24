def visit_counter(request):
    if request.user.is_authenticated:
        visits = request.session.get('visits', 0)
        visits += 1
        request.session['visits'] = visits
    else:
        visits = 0
    print(visits)
    return {'visits': visits}