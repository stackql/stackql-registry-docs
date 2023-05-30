---
title: grouptargets
hide_title: false
hide_table_of_contents: false
keywords:
  - grouptargets
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
<tr><td><b>Name</b></td><td><code>grouptargets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.grouptargets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `objectClass` | `array` |
| `type` | `string` |
| `lastMembershipUpdated` | `string` |
| `profile` | `object` |
| `created` | `string` |
| `lastUpdated` | `string` |
| `_embedded` | `object` |
| `_links` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `roleId, userId, subdomain` |
| `insert` | `INSERT` | `groupId, roleId, userId, subdomain` |
| `delete` | `DELETE` | `groupId, roleId, userId, subdomain` |
