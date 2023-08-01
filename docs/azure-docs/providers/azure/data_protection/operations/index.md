---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - data_protection
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
<tr><td><b>Id</b></td><td><code>azure.data_protection.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the Operation. |
| `properties` | `object` | Class to represent shoebox properties in json client discovery. |
| `display` | `object` | Localized display information of an operation. |
| `isDataAction` | `boolean` | Indicates whether the operation is a data action |
| `origin` | `string` | The intended executor of the operation;governs the display of the operation in the RBAC UX and the audit logs UX |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `DataProtectionOperations_List` | `SELECT` | `api-version` |
