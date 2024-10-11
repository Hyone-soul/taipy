

## ⭐️ 什么是 Taipy?

Taipy 是专为数据科学家和机器学习工程师设计的，用于构建数据与 AI Web 应用程序的工具。<br />

⭐️ 使构建生产就绪的 Web 应用程序成为可能。<br />
⭐️ 无需学习新的语言，仅需 Python。<br />
⭐️ 专注于数据和 AI 算法，而不用担心开发和部署的复杂性。<br />

&nbsp;

<h4 align="left">
Taipy 是一个集 UI 生成和场景/数据管理于一体的工具
</h4>

<br />

| 用户界面生成 | 场景和数据管理 |
| ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| <img src="readme_img/taipy_github_GUI_video.gif" alt="界面动画"  width="100%" /> | <img src="readme_img/taipy_github_scenarios_video.gif" alt="后台动画"  width="100%"/> |

&nbsp;

## ✨ 关键功能

<img src="readme_img/taipy_github_scenario.png" alt="场景横幅"  width="49%" />  <img src="readme_img/taipy-github-optimized.png" alt="后台动画"  width="49.7%"/>
<img src="readme_img/taipy_github_data_support.png" alt="后台动画"  width="49.7%" />

&nbsp;

## ⚙️ 快速开始

安装 Taipy 稳定版请运行：

```bash
pip install taipy
```

准备好安装 Taipy 了吗？🚀<br>
很快就能设置好！无论你是使用 Conda 环境，还是从源码安装，请按照我们的[安装指南](https://docs.taipy.io/en/latest/installation/)获取逐步指导。<br/>

期待马上使用？💡<br>
从今天开始用 Taipy 构建吧！我们的[快速入门指南](https://docs.taipy.io/en/latest/tutorials/getting_started/)是你开始 Taipy 之旅的理想起点，充分挖掘 Taipy 的潜力。

&nbsp;

## 🔌 场景和数据管理

让我们在 Taipy 中创建一个场景，允许你根据选择的电影类型过滤数据。<br />
该场景设计为一个简单的管道。<br />
每次更改电影类型选择时，场景都会运行以处理你的请求。<br />
然后，它会显示该类型中最受欢迎的前七部电影。

<br />

> ⚠️ 请注意，在这个示例中，我们使用了一个非常简单的仅包含一个任务的管道。然而，<br />
> Taipy 能够处理更复杂的管道 🚀

<br />

以下是我们的过滤函数。这是一个典型的 Python 函数，也是该场景中使用的唯一任务。

```python
def filter_genre(initial_dataset: pd.DataFrame, selected_genre):
    filtered_dataset = initial_dataset[initial_dataset['genres'].str.contains(selected_genre)]
    filtered_data = filtered_dataset.nlargest(7, 'Popularity %')
    return filtered_data
```

这是我们正在实现的场景的执行图

<p align="center">
<img src="https://github.com/Avaiga/taipy/raw/develop/readme_img/readme_exec_graph.png" width="600" align="center" />
</p>

### Taipy Studio

你可以在 Visual Studio Code 中使用 Taipy Studio 扩展来无代码配置场景。<br />
你的配置会自动保存为 TOML 文件。<br />
查看 Taipy Studio [文档](https://docs.taipy.io/en/latest/manuals/studio/)

对于更高级的用例，或如果你更喜欢通过编码而非使用 Taipy Studio 来配置场景，<br />
请查看这个[演示](https://docs.taipy.io/en/latest/gallery/other/movie_genre_selector/)的电影类型筛选场景创建。

![TaipyStudio](https://github.com/Avaiga/taipy/raw/develop/readme_img/readme_demo_studio.gif)

&nbsp;

## 用户界面生成和场景 & 数据管理

这个简单的 Taipy 应用程序演示了如何使用 Taipy 创建一个基本的电影推荐系统。<br />
应用程序根据用户选择的电影类型过滤电影数据集，并显示该类型中最受欢迎的前七部电影。
以下是该应用程序的前端和后端代码的完整实现。

```python
import taipy as tp
import pandas as pd
from taipy import Config, Scope, Gui

# 定义辅助函数

# 回调定义 - 提交场景与类型选择
def on_genre_selected(state):
    scenario.selected_genre_node.write(state.selected_genre)
    tp.submit(scenario)
    state.df = scenario.filtered_data.read()

## 设置初始值为 Action
def on_init(state):
    on_genre_selected(state)

# 过滤函数 - 任务
def filter_genre(initial_dataset: pd.DataFrame, selected_genre):
    filtered_dataset = initial_dataset[initial_dataset["genres"].str.contains(selected_genre)]
    filtered_data = filtered_dataset.nlargest(7, "Popularity %")
    return filtered_data

# 主脚本
if __name__ == "__main__":
    # Taipy 场景 & 数据管理

    # 加载通过 Taipy Studio 创建的配置
    Config.load("config.toml")
    scenario_cfg = Config.scenarios["scenario"]

    # 启动 Taipy 协调器
    tp.Orchestrator().run()

    # 创建一个场景
    scenario = tp.create_scenario(scenario_cfg)

    # Taipy 用户界面
    # 让我们为场景管理添加一个 GUI，形成一个完整的应用程序

    # 获取类型列表
    genres = [
        "Action", "Adventure", "Animation", "Children", "Comedy", "Fantasy", "IMAX"
        "Romance", "Sci-FI", "Western", "Crime", "Mystery", "Drama", "Horror", "Thriller", "Film-Noir", "War", "Musical", "Documentary"
    ]

    # 初始化变量
    df = pd.DataFrame(columns=["Title", "Popularity %"])
    selected_genre = "Action"

    # 用户界面定义
    my_page = """
# 电影推荐

## 选择你喜欢的电影类型
<|{selected_genre}|selector|lov={genres}|on_change=on_genre_selected|dropdown|>

## 以下是最受欢迎的前七部电影
<|{df}|chart|x=Title|y=Popularity %|type=bar|title=电影受欢迎度|>
    """

    Gui(page=my_page).run()
```

最终结果如下：
<img src="readme_img/readme_app.gif" />

