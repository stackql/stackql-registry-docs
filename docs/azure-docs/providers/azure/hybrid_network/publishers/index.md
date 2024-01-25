---
title: publishers
hide_title: false
hide_table_of_contents: false
keywords:
  - publishers
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
<tr><td><b>Name</b></td><td><code>publishers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.publishers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | publisher properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `publisherName, resourceGroupName, subscriptionId` | Gets information about the specified publisher. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the publishers in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all the publishers in a subscription. |
| `create_or_update` | `INSERT` | `publisherName, resourceGroupName, subscriptionId` | Creates or updates a publisher. |
| `delete` | `DELETE` | `publisherName, resourceGroupName, subscriptionId` | Deletes the specified publisher. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the publishers in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all the publishers in a subscription. |
| `update` | `EXEC` | `publisherName, resourceGroupName, subscriptionId` | Update a publisher resource. |
