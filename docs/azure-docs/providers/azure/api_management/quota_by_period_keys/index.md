---
title: quota_by_period_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - quota_by_period_keys
  - api_management
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

Creates, updates, deletes, gets or lists a <code>quota_by_period_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quota_by_period_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.quota_by_period_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="counterKey" /> | `string` | The Key value of the Counter. Must not be empty. |
| <CopyableCode code="periodEndTime" /> | `string` | The date of the end of Counter Period. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard. |
| <CopyableCode code="periodKey" /> | `string` | Identifier of the Period for which the counter was collected. Must not be empty. |
| <CopyableCode code="periodStartTime" /> | `string` | The date of the start of Counter Period. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard. |
| <CopyableCode code="value" /> | `object` | Quota counter value details. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="quotaCounterKey, quotaPeriodKey, resourceGroupName, serviceName, subscriptionId" /> | Gets the value of the quota counter associated with the counter-key in the policy for the specific period in service instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="quotaCounterKey, quotaPeriodKey, resourceGroupName, serviceName, subscriptionId" /> | Updates an existing quota counter value in the specified service instance. |

## `SELECT` examples

Gets the value of the quota counter associated with the counter-key in the policy for the specific period in service instance.


```sql
SELECT
counterKey,
periodEndTime,
periodKey,
periodStartTime,
value
FROM azure.api_management.quota_by_period_keys
WHERE quotaCounterKey = '{{ quotaCounterKey }}'
AND quotaPeriodKey = '{{ quotaPeriodKey }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `UPDATE` example

Updates a <code>quota_by_period_keys</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.quota_by_period_keys
SET 
properties = '{{ properties }}'
WHERE 
quotaCounterKey = '{{ quotaCounterKey }}'
AND quotaPeriodKey = '{{ quotaPeriodKey }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
