---
title: partner_topic_event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_topic_event_subscriptions
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
<tr><td><b>Name</b></td><td><code>partner_topic_event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.partner_topic_event_subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the Event Subscription. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId" /> | Get properties of an event subscription of a partner topic. |
| <CopyableCode code="list_by_partner_topic" /> | `SELECT` | <CopyableCode code="partnerTopicName, resourceGroupName, subscriptionId" /> | List event subscriptions that belong to a specific partner topic. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId" /> | Asynchronously creates or updates an event subscription of a partner topic with the specified parameters. Existing event subscriptions will be updated with this API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId" /> | Delete an existing event subscription of a partner topic. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId" /> | Update an existing event subscription of a partner topic. |
