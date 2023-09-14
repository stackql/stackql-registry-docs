---
title: teams_for_auth_user
hide_title: false
hide_table_of_contents: false
keywords:
  - teams_for_auth_user
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
<tr><td><b>Name</b></td><td><code>teams_for_auth_user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.teams_for_auth_user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the team |
| `name` | `string` | Name of the team |
| `description` | `string` |  |
| `created_at` | `string` |  |
| `url` | `string` | URL for the team |
| `members_count` | `integer` |  |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `repos_count` | `integer` |  |
| `notification_setting` | `string` | The notification setting the team has set |
| `privacy` | `string` | The level of privacy this team should have |
| `permission` | `string` | Permission that the team will have for its repositories |
| `organization` | `object` | Team Organization |
| `ldap_dn` | `string` | Distinguished Name (DN) that team maps to within LDAP environment |
| `updated_at` | `string` |  |
| `members_url` | `string` |  |
| `node_id` | `string` |  |
| `repositories_url` | `string` |  |
| `html_url` | `string` |  |
| `slug` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_for_authenticated_user` | `SELECT` |  |
