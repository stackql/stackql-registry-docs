---
title: metrics_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics_configurations
  - nexus
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
<tr><td><b>Name</b></td><td><code>metrics_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.nexus.metrics_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` |  |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, metricsConfigurationName, resourceGroupName, subscriptionId` | Get metrics configuration of the provided cluster. |
| `list_by_cluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Get a list of metrics configurations for the provided cluster. |
| `create_or_update` | `INSERT` | `clusterName, metricsConfigurationName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties` | Create new or update the existing metrics configuration of the provided cluster. |
| `delete` | `DELETE` | `clusterName, metricsConfigurationName, resourceGroupName, subscriptionId` | Delete the metrics configuration of the provided cluster. |
| `_list_by_cluster` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Get a list of metrics configurations for the provided cluster. |
| `update` | `EXEC` | `clusterName, metricsConfigurationName, resourceGroupName, subscriptionId` | Patch properties of metrics configuration for the provided cluster, or update the tags associated with it. Properties and tag updates can be done independently. |
