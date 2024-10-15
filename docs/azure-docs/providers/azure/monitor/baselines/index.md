---
title: baselines
hide_title: false
hide_table_of_contents: false
keywords:
  - baselines
  - monitor
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

Creates, updates, deletes, gets or lists a <code>baselines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>baselines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.baselines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The metric baseline Id. |
| <CopyableCode code="name" /> | `string` | The name of the metric for which the baselines were retrieved. |
| <CopyableCode code="properties" /> | `object` | The response to a metric baselines query. |
| <CopyableCode code="type" /> | `string` | The resource type of the metric baseline resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="interval, metricName, resourceUri, timespan" /> | **Lists the metric baseline values for a resource**. |

## `SELECT` examples

**Lists the metric baseline values for a resource**.


```sql
SELECT
id,
name,
properties,
type
FROM azure.monitor.baselines
WHERE interval = '{{ interval }}'
AND metricName = '{{ metricName }}'
AND resourceUri = '{{ resourceUri }}'
AND timespan = '{{ timespan }}';
```