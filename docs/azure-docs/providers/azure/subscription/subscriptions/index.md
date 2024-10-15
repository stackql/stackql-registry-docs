---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - subscription
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>subscriptions</code> resource.

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
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Gets all subscriptions for a tenant. |
| <CopyableCode code="accept_ownership" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Accept subscription ownership. |
| <CopyableCode code="accept_ownership_status" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Accept subscription ownership status. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | The operation to cancel a subscription |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | The operation to enable a subscription |
| <CopyableCode code="rename" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | The operation to rename a subscription |

## `SELECT` examples

Gets all subscriptions for a tenant.


```sql
SELECT
id,
authorizationSource,
displayName,
state,
subscriptionId,
subscriptionPolicies,
tags,
tenantId
FROM azure.subscription.subscriptions
;
```