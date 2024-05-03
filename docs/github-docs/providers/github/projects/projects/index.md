---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
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
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.projects.projects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="name" /> | `string` | Name of the project |
| <CopyableCode code="body" /> | `string` | Body of the project |
| <CopyableCode code="columns_url" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="creator" /> | `object` | A GitHub user. |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="number" /> | `integer` |  |
| <CopyableCode code="organization_permission" /> | `string` | The baseline permission that all organization members have on this project. Only present if owner is an organization. |
| <CopyableCode code="owner_url" /> | `string` |  |
| <CopyableCode code="private" /> | `boolean` | Whether or not this project can be seen by everyone. Only present if owner is an organization. |
| <CopyableCode code="state" /> | `string` | State of the project; either 'open' or 'closed' |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project_id" /> | Gets a project by its `id`. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| <CopyableCode code="list_for_org" /> | `SELECT` | <CopyableCode code="org" /> | Lists the projects in an organization. Returns a `404 Not Found` status if projects are disabled in the organization. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| <CopyableCode code="list_for_repo" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists the projects in a repository. Returns a `404 Not Found` status if projects are disabled in the repository. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| <CopyableCode code="list_for_user" /> | `SELECT` | <CopyableCode code="username" /> | Lists projects for a user. |
| <CopyableCode code="create_for_authenticated_user" /> | `INSERT` | <CopyableCode code="data__name" /> | Creates a user project board. Returns a `410 Gone` status if the user does not have existing classic projects. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| <CopyableCode code="create_for_org" /> | `INSERT` | <CopyableCode code="org, data__name" /> | Creates an organization project board. Returns a `410 Gone` status if projects are disabled in the organization or if the organization does not have existing classic projects. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| <CopyableCode code="create_for_repo" /> | `INSERT` | <CopyableCode code="owner, repo, data__name" /> | Creates a repository project board. Returns a `410 Gone` status if projects are disabled in the repository or if the repository does not have existing classic projects. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project_id" /> | Deletes a project board. Returns a `404 Not Found` status if projects are disabled. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="project_id" /> | Updates a project board's information. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
