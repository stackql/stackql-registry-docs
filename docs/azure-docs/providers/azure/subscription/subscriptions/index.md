---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - subscription
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
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.subscription.subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified ID for the subscription. For example, /subscriptions/00000000-0000-0000-0000-000000000000. |
| <CopyableCode code="authorizationSource" /> | `string` | The authorization source of the request. Valid values are one or more combinations of Legacy, RoleBased, Bypassed, Direct and Management. For example, 'Legacy, RoleBased'. |
| <CopyableCode code="displayName" /> | `string` | The subscription display name. |
| <CopyableCode code="state" /> | `string` | The subscription state. Possible values are Enabled, Warned, PastDue, Disabled, and Deleted. |
| <CopyableCode code="subscriptionId" /> | `string` | The subscription ID. |
| <CopyableCode code="subscriptionPolicies" /> | `object` | Subscription policies. |
| <CopyableCode code="tags" /> | `object` | Tags for the subscription |
| <CopyableCode code="tenantId" /> | `string` | The tenant ID. For example, 00000000-0000-0000-0000-000000000000. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets details about a specified subscription. |
| <CopyableCode code="list" /> | `SELECT` |  | Gets all subscriptions for a tenant. |
