---
title: ip_extended_communities
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_extended_communities
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
<tr><td><b>Name</b></td><td><code>ip_extended_communities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.ip_extended_communities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | IP Extended Community Properties defines the resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `ipExtendedCommunityName, resourceGroupName, subscriptionId` | Implements IP Extended Community GET method. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Implements IpExtendedCommunities list by resource group GET method. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Implements IpExtendedCommunities list by subscription GET method. |
| `create` | `INSERT` | `ipExtendedCommunityName, resourceGroupName, subscriptionId, data__properties` | Implements IP Extended Community PUT method. |
| `delete` | `DELETE` | `ipExtendedCommunityName, resourceGroupName, subscriptionId` | Implements IP Extended Community DELETE method. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Implements IpExtendedCommunities list by resource group GET method. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Implements IpExtendedCommunities list by subscription GET method. |
| `update` | `EXEC` | `ipExtendedCommunityName, resourceGroupName, subscriptionId` | API to update certain properties of the IP Extended Community resource. |
