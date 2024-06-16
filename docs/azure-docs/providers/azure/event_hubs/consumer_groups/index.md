---
title: consumer_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - consumer_groups
  - event_hubs
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
<tr><td><b>Name</b></td><td><code>consumer_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_hubs.consumer_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `` | Single item in List or Get Consumer group operation |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="consumerGroupName, eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Gets a description for the specified consumer group. |
| <CopyableCode code="list_by_event_hub" /> | `SELECT` | <CopyableCode code="eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Gets all the consumer groups in a Namespace. An empty feed is returned if no consumer group exists in the Namespace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="consumerGroupName, eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Creates or updates an Event Hubs consumer group as a nested resource within a Namespace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="consumerGroupName, eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Deletes a consumer group from the specified Event Hub and resource group. |
