---
title: volumes_by_metric_name
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes_by_metric_name
  - metrics
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes_by_metric_name</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.metrics.volumes_by_metric_name" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The metric name for this resource. |
| <CopyableCode code="MetricIngestedIndexedVolume_attributes" /> | `object` | Object containing the definition of a metric's ingested and indexed volume. |
| <CopyableCode code="MetricIngestedIndexedVolume_id" /> | `string` | The metric name for this resource. |
| <CopyableCode code="MetricIngestedIndexedVolume_type" /> | `string` | The metric ingested and indexed volume type. |
| <CopyableCode code="attributes" /> | `object` | Object containing the definition of a metric's distinct volume. |
| <CopyableCode code="type" /> | `string` | The metric distinct volume type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_volumes_by_metric_name" /> | `SELECT` | <CopyableCode code="metric_name, dd_site" /> |
| <CopyableCode code="_list_volumes_by_metric_name" /> | `EXEC` | <CopyableCode code="metric_name, dd_site" /> |
