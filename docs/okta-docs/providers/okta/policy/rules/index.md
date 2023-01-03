---
title: rules
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
| `lastUpdated` | `string` |
| `status` | `string` |
| `type` | `string` |
| `_links` | `object` |
| `priority` | `integer` |
| `created` | `string` |
| `system` | `boolean` |
| `_embedded` | `object` |
| `conditions` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `policyId, ruleId` | Gets a policy rule. |
| `list` | `SELECT` | `type` | Gets all policies with the specified type. |
| `insert` | `INSERT` | `policyId` | Creates a policy rule. |
| `delete` | `DELETE` | `policyId, ruleId` | Removes a policy rule. |
| `activate` | `EXEC` | `policyId, ruleId` | Activates a policy rule. |
| `deactivate` | `EXEC` | `policyId, ruleId` | Deactivates a policy rule. |
| `put` | `EXEC` | `policyId, ruleId` | Updates a policy rule. |
