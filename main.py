from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI(title="项目组介绍网站")

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 设置模板
templates = Jinja2Templates(directory="templates")

# 项目数据
project_data = {
    "project_name": "人机共智的认知对齐与协调演化机制研究",
    "project_description": {
        "background": "生成式AI与教育智能体快速进入学习场景，学习正从“人独自完成”转向“人机共智协作”，亟需同时关注其对认知过程的促进作用与潜在风险。",
        "direction": "面向人机共智教育，我们聚焦构建“可解释、可信赖、可协同”的智能学习体系，系统揭示人机协作的认知与行为规律，并形成可迁移的教学交互设计与评测方法，支撑高质量学习与负责任的教育智能应用。",
        "content": "研究内容包括：1) （尤阳研究方向）；2) （顾晨宇研究方向）；3) （汪彩云研究方向）；4) AI谄媚和多智能体冲突消融。"
    },
    "team": {
        "leader": {
            "name": "甄园宜",
            "title": "助理教授、博士生导师",
            "email": "zhenyuanyi@bza.edu.cn",
            "research_interests": "科学学与创新，人工智能教育应用，社会计算",
            "achievements": "参与国家自然科学基金、北京学而思教育科技有限公司基金等课题5项，在SCI/SSCI/CSSCI/EI等检索刊物发表论文10余篇，获2024年国际社会计算会议最具创新奖。"
        },
        "members": [
            {
                "name": "尤阳",
                "role": "博士研究生",
                "specialization": "（待补充）"
            },
            {
                "name": "顾晨宇",
                "role": "博士研究生",
                "specialization": "（待补充）"
            },
            {
                "name": "汪彩云",
                "role": "博士研究生",
                "specialization": "（待补充）"
            },
            {
                "name": "胡晓林",
                "role": "博士研究生",
                "specialization": "研究方向聚焦于多模态大模型与数字人，致力于让数字人“听得懂、说得像、做得自然”，结合多模态理解驱动语义一致的表情与动作表达，关注多模态、具身智能、动作生成等前沿方向。此前在三维重建方向有一定积累。"
            },
           
        ],
        "team_culture": "我们是一支充满活力、勇于创新的研究团队，始终面向学术前沿与真实需求，致力于培养具有国际视野与扎实科研能力的高水平研究人才。团队氛围开放包容、协作紧密，既重视严谨求证的学术训练，也鼓励大胆探索与跨领域交流。我们相信，有温度的团队文化能让每一次讨论更坦诚、每一次并肩更坚定，也让每个人在成长路上被看见、被支持。"
    },
    "news_and_achievements": [
        {
            "date": "2026-01",
            "type": "论文发表",
            "title": "团队论文被人工智能顶级会议NeurIPS 2026接收",
            "description": "关于多模态学习的最新研究成果"
        },
        {
            "date": "2025-12",
            "type": "项目立项",
            "title": "获批国家自然科学基金重点项目",
            "description": "项目资助金额300万元"
        },
        {
            "date": "2025-11",
            "type": "获奖",
            "title": "获得省级科技进步一等奖",
            "description": "智能数据分析系统获得省级科技进步一等奖"
        },
        {
            "date": "2025-10",
            "type": "专利授权",
            "title": "获得发明专利授权3项",
            "description": "涉及数据处理、模型优化等领域"
        },
        {
            "date": "2025-09",
            "type": "学术交流",
            "title": "团队成员在国际会议作主题报告",
            "description": "在ICML 2025大会上作Oral报告"
        }
    ],
    "recruitment": {
        "is_open": True,
        "positions": [
            {
                "title": "博士研究生",
                "requirements": [
                    "具有计算机、数学、社会学、教育学等相关专业背景",
                    "有较强的编程能力（Python/C++）",
                    "对人工智能、大模型、人机交互、AI教育有浓厚兴趣",
                    "有良好的英文阅读和写作能力"
                ],
                "count": "1-2名"
            },
           
            {
                "title": "科研助理",
                "requirements": [
                    "本科及以上学历",
                    "有机器学习或数据分析经验",
                    "能够独立完成研究任务",
                    "有相关项目经验者优先"
                ],
                "count": "1-2名"
            }
        ],
        "contact": {
            "email": "zhenyuanyi@bza.edu.cn",
            "phone": "010-82821011",
            "telephone": "010-82821011",
            "address": "北京市海淀区西北旺镇大牛坊海淀大悦信息科技园",
            "note": "欢迎发送简历至招生邮箱，我们会尽快与您联系！"
        }
    }
}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """首页路由"""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "data": project_data
        }
    )


@app.get("/api/project-info")
async def get_project_info():
    """API接口：获取项目信息"""
    return project_data


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
