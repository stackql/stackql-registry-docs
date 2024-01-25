---
title: partner_destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_destinations
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
<tr><td><b>Name</b></td><td><code>partner_destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.partner_destinations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the Partner Destination. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `partnerDestinationName, resourceGroupName, subscriptionId` | Get properties of a partner destination. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all the partner destinations under a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all the partner destinations under an Azure subscription. |
| `create_or_update` | `INSERT` | `partnerDestinationName, resourceGroupName, subscriptionId` | Asynchronously creates a new partner destination with the specified parameters. |
| `delete` | `DELETE` | `partnerDestinationName, resourceGroupName, subscriptionId` | Delete existing partner destination. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all the partner destinations under a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all the partner destinations under an Azure subscription. |
| `activate` | `EXEC` | `partnerDestinationName, resourceGroupName, subscriptionId` | Activate a newly created partner destination. |
| `update` | `EXEC` | `partnerDestinationName, resourceGroupName, subscriptionId` | Asynchronously updates a partner destination with the specified parameters. |
