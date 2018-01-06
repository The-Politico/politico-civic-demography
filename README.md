![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# django-politico-civic-demography

Gather U.S. Census data for elections, the POLITICO way.

### Quickstart

1. Install the app.

  ```
  $ pip install django-politico-civic-demography
  ```

2. Add the app to your Django project and configure settings.

  ```python
  INSTALLED_APPS = [
      # ...
      'rest_framework',
      'geography',
      'demography',
  ]

  #########################
  # demography settings

  CENSUS_API_KEY = ''
  DEMOGRAPHY_AWS_ACCESS_KEY_ID = ''
  DEMOGRAPHY_AWS_SECRET_ACCESS_KEY = ''
  DEMOGRAPHY_AWS_S3_BUCKET = ''
  DEMOGRAPHY_AWS_REGION = 'us-east-1' # default
  DEMOGRAPHY_AWS_S3_UPLOAD_ROOT = 'elections' # default
  DEMOGRAPHY_AWS_ACL = 'public-read' # default
  DEMOGRAPHY_AWS_CACHE_HEADER = 'max-age=31536000' # default
  DEMOGRAPHY_API_AUTHENTICATION_CLASS = 'rest_framework.authentication.BasicAuthentication' # default
  DEMOGRAPHY_API_PERMISSION_CLASS = 'rest_framework.permissions.IsAdminUser' # default
  DEMOGRAPHY_API_PAGINATION_CLASS = 'demography.pagination.ResultsPagination' # default
  ```

### Developing

##### Running a development server

Move into the example directory, install dependencies and run the development server with pipenv.

  ```
  $ cd example
  $ pipenv install
  $ pipenv run python manage.py runserver
  ```

##### Setting up a PostgreSQL database

1. Run the make command to setup a fresh database.

  ```
  $ make database
  ```

2. Add a connection URL to `example/.env`.

  ```
  DATABASE_URL="postgres://localhost:5432/geography"
  ```

3. Run migrations from the example app.

  ```
  $ cd example
  $ pipenv run python manage.py migrate
  ```
