---
title: domain_event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_event_subscriptions
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
<tr><td><b>Name</b></td><td><code>domain_event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.domain_event_subscriptions" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, eventSubscriptionName, resourceGroupName, subscriptionId" /> | Get properties of an event subscription of a domain. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | List all event subscriptions that have been created for a specific topic. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainName, eventSubscriptionName, resourceGroupName, subscriptionId" /> | Asynchronously creates a new event subscription or updates an existing event subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainName, eventSubscriptionName, resourceGroupName, subscriptionId" /> | Delete an existing event subscription for a domain. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="domainName, eventSubscriptionName, resourceGroupName, subscriptionId" /> | Update an existing event subscription for a topic. |
