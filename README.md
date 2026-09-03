# 项目组介绍网站

基于 FastAPI 框架构建的项目组介绍网站，包含项目信息、团队介绍、动态成果和招生信息等完整功能。

## 功能特点

✨ **完整的项目展示系统**
- 📋 项目名称与详细介绍
- 👥 项目负责人与团队成员展示
- 🏆 项目动态与成果时间线
- 📢 招生信息与联系方式

✨ **现代化设计**
- 响应式布局，支持各种设备
- 优雅的动画效果
- 专业的视觉设计
- 平滑滚动与导航高亮

✨ **技术栈**
- **后端**: FastAPI
- **模板引擎**: Jinja2
- **前端**: HTML5 + CSS3 + JavaScript
- **服务器**: Uvicorn

## 项目结构

```
cv/
├── main.py                 # FastAPI 主应用
├── requirements.txt        # Python 依赖
├── README.md              # 项目说明
├── templates/             # HTML 模板
│   └── index.html
└── static/                # 静态资源
    ├── css/
    │   └── style.css      # 样式文件
    └── js/
        └── script.js      # JavaScript 脚本
```

## 快速开始

### GitHub Pages（推荐发布方式）

该站点在 GitHub Pages 采用纯静态部署，发布入口为：

1. 仓库根目录下的 `index.html`
2. 静态资源位于 `static/`（`static/css/style.css`、`static/js/script.js`）

部署到 GitHub Pages 时，不需要运行 FastAPI，打开仓库 Pages URL 即可查看。

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行项目

```bash
python main.py
```

或者使用 uvicorn 命令：

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. 访问网站

在浏览器中打开：
```
http://localhost:8000
```

## API 接口

项目还提供了 RESTful API 接口：

- **GET /** - 网站首页
- **GET /api/project-info** - 获取项目信息（JSON 格式）

访问 API 文档：
```
http://localhost:8000/docs
```

## 自定义内容

### 修改项目数据

编辑 `main.py` 文件中的 `project_data` 字典，修改以下内容：

1. **项目信息**
   - `project_name`: 项目名称
   - `project_description`: 项目背景、方向、内容

2. **团队信息**
   - `team.leader`: 项目负责人信息
   - `team.members`: 团队成员列表
   - `team.team_culture`: 团队风采描述

3. **动态成果**
   - `news_and_achievements`: 添加或修改新闻和成果列表

4. **招生信息**
   - `recruitment.is_open`: 是否开放招募
   - `recruitment.positions`: 招募岗位和要求
   - `recruitment.contact`: 联系方式

### 修改样式

编辑 `static/css/style.css` 文件，可以自定义：
- 颜色主题（修改 `:root` 中的 CSS 变量）
- 字体样式
- 布局间距
- 动画效果

### 添加功能

在 `static/js/script.js` 中可以添加更多交互功能。

## 部署建议

### 使用 Gunicorn + Uvicorn（生产环境）

```bash
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### 使用 Docker

创建 `Dockerfile`：

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

构建并运行：

```bash
docker build -t project-website .
docker run -p 8000:8000 project-website
```

## 浏览器兼容性

- ✅ Chrome (推荐)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ⚠️ IE11 及以下版本不支持

## 许可证

本项目仅供学习和研究使用。

## 技术支持

如有问题，请根据项目中的联系方式获取支持。

---

**Powered by FastAPI** 🚀
