---
title: event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - event_subscriptions
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
<tr><td><b>Name</b></td><td><code>event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.event_subscriptions" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="eventSubscriptionName, scope" /> | Get properties of an event subscription. |
| <CopyableCode code="list_by_domain_topic" /> | `SELECT` | <CopyableCode code="domainName, resourceGroupName, subscriptionId, topicName" /> | List all event subscriptions that have been created for a specific domain topic. |
| <CopyableCode code="list_by_resource" /> | `SELECT` | <CopyableCode code="providerNamespace, resourceGroupName, resourceName, resourceTypeName, subscriptionId" /> | List all event subscriptions that have been created for a specific resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="eventSubscriptionName, scope" /> | Asynchronously creates a new event subscription or updates an existing event subscription based on the specified scope. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="eventSubscriptionName, scope" /> | Delete an existing event subscription. |
| <CopyableCode code="_list_by_domain_topic" /> | `EXEC` | <CopyableCode code="domainName, resourceGroupName, subscriptionId, topicName" /> | List all event subscriptions that have been created for a specific domain topic. |
| <CopyableCode code="_list_by_resource" /> | `EXEC` | <CopyableCode code="providerNamespace, resourceGroupName, resourceName, resourceTypeName, subscriptionId" /> | List all event subscriptions that have been created for a specific resource. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="eventSubscriptionName, scope" /> | Asynchronously updates an existing event subscription. |
