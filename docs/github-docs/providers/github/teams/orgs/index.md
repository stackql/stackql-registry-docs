---
title: orgs
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs
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
<tr><td><b>Name</b></td><td><code>orgs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.orgs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `url` | `string` |  |
| `node_id` | `string` |  |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `notification_setting` | `string` |  |
| `members_url` | `string` |  |
| `privacy` | `string` |  |
| `html_url` | `string` |  |
| `slug` | `string` |  |
| `permission` | `string` |  |
| `repositories_url` | `string` |  |
| `permissions` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `org` | Lists all teams in an organization that are visible to the authenticated user. |
| `list_child_in_org` | `SELECT` | `org, team_slug` | Lists the child teams of the team specified by `&#123;team_slug&#125;`.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/teams`. |
| `create` | `INSERT` | `org, data__name` | To create a team, the authenticated user must be a member or owner of `&#123;org&#125;`. By default, organization members can create teams. Organization owners can limit team creation to organization owners. For more information, see "[Setting team creation permissions](https://docs.github.com/articles/setting-team-creation-permissions-in-your-organization)."<br /><br />When you create a new team, you automatically become a team maintainer without explicitly adding yourself to the optional array of `maintainers`. For more information, see "[About teams](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/about-teams)". |
| `delete_in_org` | `DELETE` | `org, team_slug` | To delete a team, the authenticated user must be an organization owner or team maintainer.<br /><br />If you are an organization owner, deleting a parent team will delete all of its child teams as well.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;`. |
| `get_by_name` | `EXEC` | `org, team_slug` | Gets a team using the team's `slug`. To create the `slug`, GitHub replaces special characters in the `name` string, changes all words to lowercase, and replaces spaces with a `-` separator. For example, `"My TEam Näme"` would become `my-team-name`.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;`. |
| `update_in_org` | `EXEC` | `org, team_slug` | To edit a team, the authenticated user must either be an organization owner or a team maintainer.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;`. |
