---
title: descendants
hide_title: false
hide_table_of_contents: false
keywords:
  - descendants
  - management_groups
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
<tr><td><b>Name</b></td><td><code>descendants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.management_groups.descendants</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The fully qualified ID for the descendant.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000 or /subscriptions/0000000-0000-0000-0000-000000000000 |
| `name` | `string` | The name of the descendant. For example, 00000000-0000-0000-0000-000000000000 |
| `properties` | `object` | The generic properties of an descendant. |
| `type` | `string` | The type of the resource. For example, Microsoft.Management/managementGroups or /subscriptions |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `groupId` |
| `_get` | `EXEC` | `groupId` |
