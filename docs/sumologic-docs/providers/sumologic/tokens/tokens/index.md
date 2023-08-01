---
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - tokens
  - tokens
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.tokens.tokens</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the token. |
| `name` | `string` | Name of the token. |
| `description` | `string` | Description of the token. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `status` | `string` | Status of the token. Can be `Active`, or `Inactive`. |
| `type` | `string` | Type of the token. Valid values: 1) CollectorRegistrationTokenResponse |
| `version` | `integer` | Version of the token. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getToken` | `SELECT` | `id, region` | Get a token with the given identifier in the token library. |
| `listTokens` | `SELECT` | `region` | Get a list of all tokens in the token library. |
| `createToken` | `INSERT` | `data__name, data__status, data__type, region` | Create a token in the token library. |
| `deleteToken` | `DELETE` | `id, region` | Delete a token with the given identifier in the token library. |
| `updateToken` | `EXEC` | `id, data__name, data__status, data__type, data__version, region` | Update a token with the given identifier in the token library. |
