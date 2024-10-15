---
title: billing_hub_service_free_hour_balances
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_hub_service_free_hour_balances
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

Creates, updates, deletes, gets or lists a <code>billing_hub_service_free_hour_balances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_hub_service_free_hour_balances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.billing_hub_service_free_hour_balances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="incrementEntries" /> | `array` |  |
| <CopyableCode code="totalRemainingFreeHours" /> | `number` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> |  |

## `SELECT` examples




```sql
SELECT
incrementEntries,
totalRemainingFreeHours
FROM azure_extras.test_base.billing_hub_service_free_hour_balances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```