## Basic Information
```
Three Invenio modules ara available to manage the Invenio users, groups and permissions
```

## 1. Invenio-Accounts
```
Invenio user management and authentication
```
### Installation
```python
pip install -e git+https://github.com/inveniosoftware/invenio-accounts.git#egg=invenio-accounts
```

### Examples
```python
create a new user: 
  invenio users create  -a software@rero.ch --password rero21
deactivate a user
  invenio users deactivate software@rero.ch
activate a user
  invenio users activate software@rero.ch

```

## 2. Invenio-Access
```
Invenio authentication and authorization system 
```
### Installation
```python
pip install -e git+https://github.com/inveniosoftware/invenio-access.git#egg=invenio-access
```

### Examples
#### Roles

```python
create a new role: 
  invenio roles create -d "description" role_name
remove a role: 
  invenio roles remove -d role_name
add user to role: 
  invenio roles add user_name role_name

```
#### Actions

```python
list of created actions: 
  invenio access list
list all assigned actions to a user: 
  invenio access show -e user_name
list all assigned actions to a role: 
  invenio access show -r role_name
grant/allow action to a role or a user: 
  invenio access allow action_name role role_name
  invenio access allow action_name user user_name
revoke/deny action from a role or a user: 
  invenio access deny action_name role role_name
  invenio access deny action_name user user_name
Remove existing action authorization !!!
```

## 3. Invenio-Admin
```
Administration interface for Invenio applications 
```
### Installation
```python
pip install -e git+https://github.com/inveniosoftware/invenio-admin.git#egg=invenio-admin
```

### Invenio Configuration and URL
```python
Config: 
Must disable parameter APP_ENABLE_SECURE_HEADERS in 
reroils-app/reroils_app/config.py

URL: localhost:5000/admin
```

