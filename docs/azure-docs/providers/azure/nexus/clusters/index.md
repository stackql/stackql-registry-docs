---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.nexus.clusters</code></td></tr>
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
| `get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Get properties of the provided cluster. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of clusters in the provided resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get a list of clusters in the provided subscription. |
| `create_or_update` | `INSERT` | `clusterName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties` | Create a new cluster or update the properties of the cluster if it exists. |
| `delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Delete the provided cluster. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get a list of clusters in the provided resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get a list of clusters in the provided subscription. |
| `deploy` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Deploy the cluster using the rack configuration provided during creation. |
| `scan_runtime` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Triggers the execution of a runtime protection scan to detect and remediate detected issues, in accordance with the cluster configuration. |
| `update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Patch the properties of the provided cluster, or update the tags associated with the cluster. Properties and tag updates can be done independently. |
