
# Store monitoring project

[![Django CI](https://github.com/madhvi-n/store-monitoring/actions/workflows/django.yml/badge.svg)](https://github.com/madhvi-n/store-monitoring/actions/workflows/django.yml)

A store monitoring project using Django which monitors store status through periodic ingestion of poll data into a database, with the objective of tracking store uptime and downtime on hourly, daily, and weekly basis.


# Requirements
- Backend
    - Python 3.8+
    - virtualenv
    - WSL
    - Redis
    - Celery

# Installation

Clone the repository and enter the root directory
```
git clone https://github.com/madhvi-n/store-monitoring.git
cd store-monitoring
```


Create a virtual environment and activate it
```
virtualenv venv
source venv/bin/activate
```

Making sure your virtual environment is activated, install the dependencies using `pip`
```
pip install -r requirements.txt
```

You can set the secret key for django project in 2 ways
- Edit the `store_monitoring/settings.py` file and add a key manually, some random string.
- Edit the venv file to export `SECRET_KEY`


After installing dependencies, migrate Django apps.(You will find the list of apps when you run the command `python manage.py runserver`)
```
python manage.py migrate
```

Finally start your Django server
```
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` or `localhost:8000` for running web server
Alternatively you can access the admin interface on `http://127.0.0.1:8000/admin/` or `localhost:8000/admin`

Access python shell
```
python manage.py shell
```

### APIs

- `/stores/` returns a list of stores
- `/stores/store_id/trigger_report/` generates report for the store at that instant
- `stores/store_id/reports/report_id/` returns the report instance


### Generating data using management commands

```
python manage.py import_stores_data #add stores to database with their timezones
python manage.py import_business_hours # add business hours for stores in database
python.manage.py import_poll_data # add poll data in database
python.manage.py generate_store_report # can be used to generate store reports
```

### Running celery tasks
- Instead of generating reports directly from api endpoints, it could be more efficient to use Celery to create reports once poll data has been ingested into the database. This can be achieved by chaining tasks in Celery so that report generation only occurs after poll data has been successfully inserted.

- Since poll data is ingested in database hourly, we can set the cache to expire hourly as well

- To optimize user performance and reduce latency, reports can be cached. When the `trigger_report` API is called, the ID of the last generated report can be fetched and returned. Alternatively, cached data can be used to return the most recent report generated for this API.

- Since reports will be generated periodically every hour, a Celery task can be enabled to remove old reports. This will help to keep the system running smoothly and prevent it from becoming cluttered with outdated reports.

#### Celery commands
- `celery -A stores worker -l info -E`

- `celery -A stores beat -l info`

We use Redis broker with Celery so make sure you have redis installed and running
before running celery commands
