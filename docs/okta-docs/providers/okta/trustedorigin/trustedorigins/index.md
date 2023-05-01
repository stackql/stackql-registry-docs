---
title: trustedorigins
hide_title: false
hide_table_of_contents: false
keywords:
  - trustedorigins
  - trustedorigin
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
<tr><td><b>Name</b></td><td><code>trustedorigins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.trustedorigin.trustedorigins</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `createdBy` | `string` |
| `lastUpdated` | `string` |
| `lastUpdatedBy` | `string` |
| `origin` | `string` |
| `scopes` | `array` |
| `status` | `string` |
| `_links` | `object` |
| `created` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `trustedOriginId` |
| `list` | `SELECT` |  |
| `insert` | `INSERT` |  |
| `delete` | `DELETE` | `trustedOriginId` |
| `activate` | `EXEC` | `trustedOriginId` |
| `deactivate` | `EXEC` | `trustedOriginId` |
| `update` | `EXEC` | `trustedOriginId` |
