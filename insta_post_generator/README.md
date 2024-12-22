# InstaPostGenerator Crew

Welcome to the InstaPostGenerator Crew project, powered by [crewAI](https://crewai.com).
## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. 
Install the requirements.txt

## Important modification required to run the tools properly:
- in crewai>utilities>crew_json_encoder.py

        class CrewJSONEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, BaseModel):
                    return self._handle_pydantic_model(obj)
                elif isinstance(obj, UUID) or isinstance(obj, Decimal):
                    return str(obj)

                elif isinstance(obj, datetime) or isinstance(obj, date):
                    return obj.isoformat()

                #this elif block needs to be added in the original function
                elif  isinstance(obj,set):
                    return str(obj)
                
                return super().default(obj) 

**Add your `OPENAI_API_KEY` and `SERPER_API_KEY` into the `.env` file**

- Modify `src/insta_post_generator/config/agents.yaml` to define your agents
- Modify `src/insta_post_generator/config/tasks.yaml` to define your tasks
- Modify `src/insta_post_generator/crew.py` to add your own logic, tools and specific args
- Modify `src/insta_post_generator/main.py` to add custom inputs for your agents and tasks

## Running the Project

- While in the insta_post_generator directory, to run the flask app, in the terminal run the following command:
    `flask --app src run --debug `


## Support

For support, questions, or feedback regarding the InstaPostGenerator Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
