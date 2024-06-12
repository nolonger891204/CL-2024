from ehownet_python3 import *
import json

tree=EHowNetTree("D:\College\Master\data\ehownet\ehownet\db\ehownet_ontology.sqlite")

def build_tree_dict(node_name):
    if not node_name:
        return {}, {}
    
    tree_dict = {}
    node_name_dict = {}
    category = tree.semanticType(node_name)
    hyponym_list = category.getHyponymList()
    node_name_dict[node_name] = category.node_id

    for child_node in hyponym_list:
        child_tree_dict, child_node_name_dict = build_tree_dict(child_node.name)
        tree_dict[child_node.node_id] = child_tree_dict
        node_name_dict.update(child_node_name_dict)
    
    return tree_dict, node_name_dict

tree_dict, node_name_dict = build_tree_dict('TopNode.1')

node_name_dict = {v: k for k, v in node_name_dict.items()}

file_path = "D:\College\Master\data\ehownet\ehownet\WordSense_ForOntology.json"
with open(file_path, "w", encoding="utf-8") as json_file:
    json.dump(tree_dict, json_file, ensure_ascii=False, indent=4)

file_path = "D:\College\Master\data\ehownet\ehownet\WordSense_nodeId.json"
with open(file_path, "w", encoding="utf-8") as json_file:
    json.dump(node_name_dict, json_file, ensure_ascii=False, indent=4)

exit();