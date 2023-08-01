---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - group
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.group.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `status` | `string` |
| `created` | `string` |
| `statusChanged` | `string` |
| `credentials` | `object` |
| `lastLogin` | `string` |
| `profile` | `object` |
| `_links` | `object` |
| `activated` | `string` |
| `transitioningToStatus` | `string` |
| `type` | `object` |
| `lastUpdated` | `string` |
| `_embedded` | `object` |
| `passwordChanged` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `groupId, subdomain` | Enumerates all users that are a member of a group. |
| `insert` | `INSERT` | `groupId, userId, subdomain` | Adds a user to a group with 'OKTA_GROUP' type. |
| `delete` | `DELETE` | `groupId, userId, subdomain` | Removes a user from a group with 'OKTA_GROUP' type. |
