---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - teams
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
<tr><td><b>Id</b></td><td><CopyableCode code="github.teams.projects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="body" /> | `string` |  |
| <CopyableCode code="columns_url" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="creator" /> | `object` | A GitHub user. |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="number" /> | `integer` |  |
| <CopyableCode code="organization_permission" /> | `string` | The organization permission for this project. Only present when owner is an organization. |
| <CopyableCode code="owner_url" /> | `string` |  |
| <CopyableCode code="permissions" /> | `object` |  |
| <CopyableCode code="private" /> | `boolean` | Whether the project is private or not. Only present when owner is an organization. |
| <CopyableCode code="state" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_projects_in_org" /> | `SELECT` | <CopyableCode code="org, team_slug" /> | Lists the organization projects for a team.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/projects`. |
| <CopyableCode code="list_projects_legacy" /> | `SELECT` | <CopyableCode code="team_id" /> | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List team projects`](https://docs.github.com/rest/teams/teams#list-team-projects) endpoint.<br /><br />Lists the organization projects for a team. |
| <CopyableCode code="remove_project_in_org" /> | `DELETE` | <CopyableCode code="org, project_id, team_slug" /> | Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have `read` access to both the team and project, or `admin` access to the team or project. This endpoint removes the project from the team, but does not delete the project.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/projects/&#123;project_id&#125;`. |
| <CopyableCode code="remove_project_legacy" /> | `EXEC` | <CopyableCode code="project_id, team_id" /> | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a project from a team](https://docs.github.com/rest/teams/teams#remove-a-project-from-a-team) endpoint.<br /><br />Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have `read` access to both the team and project, or `admin` access to the team or project. **Note:** This endpoint removes the project from the team, but does not delete it. |
