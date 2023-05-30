---
title: grants
hide_title: false
hide_table_of_contents: false
keywords:
  - grants
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
<tr><td><b>Name</b></td><td><code>grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.grants</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `clientId` | `string` |
| `created` | `string` |
| `lastUpdated` | `string` |
| `createdBy` | `object` |
| `userId` | `string` |
| `source` | `string` |
| `issuer` | `string` |
| `scopeId` | `string` |
| `_links` | `object` |
| `status` | `string` |
| `_embedded` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `grantId, userId, subdomain` | Gets a grant for the specified user |
| `list` | `SELECT` | `userId, subdomain` | Lists all grants for the specified user |
| `delete` | `DELETE` | `grantId, userId, subdomain` | Revokes one grant for a specified user |
| `deleteAll` | `EXEC` | `userId, subdomain` | Revokes all grants for a specified user |
