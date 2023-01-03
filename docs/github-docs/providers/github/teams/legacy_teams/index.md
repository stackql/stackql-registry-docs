---
title: legacy_teams
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>legacy_teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.legacy_teams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the team |
| `name` | `string` | Name of the team |
| `description` | `string` |  |
| `organization` | `object` | Organization Full |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `created_at` | `string` |  |
| `slug` | `string` |  |
| `permission` | `string` | Permission that the team will have for its repositories |
| `ldap_dn` | `string` | Distinguished Name (DN) that team maps to within LDAP environment |
| `html_url` | `string` |  |
| `members_url` | `string` |  |
| `privacy` | `string` | The level of privacy this team should have |
| `repositories_url` | `string` |  |
| `members_count` | `integer` |  |
| `repos_count` | `integer` |  |
| `url` | `string` | URL for the team |
| `updated_at` | `string` |  |
| `node_id` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_legacy` | `SELECT` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the [Get a team by name](https://docs.github.com/rest/reference/teams#get-a-team-by-name) endpoint. |
| `delete_legacy` | `DELETE` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Delete a team](https://docs.github.com/rest/reference/teams#delete-a-team) endpoint.<br /><br />To delete a team, the authenticated user must be an organization owner or team maintainer.<br /><br />If you are an organization owner, deleting a parent team will delete all of its child teams as well. |
| `update_legacy` | `EXEC` | `team_id, data__name` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a team](https://docs.github.com/rest/reference/teams#update-a-team) endpoint.<br /><br />To edit a team, the authenticated user must either be an organization owner or a team maintainer.<br /><br />**Note:** With nested teams, the `privacy` for parent teams cannot be `secret`. |
