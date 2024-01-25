---
title: network_service_design_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - network_service_design_groups
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>network_service_design_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.network_service_design_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | network service design group properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkServiceDesignGroupName, publisherName, resourceGroupName, subscriptionId` | Gets information about the specified networkServiceDesign group. |
| `list_by_publisher` | `SELECT` | `publisherName, resourceGroupName, subscriptionId` | Gets information of the network service design groups under a publisher. |
| `create_or_update` | `INSERT` | `networkServiceDesignGroupName, publisherName, resourceGroupName, subscriptionId` | Creates or updates a network service design group. |
| `delete` | `DELETE` | `networkServiceDesignGroupName, publisherName, resourceGroupName, subscriptionId` | Deletes a specified network service design group. |
| `_list_by_publisher` | `EXEC` | `publisherName, resourceGroupName, subscriptionId` | Gets information of the network service design groups under a publisher. |
| `update` | `EXEC` | `networkServiceDesignGroupName, publisherName, resourceGroupName, subscriptionId` | Updates a network service design groups resource. |
