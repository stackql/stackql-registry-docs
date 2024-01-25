---
title: change_data_capture
hide_title: false
hide_table_of_contents: false
keywords:
  - change_data_capture
  - data_factory
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
<tr><td><b>Name</b></td><td><code>change_data_capture</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.change_data_capture</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `etag` | `string` | Etag identifies change in the resource. |
| `properties` | `object` | A Azure Data Factory object which automatically detects data changes at the source and then sends the updated data to the destination. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, changeDataCaptureName, factoryName, resourceGroupName, subscriptionId` | Gets a change data capture. |
| `list_by_factory` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists all resources of type change data capture. |
| `create_or_update` | `INSERT` | `api-version, changeDataCaptureName, factoryName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a change data capture resource. |
| `delete` | `DELETE` | `api-version, changeDataCaptureName, factoryName, resourceGroupName, subscriptionId` | Deletes a change data capture. |
| `_list_by_factory` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists all resources of type change data capture. |
| `start` | `EXEC` | `api-version, changeDataCaptureName, factoryName, resourceGroupName, subscriptionId` | Starts a change data capture. |
| `status` | `EXEC` | `api-version, changeDataCaptureName, factoryName, resourceGroupName, subscriptionId` | Gets the current status for the change data capture resource. |
| `stop` | `EXEC` | `api-version, changeDataCaptureName, factoryName, resourceGroupName, subscriptionId` | Stops a change data capture. |
