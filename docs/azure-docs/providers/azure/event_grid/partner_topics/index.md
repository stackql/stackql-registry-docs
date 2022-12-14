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
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Tags of the resource. |
| `identity` | `object` | The identity information for the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties of the Partner Topic. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PartnerTopics_Get` | `SELECT` | `partnerTopicName, resourceGroupName, subscriptionId` | Get properties of a partner topic. |
| `PartnerTopics_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the partner topics under a resource group. |
| `PartnerTopics_ListBySubscription` | `SELECT` | `subscriptionId` | List all the partner topics under an Azure subscription. |
| `PartnerTopics_CreateOrUpdate` | `INSERT` | `partnerTopicName, resourceGroupName, subscriptionId` | Asynchronously creates a new partner topic with the specified parameters. |
| `PartnerTopics_Delete` | `DELETE` | `partnerTopicName, resourceGroupName, subscriptionId` | Delete existing partner topic. |
| `PartnerTopics_Activate` | `EXEC` | `partnerTopicName, resourceGroupName, subscriptionId` | Activate a newly created partner topic. |
| `PartnerTopics_Deactivate` | `EXEC` | `partnerTopicName, resourceGroupName, subscriptionId` | Deactivate specific partner topic. |
| `PartnerTopics_Update` | `EXEC` | `partnerTopicName, resourceGroupName, subscriptionId` | Asynchronously updates a partner topic with the specified parameters. |
