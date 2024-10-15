---
title: plans_metric_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - plans_metric_definitions
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

Creates, updates, deletes, gets or lists a <code>plans_metric_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>plans_metric_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.plans_metric_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Metric definition name. |
| <CopyableCode code="metricAvailabilities" /> | `array` | List of metric definitions. |
| <CopyableCode code="primaryAggregationType" /> | `string` | The primary aggregation type for resource metric. |
| <CopyableCode code="unit" /> | `string` | The resource metric unit. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="plan, resourceGroupName, subscriptionId" /> | Get the metric definitions of the specified plan. |

## `SELECT` examples

Get the metric definitions of the specified plan.


```sql
SELECT
name,
metricAvailabilities,
primaryAggregationType,
unit
FROM azure_stack.subscriptions_admin.plans_metric_definitions
WHERE plan = '{{ plan }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```