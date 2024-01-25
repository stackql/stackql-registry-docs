---
title: site_network_services
hide_title: false
hide_table_of_contents: false
keywords:
  - site_network_services
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
<tr><td><b>Name</b></td><td><code>site_network_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.site_network_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Site network service properties. |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, siteNetworkServiceName, subscriptionId` | Gets information about the specified site network service. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all site network services. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all sites in the network service in a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, siteNetworkServiceName, subscriptionId` | Creates or updates a network site. |
| `delete` | `DELETE` | `resourceGroupName, siteNetworkServiceName, subscriptionId` | Deletes the specified site network service. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all site network services. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all sites in the network service in a subscription. |
