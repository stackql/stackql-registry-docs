---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
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
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the team |
| `name` | `string` | Name of the team |
| `description` | `string` |  |
| `node_id` | `string` |  |
| `html_url` | `string` |  |
| `privacy` | `string` | The level of privacy this team should have |
| `url` | `string` | URL for the team |
| `organization` | `object` | Team Organization |
| `notification_setting` | `string` | The notification setting the team has set |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `members_url` | `string` |  |
| `slug` | `string` |  |
| `repositories_url` | `string` |  |
| `created_at` | `string` |  |
| `repos_count` | `integer` |  |
| `permission` | `string` | Permission that the team will have for its repositories |
| `members_count` | `integer` |  |
| `updated_at` | `string` |  |
| `ldap_dn` | `string` | Distinguished Name (DN) that team maps to within LDAP environment |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_for_authenticated_user` | `SELECT` |  |
