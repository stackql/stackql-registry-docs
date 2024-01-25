---
title: cloud_services_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_services_networks
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
<tr><td><b>Name</b></td><td><code>cloud_services_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.nexus.cloud_services_networks</code></td></tr>
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
| `get` | `SELECT` | `cloudServicesNetworkName, resourceGroupName, subscriptionId` | Get properties of the provided cloud services network. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of cloud services networks in the provided resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get a list of cloud services networks in the provided subscription. |
| `create_or_update` | `INSERT` | `cloudServicesNetworkName, resourceGroupName, subscriptionId, data__extendedLocation` | Create a new cloud services network or update the properties of the existing cloud services network. |
| `delete` | `DELETE` | `cloudServicesNetworkName, resourceGroupName, subscriptionId` | Delete the provided cloud services network. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get a list of cloud services networks in the provided resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get a list of cloud services networks in the provided subscription. |
| `update` | `EXEC` | `cloudServicesNetworkName, resourceGroupName, subscriptionId` | Update properties of the provided cloud services network, or update the tags associated with it. Properties and tag updates can be done independently. |
