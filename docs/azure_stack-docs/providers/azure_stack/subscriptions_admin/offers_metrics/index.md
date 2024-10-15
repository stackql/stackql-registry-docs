---
title: offers_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - offers_metrics
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

Creates, updates, deletes, gets or lists a <code>offers_metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>offers_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.offers_metrics" /></td></tr>
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
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="offer, resourceGroupName, subscriptionId" /> | Get the offer metrics. |

## `SELECT` examples

Get the offer metrics.


```sql
SELECT
endTime,
metricUnit,
metricValues,
startTime,
timeGrain
FROM azure_stack.subscriptions_admin.offers_metrics
WHERE offer = '{{ offer }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```