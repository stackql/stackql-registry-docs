---
title: security_managers
hide_title: false
hide_table_of_contents: false
keywords:
  - security_managers
  - orgs
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
<tr><td><b>Name</b></td><td><code>security_managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.security_managers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the team |
| `name` | `string` | Name of the team |
| `description` | `string` | Description of the team |
| `permission` | `string` | Permission that the team will have for its repositories |
| `notification_setting` | `string` | The notification setting the team has set |
| `html_url` | `string` |  |
| `privacy` | `string` | The level of privacy this team should have |
| `url` | `string` | URL for the team |
| `repositories_url` | `string` |  |
| `slug` | `string` |  |
| `ldap_dn` | `string` | Distinguished Name (DN) that team maps to within LDAP environment |
| `node_id` | `string` |  |
| `members_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_security_manager_teams` | `SELECT` | `org` |
