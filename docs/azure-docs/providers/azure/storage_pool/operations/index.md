---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - storage_pool
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_pool.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the operation being performed on this particular object |
| `actionType` | `string` | Indicates the action type. |
| `display` | `object` | Metadata about an operation. |
| `isDataAction` | `boolean` | Indicates whether the operation applies to data-plane. |
| `origin` | `string` | The intended executor of the operation; governs the display of the operation in the RBAC UX and the audit logs UX. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Operations_List` | `SELECT` |  |
