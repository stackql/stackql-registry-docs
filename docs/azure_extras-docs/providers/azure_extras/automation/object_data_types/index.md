---
title: object_data_types
hide_title: false
hide_table_of_contents: false
keywords:
  - object_data_types
  - automation
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>object_data_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.object_data_types</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ObjectDataTypes_ListFieldsByModuleAndType` | `EXEC` | `automationAccountName, moduleName, resourceGroupName, subscriptionId, typeName` | Retrieve a list of fields of a given type identified by module name. |
| `ObjectDataTypes_ListFieldsByType` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId, typeName` | Retrieve a list of fields of a given type across all accessible modules. |
