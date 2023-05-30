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
| `lastUpdated` | `string` |
| `origin` | `string` |
| `status` | `string` |
| `created` | `string` |
| `lastUpdatedBy` | `string` |
| `createdBy` | `string` |
| `scopes` | `array` |
| `_links` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `trustedOriginId, subdomain` |
| `list` | `SELECT` | `subdomain` |
| `insert` | `INSERT` | `subdomain` |
| `delete` | `DELETE` | `trustedOriginId, subdomain` |
| `activate` | `EXEC` | `trustedOriginId, subdomain` |
| `deactivate` | `EXEC` | `trustedOriginId, subdomain` |
| `update` | `EXEC` | `trustedOriginId, subdomain` |
