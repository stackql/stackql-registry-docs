---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.policy.policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `conditions` | `object` |
| `_links` | `object` |
| `status` | `string` |
| `created` | `string` |
| `priority` | `integer` |
| `system` | `boolean` |
| `type` | `string` |
| `_embedded` | `object` |
| `lastUpdated` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `policyId` | Gets a policy. |
| `list` | `SELECT` | `type` | Gets all policies with the specified type. |
| `insert` | `INSERT` |  | Creates a policy. |
| `delete` | `DELETE` | `policyId` | Removes a policy. |
| `activate` | `EXEC` | `policyId, ruleId` | Activates a policy rule. |
| `deactivate` | `EXEC` | `policyId, ruleId` | Deactivates a policy rule. |
