---
title: event_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - event_hubs
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
<tr><td><b>Name</b></td><td><code>event_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_hubs.event_hubs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `` | Properties supplied to the Create Or Update Event Hub operation. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Gets an Event Hubs description for the specified Event Hub. |
| <CopyableCode code="list_by_namespace" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Gets all the Event Hubs in a Namespace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Creates or updates a new Event Hub as a nested resource within a Namespace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Deletes an Event Hub from the specified Namespace and resource group. |
| <CopyableCode code="regenerate_keys" /> | `EXEC` | <CopyableCode code="authorizationRuleName, eventHubName, namespaceName, resourceGroupName, subscriptionId, data__keyType" /> | Regenerates the ACS and SAS connection strings for the Event Hub. |
