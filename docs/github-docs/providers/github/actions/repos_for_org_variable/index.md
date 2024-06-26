---
title: repos_for_org_variable
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_for_org_variable
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
<tr><td><b>Name</b></td><td><code>repos_for_org_variable</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.actions.repos_for_org_variable" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="repositories" /> | `array` |
| <CopyableCode code="total_count" /> | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_selected_repos_for_org_variable" /> | `SELECT` | <CopyableCode code="name, org" /> | Lists all repositories that can access an organization variable<br />that is available to selected repositories.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `organization_actions_variables:read` organization permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| <CopyableCode code="remove_selected_repo_from_org_variable" /> | `DELETE` | <CopyableCode code="name, org, repository_id" /> | Removes a repository from an organization variable that is<br />available to selected repositories. Organization variables that are available to<br />selected repositories have their `visibility` field set to `selected`.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `organization_actions_variables:write` organization permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| <CopyableCode code="add_selected_repo_to_org_variable" /> | `EXEC` | <CopyableCode code="name, org, repository_id" /> | Adds a repository to an organization variable that is available to selected repositories.<br />Organization variables that are available to selected repositories have their `visibility` field set to `selected`.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `organization_actions_variables:write` organization permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
| <CopyableCode code="set_selected_repos_for_org_variable" /> | `EXEC` | <CopyableCode code="name, org, data__selected_repository_ids" /> | Replaces all repositories for an organization variable that is available<br />to selected repositories. Organization variables that are available to selected<br />repositories have their `visibility` field set to `selected`.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `organization_actions_variables:write` organization permission to use this<br />endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read variables. |
