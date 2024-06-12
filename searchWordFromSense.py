from ehownet_python3 import *
import json

tree=EHowNetTree("D:\College\Master\data\ehownet\ehownet\db\ehownet_ontology.sqlite")

# list=tree.searchWord(u"北方")
# node=tree.word(list[0].name)
# categoryList=node.getSemanticTypeList()
# category=categoryList[0]
# descendantWordList = category.getDescendantWordList()
# ancestorList=category.getAncestorList()
# print(descendantWordList) # 和word sense of "北"相關的所有字
# print(ancestorList)

# LocationalValue|空間值.1
# {在}.1
category=tree.semanticType('LocationalValue|空間值.1')
hyponymList = category.getHyponymList()
result_dict = {}
for hyponym in hyponymList:
    semanticType = hyponym.name
    category_l2 = tree.semanticType(semanticType)
    hyponymList_l2 = category_l2.getHyponymList()
    temp_list = []
    result_dict[category_l2.name] = {}
    for hyponym_l2 in hyponymList_l2:
        semanticType = hyponym_l2.name
        category_l3 = tree.semanticType(semanticType)
        descendantWordList = category_l3.getDescendantWordList()
        # print(descendantWordList, "\n")
        result_dict[category_l2.name][category_l3.name] = [ { descendantWord.word: tree.word(descendantWord.name).ehownet } for descendantWord in descendantWordList  ]
# print(hyponymList)
# print(result_dict)
# File path to save JSON data
file_path = "D:\College\Master\data\ehownet\ehownet\LocationalValueWord.json"

# Writing dictionary to JSON file
with open(file_path, "w", encoding="utf-8") as json_file:
    json.dump(result_dict, json_file, ensure_ascii=False, indent=4)
# get word
# descendantWordList = category.getDescendantWordList()
# print(len(descendantWordList))
# print(descendantWordList)

exit();