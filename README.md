# generate-weighted-graph

## Description
This script use to generate weighted graph from OpenStreetMap data

## output
### There are 4 kinds of output:
```
1. images/images.png: image of graph with highlight source and destination
2. nodes_origin.csv: list of nodes in graph generated from OpenStreetMap.
   edges_origin.csv: list of edges in graph generated from OpenStreetMap.
3. adj_list.json: adjacency list as json format.
4. graph.graphml: graphml format of graph for later plotting.
```

## Usage
### Prerequisites
#### install required packages
```bash
pip3 install -r requirements.txt
```

##### include area of map you want to generate graph in areas_list.txt
```yaml
---
areas:
  - "Quận 10"
  - "Quận 3"
  - "Quận 1"
```
#### or you can use bbox to specify the area which more accurate than above method, if you specify both, bbox will be used. bbox is in format of [north, south, east, west]
```yaml
bbox: [10.7880, 10.7591, 106.7048, 106.6556]
```

#### include source and destination for highlight in areas_list.txt (optional, still manually find the node id)
```yaml
src_node: 2302073725 # Đai học Bách Khoa
dest_node: 11221021745 # Chợ Bến Thành
```

#### run script
```bash
python3 osmnx2graph.py
```

