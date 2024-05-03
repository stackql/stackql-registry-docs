---
title: collaborators
hide_title: false
hide_table_of_contents: false
keywords:
  - collaborators
  - projects
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
<tr><td><b>Name</b></td><td><code>collaborators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.projects.collaborators" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="permission" /> | `string` |  |
| <CopyableCode code="user" /> | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_permission_for_user" /> | `SELECT` | <CopyableCode code="project_id, username" /> | Returns the collaborator's permission level for an organization project. Possible values for the `permission` key: `admin`, `write`, `read`, `none`. You must be an organization owner or a project `admin` to review a user's permission level. |
| <CopyableCode code="list_collaborators" /> | `SELECT` | <CopyableCode code="project_id" /> | Lists the collaborators for an organization project. For a project, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners. You must be an organization owner or a project `admin` to list collaborators. |
| <CopyableCode code="remove_collaborator" /> | `DELETE` | <CopyableCode code="project_id, username" /> | Removes a collaborator from an organization project. You must be an organization owner or a project `admin` to remove a collaborator. |
| <CopyableCode code="add_collaborator" /> | `EXEC` | <CopyableCode code="project_id, username" /> | Adds a collaborator to an organization project and sets their permission level. You must be an organization owner or a project `admin` to add a collaborator. |
