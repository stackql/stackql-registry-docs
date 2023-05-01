---
title: authorizationservers
hide_title: false
hide_table_of_contents: false
keywords:
  - authorizationservers
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
<tr><td><b>Name</b></td><td><code>authorizationservers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.authorizationservers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `credentials` | `object` |
| `issuer` | `string` |
| `created` | `string` |
| `audiences` | `array` |
| `issuerMode` | `string` |
| `lastUpdated` | `string` |
| `status` | `string` |
| `_links` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `authServerId` |
| `list` | `SELECT` |  |
| `insert` | `INSERT` |  |
| `delete` | `DELETE` | `authServerId` |
| `activate` | `EXEC` | `authServerId` |
| `deactivate` | `EXEC` | `authServerId` |
| `update` | `EXEC` | `authServerId` |
