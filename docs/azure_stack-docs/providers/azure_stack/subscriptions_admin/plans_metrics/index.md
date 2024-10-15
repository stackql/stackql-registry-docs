---
title: plans_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - plans_metrics
  - subscriptions_admin
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

Creates, updates, deletes, gets or lists a <code>plans_metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>plans_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.plans_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endTime" /> | `string` | End time of the metric. |
| <CopyableCode code="metricUnit" /> | `string` | The resource metric unit. |
| <CopyableCode code="metricValues" /> | `array` | List of metric values. |
| <CopyableCode code="startTime" /> | `string` | Start time of the metric. |
| <CopyableCode code="timeGrain" /> | `string` | Timespan of the metric. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="plan, resourceGroupName, subscriptionId" /> | Get the metrics of the specified plan. |

## `SELECT` examples

Get the metrics of the specified plan.


```sql
SELECT
endTime,
metricUnit,
metricValues,
startTime,
timeGrain
FROM azure_stack.subscriptions_admin.plans_metrics
WHERE plan = '{{ plan }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```