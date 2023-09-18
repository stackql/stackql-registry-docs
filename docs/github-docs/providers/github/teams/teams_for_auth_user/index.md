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
| `members_url` | `string` |  |
| `created_at` | `string` |  |
| `ldap_dn` | `string` | Distinguished Name (DN) that team maps to within LDAP environment |
| `privacy` | `string` | The level of privacy this team should have |
| `node_id` | `string` |  |
| `organization` | `object` | Team Organization |
| `updated_at` | `string` |  |
| `html_url` | `string` |  |
| `repositories_url` | `string` |  |
| `slug` | `string` |  |
| `repos_count` | `integer` |  |
| `url` | `string` | URL for the team |
| `notification_setting` | `string` | The notification setting the team has set |
| `members_count` | `integer` |  |
| `permission` | `string` | Permission that the team will have for its repositories |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_for_authenticated_user` | `SELECT` |  |
