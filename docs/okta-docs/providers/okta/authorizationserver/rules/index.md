---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
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
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `actions` | `object` |
| `type` | `string` |
| `status` | `string` |
| `system` | `boolean` |
| `conditions` | `object` |
| `created` | `string` |
| `lastUpdated` | `string` |
| `priority` | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `authServerId, policyId, ruleId, subdomain` | Returns a Policy Rule by ID that is defined in the specified Custom Authorization Server and Policy. |
| `list` | `SELECT` | `authServerId, policyId, subdomain` | Enumerates all policy rules for the specified Custom Authorization Server and Policy. |
| `insert` | `INSERT` | `authServerId, policyId, subdomain` | Creates a policy rule for the specified Custom Authorization Server and Policy. |
| `delete` | `DELETE` | `authServerId, policyId, ruleId, subdomain` | Deletes a Policy Rule defined in the specified Custom Authorization Server and Policy. |
| `activate` | `EXEC` | `authServerId, policyId, ruleId, subdomain` | Activate Authorization Server Policy Rule |
| `deactivate` | `EXEC` | `authServerId, policyId, ruleId, subdomain` | Deactivate Authorization Server Policy Rule |
| `update` | `EXEC` | `authServerId, policyId, ruleId, subdomain` | Updates the configuration of the Policy Rule defined in the specified Custom Authorization Server and Policy. |
