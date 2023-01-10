---
title: data_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - data_controllers
  - azure_arc_data
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
<tr><td><b>Name</b></td><td><code>data_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.azure_arc_data.data_controllers</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataControllers_DeleteDataController` | `EXEC` | `api-version, dataControllerName, resourceGroupName, subscriptionId` | Deletes a dataController resource |
| `DataControllers_GetDataController` | `EXEC` | `api-version, dataControllerName, resourceGroupName, subscriptionId` | Retrieves a dataController resource |
| `DataControllers_ListInGroup` | `EXEC` | `api-version, resourceGroupName, subscriptionId` |  |
| `DataControllers_ListInSubscription` | `EXEC` | `api-version, subscriptionId` |  |
| `DataControllers_PatchDataController` | `EXEC` | `api-version, dataControllerName, resourceGroupName, subscriptionId` | Updates a dataController resource |
| `DataControllers_PutDataController` | `EXEC` | `api-version, dataControllerName, resourceGroupName, subscriptionId, data__properties` | Creates or replaces a dataController resource |
