---
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - tokens
  - application
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
<tr><td><b>Id</b></td><td><code>okta.application.tokens</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `issuer` | `string` |
| `_embedded` | `object` |
| `created` | `string` |
| `status` | `string` |
| `_links` | `object` |
| `clientId` | `string` |
| `lastUpdated` | `string` |
| `scopes` | `array` |
| `expiresAt` | `string` |
| `userId` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appId, tokenId, subdomain` | Gets a token for the specified application |
| `list` | `SELECT` | `appId, subdomain` | Lists all tokens for the application |
| `delete` | `DELETE` | `appId, tokenId, subdomain` | Revokes the specified token for the specified application |
