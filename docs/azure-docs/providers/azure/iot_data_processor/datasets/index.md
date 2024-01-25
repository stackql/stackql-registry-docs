---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
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
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_data_processor.datasets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | Extended location is an extension of Azure locations. They provide a way to use their Azure ARC enabled Kubernetes clusters as target locations for deploying Azure services instances. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a Dataset resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `datasetName, instanceName, resourceGroupName, subscriptionId` | Get a Dataset |
| `list_by_instance` | `SELECT` | `instanceName, resourceGroupName, subscriptionId` | List Dataset resources by Instance |
| `create_or_update` | `INSERT` | `datasetName, instanceName, resourceGroupName, subscriptionId, data__extendedLocation` | Create a Dataset |
| `delete` | `DELETE` | `datasetName, instanceName, resourceGroupName, subscriptionId` | Delete a Dataset |
| `_list_by_instance` | `EXEC` | `instanceName, resourceGroupName, subscriptionId` | List Dataset resources by Instance |
| `update` | `EXEC` | `datasetName, instanceName, resourceGroupName, subscriptionId` | Update a Dataset |
