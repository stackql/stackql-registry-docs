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
| `e` | `string` |
| `alg` | `string` |
| `kid` | `string` |
| `x5u` | `string` |
| `expiresAt` | `string` |
| `lastUpdated` | `string` |
| `_links` | `object` |
| `x5t#S256` | `string` |
| `use` | `string` |
| `x5t` | `string` |
| `x5c` | `array` |
| `created` | `string` |
| `false` | `string` |
| `key_ops` | `array` |
| `kty` | `string` |
| `status` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `authServerId, subdomain` |
| `rotate` | `EXEC` | `authServerId, subdomain` |
