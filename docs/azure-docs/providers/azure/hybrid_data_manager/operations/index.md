---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - hybrid_data_manager
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
<tr><td><b>Id</b></td><td><code>azure.hybrid_data_manager.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Gets or Sets Name of the operations |
| `display` | `object` | Contains the localized display information for this particular operation / action. <br />These value will be used by several clients for <br />(1) custom role definitions for RBAC; <br />(2) complex query filters for the event service; and (3) audit history / records for management operations. |
| `origin` | `string` | Gets or sets Origin<br />The intended executor of the operation; governs the display of the operation in the RBAC UX and the audit logs UX.<br />Default value is “user,system” |
| `properties` | `object` | Class represents Properties in AvailableProviderOperations |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Operations_List` | `SELECT` |  |
