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
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `permission` | `string` |  |
| `html_url` | `string` |  |
| `url` | `string` |  |
| `node_id` | `string` |  |
| `privacy` | `string` |  |
| `repositories_url` | `string` |  |
| `permissions` | `object` |  |
| `slug` | `string` |  |
| `notification_setting` | `string` |  |
| `members_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_child_legacy` | `SELECT` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List child teams`](https://docs.github.com/rest/teams/teams#list-child-teams) endpoint. |
| `delete_legacy` | `DELETE` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Delete a team](https://docs.github.com/rest/teams/teams#delete-a-team) endpoint.<br /><br />To delete a team, the authenticated user must be an organization owner or team maintainer.<br /><br />If you are an organization owner, deleting a parent team will delete all of its child teams as well. |
| `get_legacy` | `EXEC` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the [Get a team by name](https://docs.github.com/rest/teams/teams#get-a-team-by-name) endpoint. |
| `update_legacy` | `EXEC` | `team_id, data__name` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a team](https://docs.github.com/rest/teams/teams#update-a-team) endpoint.<br /><br />To edit a team, the authenticated user must either be an organization owner or a team maintainer.<br /><br />**Note:** With nested teams, the `privacy` for parent teams cannot be `secret`. |
