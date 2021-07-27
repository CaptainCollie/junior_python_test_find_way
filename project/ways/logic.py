from trains.models import Train


def dfs_paths(graph, start, finish):
    """Функция поиска всех возможных маршрутов из одного города в другой"""
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == finish:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.start_city_id, set())
        graph[q.start_city_id].add(q.finish_city_id)
    return graph


def get_ways(request, form) -> dict:
    context = {'form': form}
    qs = Train.objects.all().select_related('start_city', 'finish_city')
    graph = get_graph(qs)
    data = form.cleaned_data
    start = data['start_city']
    finish = data['finish_city']
    btw = data['btw']
    ways = list(dfs_paths(graph, start.id, finish.id))
    if not len(ways):
        raise ValueError('Way does no exist')
    if btw:
        _btw = [city.id for city in btw]
        right_ways = []
        for way in ways:
            if all(city in way for city in _btw):
                right_ways.append(way)
        if not right_ways:
            raise ValueError('No way')
    else:
        right_ways = ways
    roads = []
    all_trains = {}
    for q in qs:
        all_trains.setdefault((q.start_city_id, q.finish_city_id), [])
        all_trains[(q.start_city_id, q.finish_city_id)].append(q)
    for way in list(right_ways):
        tmp = {}
        tmp['trains'] = []
        total_time = 0
        for i in range(len(way) - 1):
            qs = all_trains[(way[i], way[i + 1])]
            q = qs[0]
            total_time += q.travel_time
            tmp['trains'].append(q)
        tmp['total_time'] = total_time
        roads.append(tmp)
    if not roads:
        raise ValueError('No trains')

    sorted_roads = []
    if len(roads) == 1:
        sorted_roads = roads
    else:
        times = list(set(road['total_time'] for road in roads))
        times.sort()
        for time in times:
            for road in roads:
                if time == road['total_time']:
                    sorted_roads.append(road)

    context['ways'] = sorted_roads
    context['btw'] = {'start_city': start, 'finish_city': finish}

    return context
