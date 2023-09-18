---
title: org_variables
hide_title: false
hide_table_of_contents: false
keywords:
  - org_variables
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
<tr><td><b>Name</b></td><td><code>org_variables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.org_variables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the variable. |
| `created_at` | `string` | The date and time at which the variable was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
| `selected_repositories_url` | `string` |  |
| `updated_at` | `string` | The date and time at which the variable was last updated, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
| `value` | `string` | The value of the variable. |
| `visibility` | `string` | Visibility of a variable |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_org_variable` | `SELECT` | `name, org` | Gets a specific variable in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `organization_actions_variables:read` organization permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| `list_org_variables` | `SELECT` | `org` | Lists all organization variables.<br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. If the repository is private, you must use an access token with the `repo` scope. GitHub Apps must have the `organization_actions_variables:read` organization permission to use this endpoint. Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| `create_org_variable` | `INSERT` | `org, data__name, data__value, data__visibility` | Creates an organization variable that you can reference in a GitHub Actions workflow.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `organization_actions_variables:write` organization permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| `delete_org_variable` | `DELETE` | `name, org` | Deletes an organization variable using the variable name.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `organization_actions_variables:write` organization permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| `update_org_variable` | `EXEC` | `name, org` | Updates an organization variable that you can reference in a GitHub Actions workflow.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `organization_actions_variables:write` organization permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
