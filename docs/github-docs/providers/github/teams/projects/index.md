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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.projects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `columns_url` | `string` |  |
| `created_at` | `string` |  |
| `body` | `string` |  |
| `private` | `boolean` | Whether the project is private or not. Only present when owner is an organization. |
| `node_id` | `string` |  |
| `creator` | `object` | Simple User |
| `owner_url` | `string` |  |
| `html_url` | `string` |  |
| `permissions` | `object` |  |
| `state` | `string` |  |
| `url` | `string` |  |
| `updated_at` | `string` |  |
| `number` | `integer` |  |
| `organization_permission` | `string` | The organization permission for this project. Only present when owner is an organization. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_projects_in_org` | `SELECT` | `org, team_slug` | Lists the organization projects for a team.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/projects`. |
| `add_or_update_project_permissions_in_org` | `INSERT` | `org, project_id, team_slug` | Adds an organization project to a team. To add a project to a team or update the team's permission on a project, the authenticated user must have `admin` permissions for the project. The project and team must be part of the same organization.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/projects/&#123;project_id&#125;`. |
| `remove_project_in_org` | `DELETE` | `org, project_id, team_slug` | Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have `read` access to both the team and project, or `admin` access to the team or project. This endpoint removes the project from the team, but does not delete the project.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/projects/&#123;project_id&#125;`. |
| `check_permissions_for_project_in_org` | `EXEC` | `org, project_id, team_slug` | Checks whether a team has `read`, `write`, or `admin` permissions for an organization project. The response includes projects inherited from a parent team.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/projects/&#123;project_id&#125;`. |
