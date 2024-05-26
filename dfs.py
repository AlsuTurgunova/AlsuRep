# -*- coding: utf-8 -*-
"""Копия блокнота "Untitled10.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vMX1sa4XoZ18fkEh_ZOQdj1PJHYu9lZH
"""
"""
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')
"""
from collections import defaultdict

def depth_first_search(graph, start, end):
  """
  Функция, которая реализует обход в глубину (DFS) с возвратом длины пути.

  Args:
    graph: Граф, представленный в виде словаря, где ключ - вершина, значение - список смежных вершин.
    start: Стартовая вершина.
    end: Конечная вершина.

  Returns:
    Длина пути от стартовой вершины до конечной, или -1, если путь не найден.
  """

  visited = set()
  stack = [start]
  path_lengths = defaultdict(lambda: -1)  # Словарь для хранения длин путей
  path_lengths[start] = 0

  while stack:
    node = stack.pop()
    if node == end:  # Если достигнута конечная вершина, возвращаем длину пути
      return path_lengths[node]

    if node not in visited:
      visited.add(node)
      for neighbor in graph[node]:
        if neighbor not in visited:
          stack.append(neighbor)
          path_lengths[neighbor] = path_lengths[node] + 1  # Обновляем длину пути

  return -1  # Если путь не найден, возвращаем -1

# Пример использования
graph = {
  2: [4],
  1: [3],
  4: [2],
  3: [1],
}

start = 2
end = 4

path_length = depth_first_search(graph, start, end)
print(f"Длина пути от {start} до {end}: {path_length}") 
