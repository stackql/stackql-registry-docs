---
title: partner_topics
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_topics
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
<tr><td><b>Name</b></td><td><code>partner_topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.partner_topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | The identity information for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the Partner Topic. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `partnerTopicName, resourceGroupName, subscriptionId` | Get properties of a partner topic. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all the partner topics under a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all the partner topics under an Azure subscription. |
| `create_or_update` | `INSERT` | `partnerTopicName, resourceGroupName, subscriptionId` | Asynchronously creates a new partner topic with the specified parameters. |
| `delete` | `DELETE` | `partnerTopicName, resourceGroupName, subscriptionId` | Delete existing partner topic. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all the partner topics under a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all the partner topics under an Azure subscription. |
| `activate` | `EXEC` | `partnerTopicName, resourceGroupName, subscriptionId` | Activate a newly created partner topic. |
| `deactivate` | `EXEC` | `partnerTopicName, resourceGroupName, subscriptionId` | Deactivate specific partner topic. |
| `update` | `EXEC` | `partnerTopicName, resourceGroupName, subscriptionId` | Asynchronously updates a partner topic with the specified parameters. |
