---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - event_grid
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
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | The identity information for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the Event Grid Domain Resource. |
| `sku` | `object` | Describes an EventGrid Resource Sku. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `domainName, resourceGroupName, subscriptionId` | Get properties of a domain. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all the domains under a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all the domains under an Azure subscription. |
| `create_or_update` | `INSERT` | `domainName, resourceGroupName, subscriptionId` | Asynchronously creates or updates a new domain with the specified parameters. |
| `delete` | `DELETE` | `domainName, resourceGroupName, subscriptionId` | Delete existing domain. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all the domains under a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all the domains under an Azure subscription. |
| `regenerate_key` | `EXEC` | `domainName, resourceGroupName, subscriptionId, data__keyName` | Regenerate a shared access key for a domain. |
| `update` | `EXEC` | `domainName, resourceGroupName, subscriptionId` | Asynchronously updates a domain with the specified parameters. |
