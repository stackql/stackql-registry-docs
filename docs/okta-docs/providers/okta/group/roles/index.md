---
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
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
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.group.roles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `description` | `string` |
| `lastUpdated` | `string` |
| `status` | `string` |
| `_links` | `object` |
| `type` | `string` |
| `label` | `string` |
| `assignmentType` | `string` |
| `_embedded` | `object` |
| `created` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `groupId, roleId, subdomain` | Success |
| `list` | `SELECT` | `groupId, subdomain` | Success |
| `insert` | `INSERT` | `groupId, subdomain` | Assigns a Role to a Group |
| `delete` | `DELETE` | `groupId, roleId, subdomain` | Unassigns a Role from a Group |
