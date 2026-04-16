# Subway Navigation Project - TODO List & Framework

## 📂 项目开发框架 (Project Framework)

```text
SubwayNavigation/
├── station.py       # 实体类模块 (数据模型，重度体现OOP特性)
├── subway_map.py    # 数据结构与算法模块 (图结构的构建与Dijkstra算法)
├── main.py          # 系统入口与控制模块 (系统初始化、CLI命令行UI、用户交互)
└── README.md        # 项目说明文件
```

---

## 📝 详细 TODO List 及需要编写的核心内容

### 1. `station.py` (实体/OOP设计)
重点展示 **Object-Oriented Programming (OOP)** 功底，满足课程评分要求。
- [ ] **定义 `Station` 类 (封装 Encapsulation)**
  - 属性：`name` (站名)、`lines` (所属线路)、`is_transfer` (是否为换乘站)。
  - 方法：添加 Getter/Setter，或通过 `@property` 装饰器控制属性访问。
- [ ] **定义一个基类 `Location` 或 `TransportNode` (继承 Inheritance)**
  - 让 `Station` 继承自 `Location`。基类可以有一些通用属性如 `id` 或通用方法如 `get_info()`。
- [ ] **实现多态 (Polymorphism)**
  - 设计一个 `TransferStation` 子类继承自 `Station`，重写（Override）基类的 `get_info()` 方法，输出时特别高亮换乘信息。
- [ ] **定义 `Connection` 或 `Route` 类 (边 Edge)**
  - 属性：`station_a`, `station_b`, `weight` (时间或距离花费)，用于构建图的连通性。

### 2. `subway_map.py` (新数据结构与算法实现)
满足 Task 2 (50%分数) 的硬性要求：图数据结构 + 寻路算法。
- [ ] **实现图数据结构 (Graph - Data Structure)**
  - 创建 `SubwayMap` 类。
  - 使用**邻接表 (Adjacency List)**，在内部用字典维护各个 `Station` 对象及其相连的邻居节点和权重。
  - 方法：`add_station(station)`, `add_connection(station1, station2, weight)`。
- [ ] **实现 Dijkstra's Algorithm (算法)**
  - 在 `SubwayMap` 类中编写 `find_shortest_path(start_name, end_name)` 方法。
  - **算法步骤：**
    1. 初始化所有节点的距离为无穷大（∞），起点距离为0。
    2. 创建一个最小堆 / 优先队列（`import heapq`）来每次获取当前距离最近的未访问节点。
    3. 维护一个 `previous_nodes` 字典来记录路径回溯轨迹。
    4. 遍历邻居，进行**松弛操作 (Relaxation)**：如果 `当前距离 + 边权重 < 邻居记录的距离`，则更新邻居距离并压入优先队列。
    5. 到达终点后，通过 `previous_nodes` 反向推导出完整的途径站点列表。
- [ ] **代码注释强化：**
  - 为 Graph 的 ADT 和 Dijkstra 的核心循环写上极其详细的英文注释（报告里需要贴代码并解释，没注释会被扣分）。

### 3. `main.py` (系统交互与测试)
满足项目的 "解决实际问题 (Real-life problem)" 要求。
- [ ] **数据初始化 (Mock Data)：**
  - 在 `main.py` 启动时，实例化几个 `Station` / `TransferStation`。
  - 用 `subway_map.add_connection()` 建立一个简易但有分叉的地铁网络。
- [ ] **CLI 命令行菜单 (User Interface)：**
  - 用 `while True` 循环实现交互控制台。
  - 选项示例：`1. View Subway Stations` | `2. Find Shortest Route` | `3. Exit`
- [ ] **异常与错误处理 (Error Handling)：**
  - 用户输入不存在的起点或终点时，使用 `try...except` 或 `if` 捕获并友好提示。

### 4. 项目报告与收尾 (The Report & Video - Due Apr 12)
- [ ] **Report - OOP 章节：** 截图说明你哪里用了封装、继承和多态（`station.py`）。
- [ ] **Report - Data Structure 章节：** 阐述 **Graph (图)** 的 ADT 是什么，邻接表的时间/空间优势。
- [ ] **Report - Algorithm 章节：** 分析 Dijkstra 算法的 **时间复杂度**（优先队列实现为 $O((V+E)\log V)$），并画图/写文字解析步骤。
- [ ] **5-min 介绍视频：** 录屏跑一遍 `main.py` 的测试案例，口头讲解一下怎么用到了要求的数据结构和OOP概念。