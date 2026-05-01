
from app.agents.trend_agent import TrendAgent
from app.agents.audience_agent import AudienceAgent
from app.agents.strategy_agent import StrategyAgent
from app.agents.creative_agent import CreativeAgent
from app.agents.review_agent import ReviewAgent

def execute_workflow(topic):
    trend = TrendAgent().run(topic)
    audience = AudienceAgent().run(trend)
    strategy = StrategyAgent().run(audience)
    creative = CreativeAgent().run(strategy)
    review = ReviewAgent().run(creative)

    return {
        "trend": trend,
        "audience": audience,
        "strategy": strategy,
        "creative": creative,
        "review": review
    }
