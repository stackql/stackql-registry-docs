---
title: teams
hide_title: false
hide_table_of_contents: false
keywords:
  - teams
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
<tr><td><b>Name</b></td><td><code>teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.teams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `repositories_url` | `string` |  |
| `permissions` | `object` |  |
| `html_url` | `string` |  |
| `privacy` | `string` |  |
| `notification_setting` | `string` |  |
| `permission` | `string` |  |
| `node_id` | `string` |  |
| `members_url` | `string` |  |
| `slug` | `string` |  |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `org` | Lists all teams in an organization that are visible to the authenticated user. |
| `list_child_in_org` | `SELECT` | `org, team_slug` | Lists the child teams of the team specified by `&#123;team_slug&#125;`.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/teams`. |
| `list_child_legacy` | `SELECT` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List child teams`](https://docs.github.com/rest/teams/teams#list-child-teams) endpoint. |
| `create` | `INSERT` | `org, data__name` | To create a team, the authenticated user must be a member or owner of `&#123;org&#125;`. By default, organization members can create teams. Organization owners can limit team creation to organization owners. For more information, see "[Setting team creation permissions](https://docs.github.com/articles/setting-team-creation-permissions-in-your-organization)."<br /><br />When you create a new team, you automatically become a team maintainer without explicitly adding yourself to the optional array of `maintainers`. For more information, see "[About teams](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/about-teams)". |
| `delete_in_org` | `DELETE` | `org, team_slug` | To delete a team, the authenticated user must be an organization owner or team maintainer.<br /><br />If you are an organization owner, deleting a parent team will delete all of its child teams as well.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;`. |
| `delete_legacy` | `EXEC` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Delete a team](https://docs.github.com/rest/teams/teams#delete-a-team) endpoint.<br /><br />To delete a team, the authenticated user must be an organization owner or team maintainer.<br /><br />If you are an organization owner, deleting a parent team will delete all of its child teams as well. |
| `get_legacy` | `EXEC` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the [Get a team by name](https://docs.github.com/rest/teams/teams#get-a-team-by-name) endpoint. |
| `update_in_org` | `EXEC` | `org, team_slug` | To edit a team, the authenticated user must either be an organization owner or a team maintainer.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;`. |
| `update_legacy` | `EXEC` | `team_id, data__name` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a team](https://docs.github.com/rest/teams/teams#update-a-team) endpoint.<br /><br />To edit a team, the authenticated user must either be an organization owner or a team maintainer.<br /><br />**Note:** With nested teams, the `privacy` for parent teams cannot be `secret`. |
