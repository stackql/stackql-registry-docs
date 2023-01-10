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
| `status` | `string` |
| `_embedded` | `object` |
| `expiresAt` | `string` |
| `issuer` | `string` |
| `scopes` | `array` |
| `_links` | `object` |
| `created` | `string` |
| `lastUpdated` | `string` |
| `userId` | `string` |
| `clientId` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appId, tokenId` | Gets a token for the specified application |
| `list` | `SELECT` | `appId` | Lists all tokens for the application |
| `delete` | `DELETE` | `appId, tokenId` | Revokes the specified token for the specified application |
