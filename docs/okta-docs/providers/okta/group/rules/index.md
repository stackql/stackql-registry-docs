---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - group
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
<tr><td><b>Id</b></td><td><code>okta.group.rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `status` | `string` |
| `type` | `string` |
| `actions` | `object` |
| `conditions` | `object` |
| `created` | `string` |
| `lastUpdated` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `ruleId` | Fetches a specific group rule by id from your organization |
| `list` | `SELECT` |  | Lists all group rules for your organization. |
| `insert` | `INSERT` |  | Creates a group rule to dynamically add users to the specified group if they match the condition |
| `delete` | `DELETE` | `ruleId` | Removes a specific group rule by id from your organization |
| `update` | `EXEC` | `ruleId` | Updates a group rule. Only `INACTIVE` rules can be updated. |
