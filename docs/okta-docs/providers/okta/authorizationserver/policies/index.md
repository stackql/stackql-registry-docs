---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `status` | `string` |
| `conditions` | `object` |
| `priority` | `integer` |
| `system` | `boolean` |
| `_embedded` | `object` |
| `_links` | `object` |
| `created` | `string` |
| `type` | `string` |
| `lastUpdated` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `authServerId, policyId, subdomain` | Success |
| `list` | `SELECT` | `authServerId, subdomain` | Success |
| `insert` | `INSERT` | `authServerId, subdomain` | Success |
| `delete` | `DELETE` | `authServerId, policyId, subdomain` | Success |
| `activate` | `EXEC` | `authServerId, policyId, subdomain` | Activate Authorization Server Policy |
| `deactivate` | `EXEC` | `authServerId, policyId, subdomain` | Deactivate Authorization Server Policy |
| `update` | `EXEC` | `authServerId, policyId, subdomain` | Success |
