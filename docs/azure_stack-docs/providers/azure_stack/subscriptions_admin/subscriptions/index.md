---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - subscriptions_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier. |
| <CopyableCode code="delegatedProviderSubscriptionId" /> | `string` | Parent DelegatedProvider subscription identifier. |
| <CopyableCode code="displayName" /> | `string` | Subscription name. |
| <CopyableCode code="externalReferenceId" /> | `string` | External reference identifier. |
| <CopyableCode code="offerId" /> | `string` | Identifier of the offer under the scope of a delegated provider. |
| <CopyableCode code="owner" /> | `string` | Subscription owner. |
| <CopyableCode code="routingResourceManagerType" /> | `string` | Resource manager type. |
| <CopyableCode code="state" /> | `string` | Subscription notification state. |
| <CopyableCode code="subscriptionId" /> | `string` | Subscription identifier. |
| <CopyableCode code="tenantId" /> | `string` | Directory tenant identifier. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId, targetSubscriptionId" /> | Get a specified subscription. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get the list of subscriptions. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="subscriptionId, targetSubscriptionId" /> | Creates or updates the specified subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="subscriptionId, targetSubscriptionId" /> | Delete the specified subscription. |
| <CopyableCode code="check_identity_health" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Checks the identity health |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Get the list of subscriptions. |
| <CopyableCode code="move_subscriptions" /> | `EXEC` | <CopyableCode code="subscriptionId, data__resources" /> | Move subscriptions between delegated provider offers. |
| <CopyableCode code="restore_data" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Restores the data |
| <CopyableCode code="validate_move_subscriptions" /> | `EXEC` | <CopyableCode code="subscriptionId, data__resources" /> | Validate that user subscriptions can be moved between delegated provider offers. |
