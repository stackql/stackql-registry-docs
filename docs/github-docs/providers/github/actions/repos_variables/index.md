---
title: repos_variables
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_variables
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
<tr><td><b>Name</b></td><td><code>repos_variables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.repos_variables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the variable. |
| `created_at` | `string` | The date and time at which the variable was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
| `updated_at` | `string` | The date and time at which the variable was last updated, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
| `value` | `string` | The value of the variable. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_repo_variable` | `SELECT` | `name, owner, repo` | Gets a specific variable in a repository.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions_variables:read` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| `list_repo_variables` | `SELECT` | `owner, repo` | Lists all repository variables.<br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions_variables:read` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| `create_repo_variable` | `INSERT` | `owner, repo, data__name, data__value` | Creates a repository variable that you can reference in a GitHub Actions workflow.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions_variables:write` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| `delete_repo_variable` | `DELETE` | `name, owner, repo` | Deletes a repository variable using the variable name.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions_variables:write` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| `update_repo_variable` | `EXEC` | `name, owner, repo` | Updates a repository variable that you can reference in a GitHub Actions workflow.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions_variables:write` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
