---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
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
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `created` | `string` |
| `e` | `string` |
| `expiresAt` | `string` |
| `alg` | `string` |
| `x5c` | `array` |
| `x5t` | `string` |
| `x5t#S256` | `string` |
| `status` | `string` |
| `kty` | `string` |
| `use` | `string` |
| `x5u` | `string` |
| `lastUpdated` | `string` |
| `false` | `string` |
| `kid` | `string` |
| `_links` | `object` |
| `key_ops` | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `authServerId` |
| `rotate` | `EXEC` | `authServerId` |
