# generate-weighted-graph

## Description
This script use to generate weighted graph from OpenStreetMap data

## output
### There are 3 kinds of output:
```
1. images/images.png: image of graph with highlight source and destination
2. nodes_origin.csv: list of nodes in graph generated from OpenStreetMap.
   edges_origin.csv: list of edges in graph generated from OpenStreetMap.
3. nodes_processed.csv: list of nodes in graph and it degrees (street_count).
   edges_processed.csv: list of edges in graph and it weight (length).
```

## Usage
### Prerequisites
#### install required packages
```bash
pip3 install -r requirements.txt
```

#### include area of map you want to generate graph in areas_list.txt
```yaml
---
areas:
  - "Quận 10"
  - "Quận 3"
  - "Quận 1"
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

