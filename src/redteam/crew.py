from __future__ import annotations
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Redteam():
    """Redteam crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def osint_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['osint_analyst'], # type: ignore[index]
            verbose=True
        )

    @agent
    def social_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['social_engineer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def malware_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['malware_designer'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def exfiltration_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['exfiltration_planner'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def osint_recon_task(self) -> Task:
        return Task(
            config=self.tasks_config['osint_recon_task'], # type: ignore[index]
        )

    @task
    def target_selection_task(self) -> Task:
        return Task(
            config=self.tasks_config['target_selection_task'], # type: ignore[index]
        )
    
    @task
    def phishing_crafting_task(self) -> Task:
        return Task(
            config=self.tasks_config['phishing_crafting_task'], # type: ignore[index]
        )
    
    @task
    def malware_concept_task(self) -> Task:
        return Task(
            config=self.tasks_config['malware_concept_task'], # type: ignore[index]
        )

    @task
    def data_exfiltration_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_exfiltration_task'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Redteam crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
