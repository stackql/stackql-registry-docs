---
title: ip_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_prefixes
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
<tr><td><b>Name</b></td><td><code>ip_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.ip_prefixes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | IP Prefix Properties defines the properties of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `ipPrefixName, resourceGroupName, subscriptionId` | Implements IP Prefix GET method. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Implements IpPrefixes list by resource group GET method. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Implements IpPrefixes list by subscription GET method. |
| `create` | `INSERT` | `ipPrefixName, resourceGroupName, subscriptionId, data__location, data__properties` | Implements IP Prefix PUT method. |
| `delete` | `DELETE` | `ipPrefixName, resourceGroupName, subscriptionId` | Implements IP Prefix DELETE method. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Implements IpPrefixes list by resource group GET method. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Implements IpPrefixes list by subscription GET method. |
| `update` | `EXEC` | `ipPrefixName, resourceGroupName, subscriptionId` | API to update certain properties of the IP Prefix resource. |
