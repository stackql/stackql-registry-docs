---
title: legacy_projects
hide_title: false
hide_table_of_contents: false
keywords:
  - legacy_projects
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>legacy_projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.legacy_projects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `html_url` | `string` |  |
| `created_at` | `string` |  |
| `state` | `string` |  |
| `organization_permission` | `string` | The organization permission for this project. Only present when owner is an organization. |
| `creator` | `object` | Simple User |
| `url` | `string` |  |
| `number` | `integer` |  |
| `permissions` | `object` |  |
| `node_id` | `string` |  |
| `body` | `string` |  |
| `owner_url` | `string` |  |
| `columns_url` | `string` |  |
| `updated_at` | `string` |  |
| `private` | `boolean` | Whether the project is private or not. Only present when owner is an organization. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_projects_legacy` | `SELECT` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List team projects`](https://docs.github.com/rest/reference/teams#list-team-projects) endpoint.<br /><br />Lists the organization projects for a team. |
| `remove_project_legacy` | `DELETE` | `project_id, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a project from a team](https://docs.github.com/rest/reference/teams#remove-a-project-from-a-team) endpoint.<br /><br />Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have `read` access to both the team and project, or `admin` access to the team or project. **Note:** This endpoint removes the project from the team, but does not delete it. |
| `add_or_update_project_permissions_legacy` | `EXEC` | `project_id, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Add or update team project permissions](https://docs.github.com/rest/reference/teams#add-or-update-team-project-permissions) endpoint.<br /><br />Adds an organization project to a team. To add a project to a team or update the team's permission on a project, the authenticated user must have `admin` permissions for the project. The project and team must be part of the same organization. |
| `check_permissions_for_project_legacy` | `EXEC` | `project_id, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a project](https://docs.github.com/rest/reference/teams#check-team-permissions-for-a-project) endpoint.<br /><br />Checks whether a team has `read`, `write`, or `admin` permissions for an organization project. The response includes projects inherited from a parent team. |
