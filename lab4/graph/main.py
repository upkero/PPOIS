from Graph import Graph


def _prompt_vertex() -> str:
    return input("Введите значение вершины: ").strip()


def _prompt_edge() -> tuple[str, str]:
    print("Укажите вершины ребра:")
    start = _prompt_vertex()
    end = _prompt_vertex()
    return start, end


def _handle_action(graph: Graph[str], action: str) -> bool:
    try:
        if action == "1":
            value = _prompt_vertex()
            graph.add_vertex(value)
            print(f"Вершина {value!r} добавлена.")
        elif action == "2":
            start, end = _prompt_edge()
            graph.add_edge(start, end)
            print(f"Ребро ({start!r}, {end!r}) добавлено.")
        elif action == "3":
            value = _prompt_vertex()
            graph.remove_vertex(value)
            print(f"Вершина {value!r} удалена.")
        elif action == "4":
            start, end = _prompt_edge()
            graph.remove_edge((start, end))
            print(f"Ребро ({start!r}, {end!r}) удалено.")
        elif action == "5":
            print("Текущее представление графа:")
            print(graph if not graph.empty() else "<пусто>")
        elif action == "6":
            print(f"Количество вершин: {graph.vertex_count()}")
            print(f"Количество ребер: {graph.edge_count()}")
        elif action == "7":
            value = _prompt_vertex()
            degree = graph.vertex_degree(value)
            print(f"Степень вершины {value!r}: {degree}")
        elif action == "8":
            start, end = _prompt_edge()
            degree = graph.edge_degree((start, end))
            print(f"Степень ребра ({start!r}, {end!r}): {degree}")
        elif action == "9":
            iterator = graph.vertex_iterator()
            values = [vertex.value for vertex in iterator.to_list()]
            print(f"Вершины по порядку добавления: {values}")
            reverse_values = [
                vertex.value for vertex in graph.vertex_reverse_iterator().to_list()
            ]
            print(f"Вершины в обратном порядке: {reverse_values}")
        elif action == "10":
            iterator = graph.edge_iterator()
            edges = [edge.as_value_pair() for edge in iterator.to_list()]
            print(f"Ребра: {edges}")
            reverse_edges = [
                edge.as_value_pair() for edge in graph.edge_reverse_iterator().to_list()
            ]
            print(f"Ребра (обратный обход): {reverse_edges}")
        elif action == "11":
            value = _prompt_vertex()
            iterator = graph.adjacent_vertex_iterator(value)
            neighbors = [vertex.value for vertex in iterator.to_list()]
            print(f"Смежные вершины для {value!r}: {neighbors}")
        elif action == "12":
            value = _prompt_vertex()
            iterator = graph.incident_edge_iterator(value)
            incident = [edge.as_value_pair() for edge in iterator.to_list()]
            print(f"Инцидентные ребра для {value!r}: {incident}")
        elif action == "0":
            return False
        else:
            print("Неизвестный пункт меню.")
    except Exception as error:
        print(f"Ошибка: {error}")
    return True


def main() -> None:
    graph: Graph[str] = Graph()
    actions = {
        "1": "Добавить вершину",
        "2": "Добавить ребро",
        "3": "Удалить вершину",
        "4": "Удалить ребро",
        "5": "Вывести граф",
        "6": "Показать количество вершин и ребер",
        "7": "Вычислить степень вершины",
        "8": "Вычислить степень ребра",
        "9": "Продемонстрировать итераторы вершин",
        "10": "Продемонстрировать итераторы ребер",
        "11": "Показать смежные вершины",
        "12": "Показать инцидентные ребра",
        "0": "Выход",
    }

    keep_running = True
    while keep_running:
        print("\nМеню:")
        for key, description in actions.items():
            print(f"{key}. {description}")
        choice = input("Выберите действие: ").strip()
        keep_running = _handle_action(graph, choice)


if __name__ == "__main__":
    main()
