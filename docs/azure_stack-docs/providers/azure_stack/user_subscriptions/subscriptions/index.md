---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - user_subscriptions
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.user_subscriptions.subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier. |
| <CopyableCode code="displayName" /> | `string` | Subscription name. |
| <CopyableCode code="offerId" /> | `string` | Identifier of the offer under the scope of a delegated provider. |
| <CopyableCode code="state" /> | `string` | Subscription notification state. |
| <CopyableCode code="subscriptionId" /> | `string` | Subscription identifier. |
| <CopyableCode code="tenantId" /> | `string` | Directory tenant identifier. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets details about particular subscription. |
| <CopyableCode code="list" /> | `SELECT` |  | Get the list of subscriptions. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="subscriptionId" /> | Create or updates a subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="subscriptionId" /> | Delete the specified subscription. |
| <CopyableCode code="_list" /> | `EXEC` |  | Get the list of subscriptions. |
