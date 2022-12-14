---
title: admin_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - admin_rules
  - network
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>admin_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.admin_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `kind` | `string` | Whether the rule is custom or default. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AdminRules_Get` | `SELECT` |  | Gets a network manager security configuration admin rule. |
| `AdminRules_List` | `SELECT` |  | List all network manager security configuration admin rules. |
| `AdminRules_CreateOrUpdate` | `INSERT` | `data__kind` | Creates or updates an admin rule. |
| `AdminRules_Delete` | `DELETE` |  | Deletes an admin rule. |
