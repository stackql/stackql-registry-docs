---
title: configuration_group_values
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_group_values
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
<tr><td><b>Name</b></td><td><code>configuration_group_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.configuration_group_values</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Hybrid configuration group value properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `configurationGroupValueName, resourceGroupName, subscriptionId` | Gets information about the specified hybrid configuration group values. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the hybrid network configurationGroupValues in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all sites in the configuration group value in a subscription. |
| `create_or_update` | `INSERT` | `configurationGroupValueName, resourceGroupName, subscriptionId` | Creates or updates a hybrid configuration group value. |
| `delete` | `DELETE` | `configurationGroupValueName, resourceGroupName, subscriptionId` | Deletes the specified hybrid configuration group value. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the hybrid network configurationGroupValues in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all sites in the configuration group value in a subscription. |
