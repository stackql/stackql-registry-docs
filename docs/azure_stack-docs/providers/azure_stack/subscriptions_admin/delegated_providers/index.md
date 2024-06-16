---
title: delegated_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_providers
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
<tr><td><b>Name</b></td><td><code>delegated_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.delegated_providers" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="delegatedProvider, subscriptionId" /> | Get the specified delegated provider. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get the list of delegatedProviders. |
