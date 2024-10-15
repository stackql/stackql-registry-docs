---
title: billing_hub_service_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_hub_service_usages
  - test_base
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

Creates, updates, deletes, gets or lists a <code>billing_hub_service_usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_hub_service_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.billing_hub_service_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextRequest" /> | `object` |  |
| <CopyableCode code="packageUsageEntries" /> | `array` |  |
| <CopyableCode code="totalCharges" /> | `number` |  |
| <CopyableCode code="totalUsedBillableHours" /> | `number` |  |
| <CopyableCode code="totalUsedFreeHours" /> | `number` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName, data__endTimeStamp, data__startTimeStamp" /> |  |

## `SELECT` examples




```sql
SELECT
nextRequest,
packageUsageEntries,
totalCharges,
totalUsedBillableHours,
totalUsedFreeHours
FROM azure_extras.test_base.billing_hub_service_usages
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}'
AND data__endTimeStamp = '{{ data__endTimeStamp }}'
AND data__startTimeStamp = '{{ data__startTimeStamp }}';
```