---
title: usertokens
hide_title: false
hide_table_of_contents: false
keywords:
  - usertokens
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
<tr><td><b>Name</b></td><td><code>usertokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.identityprovider.usertokens</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `tokenAuthScheme` | `string` |
| `tokenType` | `string` |
| `expiresAt` | `string` |
| `scopes` | `array` |
| `token` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `idpId, userId, subdomain` |
