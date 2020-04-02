#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Time: 2020/3/28 3:23 PM
@Author: cuberqiu
@File: count_degree.py
@Description: 
"""

# 用字典来表示一边
edge = {
    "actor1": None,
    "actor2": None,
    "num_movies": None
}

node = {
    "id": None,
    "name": None,
    "movies_95_04": None,
    "main_genre": None,
    "genres": None
}

node_xy = {
    "degree": None,
    "node_number": None
}


def init_edge(edge_file_path):

    # 用数组存储所有边
    edge_list = list()

    with open(edge_file_path, 'r') as f:
        # 读取第一行
        line = f.readline()

        while line:
            line = f.readline()
            line = line.strip('\n').strip()

            if line:
                edge_element = line.split('\t')

                edge_list.append({
                    "actor1": edge_element[0],
                    "actor2": edge_element[1],
                    "num_movies": edge_element[2]
                })

    return edge_list


def init_node(node_file_path):

    # 用集合存储所有点
    nodes = dict()

    with open(node_file_path, 'r',  encoding="utf-8") as f:
        line = f.readline()

        while line:
            line = f.readline()
            line = line.strip('\n').strip()

            if line:
                node_element = line.split('\t')
                nodes[node_element[0]] = {
                    "name": node_element[1],
                    "movies_95_04": node_element[2],
                    "main_genre": node_element[3],
                    "genres": node_element[4],
                    "degree": 0
                }

        return nodes


def count_degree(edges, nodes):
    for edge in edges:
        actor1 = edge['actor1']
        actor2 = edge['actor2']

        nodes[actor1]['degree'] = nodes[actor1]['degree'] + 1
        nodes[actor2]['degree'] = nodes[actor2]['degree'] + 1

    return nodes


def sort_node_degree(nodes:dict):
    nodes_degree = list()

    for node_id, value in nodes.items():
        nodes_degree.append({
            "node_id": node_id,
            "degree": value['degree']
        })

    nodes_degree.sort(key=lambda node : node['degree'], reverse=True)

    result = list()

    count = 0

    for node in nodes_degree:
        if count < 20:
            result.append(node)
        else:
            if node['degree'] == result[19]['degree']:
                result.append(node)
        count = count + 1

    return result


def count_degree_numbers(node_degree:dict):
    result = dict()

    for node_id, value in node_degree.items():
        degree = value['degree']
        result[degree] = 0

    for node_id, value in node_degree.items():
        degree = value['degree']
        result[degree] = result[degree] + 1

    return result


if __name__ == "__main__":
    edges = init_edge("./imdb_actor_edges.tsv")
    nodes = init_node("./imdb_actors_key.tsv")

    nodes = count_degree(edges, nodes)

    top_nodes = sort_node_degree(nodes)

    degree_number = count_degree_numbers(nodes)

    for node_degree, number in degree_number.items():
        print("{} : {}".format(node_degree, number))


