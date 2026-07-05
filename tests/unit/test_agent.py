"""COO Copilot Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_monitor_operations():
    """Test Monitor operational efficiency metrics across departments."""
    tools = AgentTools()
    result = await tools.monitor_operations(departments="test", metrics="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_process_improvements():
    """Test Track process improvement initiatives and savings."""
    tools = AgentTools()
    result = await tools.track_process_improvements(program_id="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_analyze_operational_costs():
    """Test Analyze operational costs and identify optimization opportunities."""
    tools = AgentTools()
    result = await tools.analyze_operational_costs(cost_centers="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_manage_cross_functional():
    """Test Manage cross-functional project status and dependencies."""
    tools = AgentTools()
    result = await tools.manage_cross_functional(project_id="test", status_filter="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.coo_copilot_agent_agent import CooCopilotAgentAgent
    agent = CooCopilotAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
