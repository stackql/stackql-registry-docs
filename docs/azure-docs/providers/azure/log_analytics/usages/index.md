---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - log_analytics
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

Creates, updates, deletes, gets or lists a <code>usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | The name of a metric. |
| <CopyableCode code="currentValue" /> | `number` | The current value of the metric. |
| <CopyableCode code="limit" /> | `number` | The quota limit for the metric. |
| <CopyableCode code="nextResetTime" /> | `string` | The time that the metric's value will reset. |
| <CopyableCode code="quotaPeriod" /> | `string` | The quota period that determines the length of time between value resets. |
| <CopyableCode code="unit" /> | `string` | The units used for the metric. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets a list of usage metrics for a workspace. |

## `SELECT` examples

Gets a list of usage metrics for a workspace.


```sql
SELECT
name,
currentValue,
limit,
nextResetTime,
quotaPeriod,
unit
FROM azure.log_analytics.usages
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```