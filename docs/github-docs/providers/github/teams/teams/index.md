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
| `id` | `integer` | Unique identifier of the team |
| `name` | `string` | Name of the team |
| `description` | `string` |  |
| `html_url` | `string` |  |
| `privacy` | `string` | The level of privacy this team should have |
| `repos_count` | `integer` |  |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
| `permission` | `string` | Permission that the team will have for its repositories |
| `slug` | `string` |  |
| `members_url` | `string` |  |
| `repositories_url` | `string` |  |
| `url` | `string` | URL for the team |
| `ldap_dn` | `string` | Distinguished Name (DN) that team maps to within LDAP environment |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `updated_at` | `string` |  |
| `members_count` | `integer` |  |
| `organization` | `object` | Organization Full |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_by_name` | `SELECT` | `org, team_slug` | Gets a team using the team's `slug`. GitHub generates the `slug` from the team `name`.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;`. |
| `list` | `SELECT` | `org` | Lists all teams in an organization that are visible to the authenticated user. |
| `list_for_authenticated_user` | `SELECT` |  | List all of the teams across all of the organizations to which the authenticated user belongs. This method requires `user`, `repo`, or `read:org` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/) when authenticating via [OAuth](https://docs.github.com/apps/building-oauth-apps/). |
| `create` | `INSERT` | `org, data__name` | To create a team, the authenticated user must be a member or owner of `&#123;org&#125;`. By default, organization members can create teams. Organization owners can limit team creation to organization owners. For more information, see "[Setting team creation permissions](https://docs.github.com/en/articles/setting-team-creation-permissions-in-your-organization)."<br /><br />When you create a new team, you automatically become a team maintainer without explicitly adding yourself to the optional array of `maintainers`. For more information, see "[About teams](https://docs.github.com/en/github/setting-up-and-managing-organizations-and-teams/about-teams)". |
| `delete_in_org` | `DELETE` | `org, team_slug` | To delete a team, the authenticated user must be an organization owner or team maintainer.<br /><br />If you are an organization owner, deleting a parent team will delete all of its child teams as well.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;`. |
| `update_in_org` | `EXEC` | `org, team_slug` | To edit a team, the authenticated user must either be an organization owner or a team maintainer.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;`. |
