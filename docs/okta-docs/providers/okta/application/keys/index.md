---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
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
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.application.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `x5t#S256` | `string` |
| `x5c` | `array` |
| `e` | `string` |
| `alg` | `string` |
| `kid` | `string` |
| `x5t` | `string` |
| `status` | `string` |
| `expiresAt` | `string` |
| `x5u` | `string` |
| `created` | `string` |
| `lastUpdated` | `string` |
| `key_ops` | `array` |
| `false` | `string` |
| `_links` | `object` |
| `use` | `string` |
| `kty` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appId, keyId` | Gets a specific application key credential by kid |
| `list` | `SELECT` | `appId` | Enumerates key credentials for an application |
| `insert` | `INSERT` | `appId` | Generates a new X.509 certificate for an application key credential |
| `delete` | `DELETE` | `appId, csrId` |  |
