---
title: variables
hide_title: false
hide_table_of_contents: false
keywords:
  - variables
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>variables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.actions.variables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the variable. |
| <CopyableCode code="created_at" /> | `string` | The date and time at which the variable was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
| <CopyableCode code="updated_at" /> | `string` | The date and time at which the variable was last updated, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
| <CopyableCode code="value" /> | `string` | The value of the variable. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_environment_variable" /> | `SELECT` | <CopyableCode code="environment_name, name, repository_id" /> | Gets a specific variable in an environment.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `environments:read` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| <CopyableCode code="get_repo_variable" /> | `SELECT` | <CopyableCode code="name, owner, repo" /> | Gets a specific variable in a repository.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions_variables:read` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| <CopyableCode code="list_environment_variables" /> | `SELECT` | <CopyableCode code="environment_name, repository_id" /> | Lists all environment variables.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `environments:read` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| <CopyableCode code="list_repo_variables" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists all repository variables.<br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions_variables:read` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| <CopyableCode code="create_environment_variable" /> | `INSERT` | <CopyableCode code="environment_name, repository_id, data__name, data__value" /> | Create an environment variable that you can reference in a GitHub Actions workflow.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `environment:write` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| <CopyableCode code="create_repo_variable" /> | `INSERT` | <CopyableCode code="owner, repo, data__name, data__value" /> | Creates a repository variable that you can reference in a GitHub Actions workflow.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions_variables:write` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| <CopyableCode code="delete_environment_variable" /> | `DELETE` | <CopyableCode code="environment_name, name, repository_id" /> | Deletes an environment variable using the variable name.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `environment:write` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| <CopyableCode code="delete_repo_variable" /> | `DELETE` | <CopyableCode code="name, owner, repo" /> | Deletes a repository variable using the variable name.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions_variables:write` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| <CopyableCode code="update_environment_variable" /> | `EXEC` | <CopyableCode code="environment_name, name, repository_id" /> | Updates an environment variable that you can reference in a GitHub Actions workflow.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `environment:write` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| <CopyableCode code="update_repo_variable" /> | `EXEC` | <CopyableCode code="name, owner, repo" /> | Updates a repository variable that you can reference in a GitHub Actions workflow.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions_variables:write` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
