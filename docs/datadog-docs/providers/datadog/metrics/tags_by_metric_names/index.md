---
title: tags_by_metric_names
hide_title: false
hide_table_of_contents: false
keywords:
  - tags_by_metric_names
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
<tr><td><b>Name</b></td><td><code>tags_by_metric_names</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.metrics.tags_by_metric_names" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The metric name for this resource. |
| <CopyableCode code="attributes" /> | `object` | Object containing the definition of a metric's tags. |
| <CopyableCode code="type" /> | `string` | The metric resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_tags_by_metric_name" /> | `SELECT` | <CopyableCode code="metric_name, dd_site" /> |
| <CopyableCode code="_list_tags_by_metric_name" /> | `EXEC` | <CopyableCode code="metric_name, dd_site" /> |
