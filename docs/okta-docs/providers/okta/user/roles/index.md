---
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
  - user
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.roles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `description` | `string` |
| `assignmentType` | `string` |
| `lastUpdated` | `string` |
| `status` | `string` |
| `_embedded` | `object` |
| `label` | `string` |
| `type` | `string` |
| `created` | `string` |
| `_links` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `roleId, userId, subdomain` | Gets role that is assigne to user. |
| `list` | `SELECT` | `userId, subdomain` | Lists all roles assigned to a user. |
| `insert` | `INSERT` | `userId, subdomain` | Assigns a role to a user. |
| `delete` | `DELETE` | `roleId, userId, subdomain` | Unassigns a role from a user. |
