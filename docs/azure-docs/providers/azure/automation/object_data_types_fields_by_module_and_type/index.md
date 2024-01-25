---
title: object_data_types_fields_by_module_and_type
hide_title: false
hide_table_of_contents: false
keywords:
  - object_data_types_fields_by_module_and_type
  - automation
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
<tr><td><b>Name</b></td><td><code>object_data_types_fields_by_module_and_type</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.object_data_types_fields_by_module_and_type</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Gets or sets the name of the field. |
| `type` | `string` | Gets or sets the type of the field. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `automationAccountName, moduleName, resourceGroupName, subscriptionId, typeName` |
| `_list` | `EXEC` | `automationAccountName, moduleName, resourceGroupName, subscriptionId, typeName` |
