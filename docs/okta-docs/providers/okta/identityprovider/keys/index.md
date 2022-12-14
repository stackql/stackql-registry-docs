---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - identityprovider
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
<tr><td><b>Id</b></td><td><code>okta.identityprovider.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `x5u` | `string` |
| `expiresAt` | `string` |
| `e` | `string` |
| `key_ops` | `array` |
| `status` | `string` |
| `x5c` | `array` |
| `kid` | `string` |
| `created` | `string` |
| `lastUpdated` | `string` |
| `kty` | `string` |
| `use` | `string` |
| `x5t` | `string` |
| `alg` | `string` |
| `_links` | `object` |
| `false` | `string` |
| `x5t#S256` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `keyId` | Gets a specific IdP Key Credential by `kid` |
| `list` | `SELECT` |  | Enumerates IdP key credentials. |
| `insert` | `INSERT` |  | Adds a new X.509 certificate credential to the IdP key store. |
| `delete` | `DELETE` | `keyId` | Deletes a specific IdP Key Credential by `kid` if it is not currently being used by an Active or Inactive IdP. |
