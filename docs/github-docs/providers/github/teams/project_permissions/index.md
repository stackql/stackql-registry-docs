---
title: project_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - project_permissions
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
<tr><td><b>Name</b></td><td><code>project_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.project_permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
| `updated_at` | `string` |  |
| `number` | `integer` |  |
| `permissions` | `object` |  |
| `state` | `string` |  |
| `html_url` | `string` |  |
| `creator` | `object` | A GitHub user. |
| `body` | `string` |  |
| `organization_permission` | `string` | The organization permission for this project. Only present when owner is an organization. |
| `owner_url` | `string` |  |
| `url` | `string` |  |
| `columns_url` | `string` |  |
| `private` | `boolean` | Whether the project is private or not. Only present when owner is an organization. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `check_permissions_for_project_in_org` | `SELECT` | `org, project_id, team_slug` | Checks whether a team has `read`, `write`, or `admin` permissions for an organization project. The response includes projects inherited from a parent team.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/projects/&#123;project_id&#125;`. |
| `check_permissions_for_project_legacy` | `SELECT` | `project_id, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a project](https://docs.github.com/rest/teams/teams#check-team-permissions-for-a-project) endpoint.<br /><br />Checks whether a team has `read`, `write`, or `admin` permissions for an organization project. The response includes projects inherited from a parent team. |
| `add_or_update_project_permissions_in_org` | `EXEC` | `org, project_id, team_slug` | Adds an organization project to a team. To add a project to a team or update the team's permission on a project, the authenticated user must have `admin` permissions for the project. The project and team must be part of the same organization.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/projects/&#123;project_id&#125;`. |
| `add_or_update_project_permissions_legacy` | `EXEC` | `project_id, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Add or update team project permissions](https://docs.github.com/rest/teams/teams#add-or-update-team-project-permissions) endpoint.<br /><br />Adds an organization project to a team. To add a project to a team or update the team's permission on a project, the authenticated user must have `admin` permissions for the project. The project and team must be part of the same organization. |
