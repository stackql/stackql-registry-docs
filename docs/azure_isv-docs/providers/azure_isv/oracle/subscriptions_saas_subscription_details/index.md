---
title: subscriptions_saas_subscription_details
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions_saas_subscription_details
  - oracle
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

Creates, updates, deletes, gets or lists a <code>subscriptions_saas_subscription_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions_saas_subscription_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.subscriptions_saas_subscription_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Purchased SaaS subscription ID |
| <CopyableCode code="isAutoRenew" /> | `boolean` | AutoRenew flag |
| <CopyableCode code="isFreeTrial" /> | `boolean` | FreeTrial flag |
| <CopyableCode code="offerId" /> | `string` | Purchased offer ID |
| <CopyableCode code="planId" /> | `string` | Purchased offer's plan ID |
| <CopyableCode code="publisherId" /> | `string` | Publisher ID |
| <CopyableCode code="purchaserEmailId" /> | `string` | Purchaser Email ID |
| <CopyableCode code="purchaserTenantId" /> | `string` | Purchaser Tenant ID |
| <CopyableCode code="saasSubscriptionStatus" /> | `string` | Indicates the status of the Subscription. |
| <CopyableCode code="subscriptionName" /> | `string` | SaaS subscription name |
| <CopyableCode code="termUnit" /> | `string` | Purchase Term Unit |
| <CopyableCode code="timeCreated" /> | `string` | Creation Date and Time |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Saas Subscription Details |

## `SELECT` examples

List Saas Subscription Details


```sql
SELECT
id,
isAutoRenew,
isFreeTrial,
offerId,
planId,
publisherId,
purchaserEmailId,
purchaserTenantId,
saasSubscriptionStatus,
subscriptionName,
termUnit,
timeCreated
FROM azure_isv.oracle.subscriptions_saas_subscription_details
WHERE subscriptionId = '{{ subscriptionId }}';
```