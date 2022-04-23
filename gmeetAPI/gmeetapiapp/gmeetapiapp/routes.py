def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/ex')
    config.add_route('listevents', '/')
    config.add_route('createevents', '/createevents')
    config.add_route('createmeeting', '/createmeeting')
