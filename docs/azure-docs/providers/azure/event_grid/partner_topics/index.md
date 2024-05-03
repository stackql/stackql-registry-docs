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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partner_topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.partner_topics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | The identity information for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the Partner Topic. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="partnerTopicName, resourceGroupName, subscriptionId" /> | Get properties of a partner topic. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the partner topics under a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the partner topics under an Azure subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="partnerTopicName, resourceGroupName, subscriptionId" /> | Asynchronously creates a new partner topic with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="partnerTopicName, resourceGroupName, subscriptionId" /> | Delete existing partner topic. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the partner topics under a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List all the partner topics under an Azure subscription. |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="partnerTopicName, resourceGroupName, subscriptionId" /> | Activate a newly created partner topic. |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="partnerTopicName, resourceGroupName, subscriptionId" /> | Deactivate specific partner topic. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="partnerTopicName, resourceGroupName, subscriptionId" /> | Asynchronously updates a partner topic with the specified parameters. |
