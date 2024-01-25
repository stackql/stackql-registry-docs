---
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
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
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Site properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, siteName, subscriptionId` | Gets information about the specified network site. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all sites in the network service. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all sites in the network service in a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, siteName, subscriptionId` | Creates or updates a network site. |
| `delete` | `DELETE` | `resourceGroupName, siteName, subscriptionId` | Deletes the specified network site. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all sites in the network service. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all sites in the network service in a subscription. |
