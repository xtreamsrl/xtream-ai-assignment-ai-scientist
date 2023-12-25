# Employee Churn Dataset
The dataset includes factors potentially influencing an individual's intention to leave their job. 

It comprises sociodemographic variables and indicators of each candidate's past behavior. 
The data were collected over a brief period, with each individual representing a single sample in the dataset. 

All variables, except the target, were gathered before the individual joined the company, 
meaning `company_size` and `company_type` refer to the candidate's previous position.

### Features

- enrollee_id: Unique ID for candidate 
- city: City code 
- city_development_index: Development index of the city (scaled)
- gender: Gender of candidate 
- relevant_experience: Relevant experience of candidate 
- enrolled_university: Type of University course enrolled if any 
- education_level: Education level of candidate 
- major_discipline: Education discipline of candidate 
- experience: Candidate total experience in years 
- company_size: Number of employees in current employer's company 
- company_type: Type of current employer 
- last_new_job: Difference in years between previous job and current job 
- training_hours: training hours completed 
- target: 0 – Not looking for job change, 1 – Looking for a job change