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
| `clientId` | `string` |
| `lastUpdated` | `string` |
| `expiresAt` | `string` |
| `status` | `string` |
| `userId` | `string` |
| `issuer` | `string` |
| `scopes` | `array` |
| `createdBy` | `object` |
| `_links` | `object` |
| `_embedded` | `object` |
| `created` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clientId, tokenId, userId` | Gets a refresh token issued for the specified User and Client. |
| `list` | `SELECT` | `clientId, userId` | Lists all refresh tokens issued for the specified User and Client. |
| `delete` | `DELETE` | `clientId, tokenId, userId` | Revokes the specified refresh token. |
| `deleteAll` | `EXEC` | `clientId, userId` | Revokes all refresh tokens issued for the specified User and Client. |
