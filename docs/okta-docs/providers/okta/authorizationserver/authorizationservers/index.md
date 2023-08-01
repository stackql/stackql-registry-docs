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
| `issuerMode` | `string` |
| `_links` | `object` |
| `lastUpdated` | `string` |
| `status` | `string` |
| `created` | `string` |
| `credentials` | `object` |
| `audiences` | `array` |
| `issuer` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `authServerId, subdomain` |
| `list` | `SELECT` | `subdomain` |
| `insert` | `INSERT` | `subdomain` |
| `delete` | `DELETE` | `authServerId, subdomain` |
| `activate` | `EXEC` | `authServerId, subdomain` |
| `deactivate` | `EXEC` | `authServerId, subdomain` |
| `update` | `EXEC` | `authServerId, subdomain` |
