---
title: repositories_environments_variables
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories_environments_variables
  - actions
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repositories_environments_variables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.repositories_environments_variables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the variable. |
| `value` | `string` | The value of the variable. |
| `created_at` | `string` | The date and time at which the variable was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
| `updated_at` | `string` | The date and time at which the variable was last updated, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_environment_variable` | `SELECT` | `environment_name, name, repository_id` | Gets a specific variable in an environment.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `environments:read` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| `list_environment_variables` | `SELECT` | `environment_name, repository_id` | Lists all environment variables.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `environments:read` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| `create_environment_variable` | `INSERT` | `environment_name, repository_id, data__name, data__value` | Create an environment variable that you can reference in a GitHub Actions workflow.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `environment:write` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| `delete_environment_variable` | `DELETE` | `environment_name, name, repository_id` | Deletes an environment variable using the variable name.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `environment:write` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| `update_environment_variable` | `EXEC` | `environment_name, name, repository_id` | Updates an environment variable that you can reference in a GitHub Actions workflow.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `environment:write` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
