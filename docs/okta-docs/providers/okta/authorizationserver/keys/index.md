---
title: keys
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
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `kty` | `string` |
| `_links` | `object` |
| `x5u` | `string` |
| `false` | `string` |
| `status` | `string` |
| `x5c` | `array` |
| `x5t#S256` | `string` |
| `use` | `string` |
| `key_ops` | `array` |
| `kid` | `string` |
| `expiresAt` | `string` |
| `created` | `string` |
| `x5t` | `string` |
| `lastUpdated` | `string` |
| `e` | `string` |
| `alg` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `authServerId` |
| `rotate` | `EXEC` | `authServerId` |
