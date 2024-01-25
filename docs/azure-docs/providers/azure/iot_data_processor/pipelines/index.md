---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - iot_data_processor
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
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_data_processor.pipelines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | Extended location is an extension of Azure locations. They provide a way to use their Azure ARC enabled Kubernetes clusters as target locations for deploying Azure services instances. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a Pipeline resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instanceName, pipelineName, resourceGroupName, subscriptionId` | Get a Pipeline |
| `list_by_instance` | `SELECT` | `instanceName, resourceGroupName, subscriptionId` | List Pipeline resources by Instance |
| `create_or_update` | `INSERT` | `instanceName, pipelineName, resourceGroupName, subscriptionId, data__extendedLocation` | Create a Pipeline |
| `delete` | `DELETE` | `instanceName, pipelineName, resourceGroupName, subscriptionId` | Delete a Pipeline |
| `_list_by_instance` | `EXEC` | `instanceName, resourceGroupName, subscriptionId` | List Pipeline resources by Instance |
| `update` | `EXEC` | `instanceName, pipelineName, resourceGroupName, subscriptionId` | Update a Pipeline |
