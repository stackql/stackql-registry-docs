---
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - tokens
  - authorizationserver
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
<tr><td><b>Name</b></td><td><code>tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.tokens</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `clientId` | `string` |
| `created` | `string` |
| `createdBy` | `object` |
| `_links` | `object` |
| `userId` | `string` |
| `issuer` | `string` |
| `status` | `string` |
| `_embedded` | `object` |
| `expiresAt` | `string` |
| `scopes` | `array` |
| `lastUpdated` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `authServerId, clientId, tokenId` |
| `list` | `SELECT` | `authServerId, clientId` |
| `delete` | `DELETE` | `authServerId, clientId, tokenId` |
| `deleteall` | `EXEC` | `authServerId, clientId` |
