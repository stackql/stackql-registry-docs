---
title: topic_event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - topic_event_subscriptions
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
<tr><td><b>Name</b></td><td><code>topic_event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.topic_event_subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the Event Subscription. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="eventSubscriptionName, resourceGroupName, subscriptionId, topicName" /> | Get properties of an event subscription of a topic. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, topicName" /> | List all event subscriptions that have been created for a specific topic. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="eventSubscriptionName, resourceGroupName, subscriptionId, topicName" /> | Asynchronously creates a new event subscription or updates an existing event subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="eventSubscriptionName, resourceGroupName, subscriptionId, topicName" /> | Delete an existing event subscription for a topic. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, topicName" /> | List all event subscriptions that have been created for a specific topic. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="eventSubscriptionName, resourceGroupName, subscriptionId, topicName" /> | Update an existing event subscription for a topic. |
