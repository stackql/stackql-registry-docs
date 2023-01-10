---
title: clientgrants
hide_title: false
hide_table_of_contents: false
keywords:
  - clientgrants
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
<tr><td><b>Name</b></td><td><code>clientgrants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.clientgrants</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `_links` | `object` |
| `lastUpdated` | `string` |
| `status` | `string` |
| `source` | `string` |
| `userId` | `string` |
| `scopeId` | `string` |
| `_embedded` | `object` |
| `created` | `string` |
| `issuer` | `string` |
| `clientId` | `string` |
| `createdBy` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `clientId, userId` | Lists all grants for a specified user and client |
| `delete` | `DELETE` | `clientId, userId` | Revokes all grants for the specified user and client |
