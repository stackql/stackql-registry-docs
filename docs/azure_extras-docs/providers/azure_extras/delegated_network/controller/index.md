---
title: controller
hide_title: false
hide_table_of_contents: false
keywords:
  - controller
  - delegated_network
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
<tr><td><b>Name</b></td><td><code>controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.delegated_network.controller</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Controller_Create` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create a dnc controller |
| `Controller_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes the DNC controller |
| `Controller_GetDetails` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Gets details about the specified dnc controller. |
| `Controller_Patch` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Update dnc controller |
