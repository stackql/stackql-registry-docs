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
| `x5c` | `array` |
| `expiresAt` | `string` |
| `created` | `string` |
| `key_ops` | `array` |
| `status` | `string` |
| `x5u` | `string` |
| `_links` | `object` |
| `kty` | `string` |
| `e` | `string` |
| `lastUpdated` | `string` |
| `use` | `string` |
| `x5t#S256` | `string` |
| `kid` | `string` |
| `false` | `string` |
| `alg` | `string` |
| `x5t` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appId, keyId, subdomain` | Gets a specific application key credential by kid |
| `list` | `SELECT` | `appId, subdomain` | Enumerates key credentials for an application |
| `insert` | `INSERT` | `appId, subdomain` | Generates a new X.509 certificate for an application key credential |
| `delete` | `DELETE` | `appId, csrId, subdomain` |  |
