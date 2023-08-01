---
title: azure_traffic_collectors
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_traffic_collectors
  - network_function
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
<tr><td><b>Name</b></td><td><code>azure_traffic_collectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network_function.azure_traffic_collectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Azure Traffic Collector resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AzureTrafficCollectors_Get` | `SELECT` | `azureTrafficCollectorName, resourceGroupName, subscriptionId` | Gets the specified Azure Traffic Collector in a specified resource group |
| `AzureTrafficCollectors_CreateOrUpdate` | `INSERT` | `azureTrafficCollectorName, resourceGroupName, subscriptionId` | Creates or updates a Azure Traffic Collector resource |
| `AzureTrafficCollectors_Delete` | `DELETE` | `azureTrafficCollectorName, resourceGroupName, subscriptionId` | Deletes a specified Azure Traffic Collector resource. |
| `AzureTrafficCollectors_UpdateTags` | `EXEC` | `azureTrafficCollectorName, resourceGroupName, subscriptionId` | Updates the specified Azure Traffic Collector tags. |
