---
title: csrs
hide_title: false
hide_table_of_contents: false
keywords:
  - okta
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>csrs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.identityprovider.csrs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `csr` | `string` |
| `kty` | `string` |
| `created` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `csrId, idpId` | Gets a specific Certificate Signing Request model by id |
| `list` | `SELECT` | `idpId` | Enumerates Certificate Signing Requests for an IdP |
| `insert` | `INSERT` | `idpId` | Generates a new key pair and returns a Certificate Signing Request for it. |
| `delete` | `DELETE` | `csrId, idpId` | Revoke a Certificate Signing Request and delete the key pair from the IdP |
