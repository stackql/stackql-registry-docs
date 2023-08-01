---
title: grouptargets
hide_title: false
hide_table_of_contents: false
keywords:
  - grouptargets
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
<tr><td><b>Name</b></td><td><code>grouptargets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.group.grouptargets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `type` | `string` |
| `_embedded` | `object` |
| `created` | `string` |
| `profile` | `object` |
| `objectClass` | `array` |
| `lastMembershipUpdated` | `string` |
| `_links` | `object` |
| `lastUpdated` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `groupId, roleId, subdomain` | Success |
| `insert` | `INSERT` | `groupId, roleId, targetGroupId, subdomain` |  |
| `delete` | `DELETE` | `groupId, roleId, targetGroupId, subdomain` |  |
