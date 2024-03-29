---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - policy
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
<tr><td><b>Id</b></td><td><code>okta.policy.rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `_embedded` | `object` |
| `lastUpdated` | `string` |
| `system` | `boolean` |
| `priority` | `integer` |
| `conditions` | `object` |
| `_links` | `object` |
| `type` | `string` |
| `created` | `string` |
| `status` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `policyId, ruleId, subdomain` | Gets a policy rule. |
| `list` | `SELECT` | `type, subdomain` | Gets all policies with the specified type. |
| `insert` | `INSERT` | `policyId, subdomain` | Creates a policy rule. |
| `delete` | `DELETE` | `policyId, ruleId, subdomain` | Removes a policy rule. |
| `activate` | `EXEC` | `policyId, ruleId, subdomain` | Activates a policy rule. |
| `deactivate` | `EXEC` | `policyId, ruleId, subdomain` | Deactivates a policy rule. |
| `put` | `EXEC` | `policyId, ruleId, subdomain` | Updates a policy rule. |
