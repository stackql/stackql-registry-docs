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
| `created` | `string` |
| `createdBy` | `object` |
| `lastUpdated` | `string` |
| `scopes` | `array` |
| `expiresAt` | `string` |
| `_links` | `object` |
| `issuer` | `string` |
| `userId` | `string` |
| `status` | `string` |
| `_embedded` | `object` |
| `clientId` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `authServerId, clientId, tokenId, subdomain` |
| `list` | `SELECT` | `authServerId, clientId, subdomain` |
| `delete` | `DELETE` | `authServerId, clientId, tokenId, subdomain` |
| `deleteall` | `EXEC` | `authServerId, clientId, subdomain` |
