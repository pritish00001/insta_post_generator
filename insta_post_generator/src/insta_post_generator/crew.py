from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from src.insta_post_generator.tools.search_tools import SearchTools 

from pydantic import BaseModel


class Prompts(BaseModel):
    prompt1: str
    prompt2: str
    prompt3: str

@CrewBase
class InstaPostGenerator():
	"""InstaPostGenerator crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def Info_gathering_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['Info_gathering_agent'],
			verbose=True,
			tools=[SearchTools.search_internet,SearchTools.search_instagram]
		)

	@agent
	def Internet_trend_searcher(self) -> Agent:
		return Agent(
			config=self.agents_config['Internet_trend_searcher'],
			verbose=True,
			tools=[SearchTools.search_internet,SearchTools.search_instagram,SearchTools.search_trends]
		)

	@agent
	def Insta_post_Creator(self) -> Agent:
		return Agent(
			config=self.agents_config['Insta_post_Creator'],
			verbose=True,
			tools=[SearchTools.search_instagram]
		)
	
	@agent
	def Image_prompt_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['Image_prompt_writer'],
			verbose=True
		)

	@task
	def info_gather(self) -> Task:
		return Task(
			config=self.tasks_config['info_gather'],
		)

	@task
	def trend_search(self) -> Task:
		return Task(
			config=self.tasks_config['trend_search'],
		)
	@task
	def instagram_post(self) -> Task:
		return Task(
			config=self.tasks_config['instagram_post'],
		)
	@task
	def instagram_post_prompt(self) -> Task:
		return Task(
			config=self.tasks_config['instagram_post_prompt'],
			output_pydantic=Prompts,
		)
	
	@crew
	def crew(self) -> Crew:
		"""Creates the InstaPostGenerator crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
