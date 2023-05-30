---
title: clienttokens
hide_title: false
hide_table_of_contents: false
keywords:
  - clienttokens
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
<tr><td><b>Name</b></td><td><code>clienttokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.clienttokens</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `issuer` | `string` |
| `createdBy` | `object` |
| `_embedded` | `object` |
| `clientId` | `string` |
| `_links` | `object` |
| `created` | `string` |
| `status` | `string` |
| `expiresAt` | `string` |
| `userId` | `string` |
| `lastUpdated` | `string` |
| `scopes` | `array` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clientId, tokenId, userId, subdomain` | Gets a refresh token issued for the specified User and Client. |
| `list` | `SELECT` | `clientId, userId, subdomain` | Lists all refresh tokens issued for the specified User and Client. |
| `delete` | `DELETE` | `clientId, tokenId, userId, subdomain` | Revokes the specified refresh token. |
| `deleteAll` | `EXEC` | `clientId, userId, subdomain` | Revokes all refresh tokens issued for the specified User and Client. |
