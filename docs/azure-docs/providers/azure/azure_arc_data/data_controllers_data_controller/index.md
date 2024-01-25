---
title: data_controllers_data_controller
hide_title: false
hide_table_of_contents: false
keywords:
  - data_controllers_data_controller
  - azure_arc_data
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
<tr><td><b>Name</b></td><td><code>data_controllers_data_controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.azure_arc_data.data_controllers_data_controller</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | The complex type of the extended location. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The data controller properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, dataControllerName, resourceGroupName, subscriptionId` | Retrieves a dataController resource |
| `delete` | `DELETE` | `api-version, dataControllerName, resourceGroupName, subscriptionId` | Deletes a dataController resource |
