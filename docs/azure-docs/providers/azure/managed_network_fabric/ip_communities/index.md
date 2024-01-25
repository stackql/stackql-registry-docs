---
title: ip_communities
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_communities
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>ip_communities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.ip_communities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | IP Community Properties defines the resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `ipCommunityName, resourceGroupName, subscriptionId` | Implements an IP Community GET method. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Implements IP Communities list by resource group GET method. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Implements IP Communities list by subscription GET method. |
| `create` | `INSERT` | `ipCommunityName, resourceGroupName, subscriptionId, data__properties` | Implements an IP Community PUT method. |
| `delete` | `DELETE` | `ipCommunityName, resourceGroupName, subscriptionId` | Implements IP Community DELETE method. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Implements IP Communities list by resource group GET method. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Implements IP Communities list by subscription GET method. |
| `update` | `EXEC` | `ipCommunityName, resourceGroupName, subscriptionId` | API to update certain properties of the IP Community resource. |
