---
title: details
hide_title: false
hide_table_of_contents: false
keywords:
  - details
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
<tr><td><b>Name</b></td><td><code>details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the team |
| `name` | `string` | Name of the team |
| `description` | `string` |  |
| `ldap_dn` | `string` | Distinguished Name (DN) that team maps to within LDAP environment |
| `permission` | `string` | Permission that the team will have for its repositories |
| `members_count` | `integer` |  |
| `url` | `string` | URL for the team |
| `members_url` | `string` |  |
| `node_id` | `string` |  |
| `repos_count` | `integer` |  |
| `created_at` | `string` |  |
| `repositories_url` | `string` |  |
| `slug` | `string` |  |
| `updated_at` | `string` |  |
| `privacy` | `string` | The level of privacy this team should have |
| `html_url` | `string` |  |
| `notification_setting` | `string` | The notification setting the team has set |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `organization` | `object` | Team Organization |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_by_name` | `SELECT` | `org, team_slug` |
