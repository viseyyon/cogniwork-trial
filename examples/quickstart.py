"""
CogniWork Quickstart Example
============================

This example demonstrates the core features of CogniWork:
- Creating an Agent
- Adding tools to an Agent
- Running a task
- Using the Orchestrator
- Running parallel tasks

For more examples, visit: https://github.com/viseyyon/cogniwork-trial
"""

import asyncio
from cogniwork import Agent, Orchestrator
from cogniwork.tools import create_shell_tool, create_file_tool


# =============================================================================
# Example 1: Creating a Simple Agent
# =============================================================================

async def simple_agent_example():
      """Create and run a simple agent."""
      print("\n--- Example 1: Simple Agent ---\n")

    # Create an agent with a name and optional model
      agent = Agent(
          name="Assistant",
          model="gpt-4",  # or "claude-3", "ollama/llama2", etc.
      )

    # Run a task
      result = await agent.run("What is the capital of France?")
      print(f"Agent response: {result.output}")

    return result


# =============================================================================
# Example 2: Agent with Tools
# =============================================================================

async def agent_with_tools_example():
      """Create an agent with custom tools."""
      print("\n--- Example 2: Agent with Tools ---\n")

    # Create an agent
      agent = Agent(name="DevAssistant", model="gpt-4")

    # Add tools to the agent
      agent.add_tool(create_shell_tool())  # Execute shell commands
    agent.add_tool(create_file_tool())   # Read/write files

    # Run a task that uses tools
    result = await agent.run("List the files in the current directory")
    print(f"Agent response: {result.output}")

    return result


# =============================================================================
# Example 3: Using the Orchestrator
# =============================================================================

async def orchestrator_example():
      """Use the Orchestrator to manage multiple agents."""
      print("\n--- Example 3: Orchestrator ---\n")

    # Create specialized agents
      coder = Agent(name="CodeWriter", model="gpt-4")
      reviewer = Agent(name="CodeReviewer", model="claude-3")
      tester = Agent(name="TestWriter", model="gpt-4")

    # Create an orchestrator and add agents
      orchestra = Orchestrator()
      orchestra.add_agent(coder)
      orchestra.add_agent(reviewer)
      orchestra.add_agent(tester)

    # Run a single agent task through the orchestrator
      result = await orchestra.run(
          agent="CodeWriter",
          task="Write a Python function to calculate fibonacci numbers"
      )
      print(f"CodeWriter output: {result.output}")

    return result


# =============================================================================
# Example 4: Running Parallel Tasks
# =============================================================================

async def parallel_tasks_example():
      """Run multiple tasks in parallel using the Orchestrator."""
      print("\n--- Example 4: Parallel Tasks ---\n")

    # Create agents
      researcher = Agent(name="Researcher", model="gpt-4")
      analyst = Agent(name="Analyst", model="claude-3")
      writer = Agent(name="Writer", model="gpt-4")

    # Create orchestrator
      orchestra = Orchestrator()
      orchestra.add_agent(researcher)
      orchestra.add_agent(analyst)
      orchestra.add_agent(writer)

    # Define parallel tasks
      tasks = [
          {"agent": "Researcher", "task": "Research best practices for API design"},
          {"agent": "Analyst", "task": "Analyze common API security vulnerabilities"},
          {"agent": "Writer", "task": "Draft an outline for API documentation"},
      ]

    # Run all tasks in parallel
      results = await orchestra.run_parallel(tasks)

    # Print results
      for task, result in zip(tasks, results):
                print(f"\n{task['agent']}: {result.output[:100]}...")

      return results


# =============================================================================
# Main Entry Point
# =============================================================================

async def main():
      """Run all examples."""
      print("=" * 60)
      print("  CogniWork Quickstart Examples")
      print("  https://github.com/viseyyon/cogniwork-trial")
      print("=" * 60)

    # Run examples (uncomment to execute)
      # await simple_agent_example()
    # await agent_with_tools_example()
    # await orchestrator_example()
    # await parallel_tasks_example()

    print("\n--- Quickstart Complete! ---")
    print("Uncomment the example functions above to run them.")
    print("Visit https://docs.cogniwork.ai for full documentation.")


if __name__ == "__main__":
      asyncio.run(main())
