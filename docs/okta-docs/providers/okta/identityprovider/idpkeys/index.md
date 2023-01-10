---
title: idpkeys
hide_title: false
hide_table_of_contents: false
keywords:
  - idpkeys
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
<tr><td><b>Name</b></td><td><code>idpkeys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.identityprovider.idpkeys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `kty` | `string` |
| `created` | `string` |
| `false` | `string` |
| `_links` | `object` |
| `key_ops` | `array` |
| `kid` | `string` |
| `use` | `string` |
| `e` | `string` |
| `status` | `string` |
| `x5t#S256` | `string` |
| `x5c` | `array` |
| `alg` | `string` |
| `expiresAt` | `string` |
| `x5t` | `string` |
| `lastUpdated` | `string` |
| `x5u` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `idpId, keyId` | Gets a specific IdP Key Credential by `kid` |
| `list` | `SELECT` | `idpId` | Enumerates signing key credentials for an IdP |
| `insert` | `INSERT` | `idpId, validityYears` | Generates a new X.509 certificate for an IdP signing key credential to be used for signing assertions sent to the IdP |
| `clone` | `EXEC` | `idpId, keyId, targetIdpId` | Clones a X.509 certificate for an IdP signing key credential from a source IdP to target IdP |
