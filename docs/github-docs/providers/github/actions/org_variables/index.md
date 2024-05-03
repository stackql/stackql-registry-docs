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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>org_variables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.actions.org_variables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the variable. |
| <CopyableCode code="created_at" /> | `string` | The date and time at which the variable was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
| <CopyableCode code="selected_repositories_url" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` | The date and time at which the variable was last updated, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
| <CopyableCode code="value" /> | `string` | The value of the variable. |
| <CopyableCode code="visibility" /> | `string` | Visibility of a variable |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_org_variable" /> | `SELECT` | <CopyableCode code="name, org" /> | Gets a specific variable in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `organization_actions_variables:read` organization permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| <CopyableCode code="list_org_variables" /> | `SELECT` | <CopyableCode code="org" /> | Lists all organization variables.<br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. If the repository is private, you must use an access token with the `repo` scope. GitHub Apps must have the `organization_actions_variables:read` organization permission to use this endpoint. Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| <CopyableCode code="create_org_variable" /> | `INSERT` | <CopyableCode code="org, data__name, data__value, data__visibility" /> | Creates an organization variable that you can reference in a GitHub Actions workflow.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `organization_actions_variables:write` organization permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| <CopyableCode code="delete_org_variable" /> | `DELETE` | <CopyableCode code="name, org" /> | Deletes an organization variable using the variable name.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `organization_actions_variables:write` organization permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| <CopyableCode code="update_org_variable" /> | `EXEC` | <CopyableCode code="name, org" /> | Updates an organization variable that you can reference in a GitHub Actions workflow.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `organization_actions_variables:write` organization permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
