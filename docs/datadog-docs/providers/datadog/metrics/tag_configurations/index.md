---
title: tag_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_configurations
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
<tr><td><b>Name</b></td><td><code>tag_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.metrics.tag_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The metric name for this resource. |
| <CopyableCode code="MetricTagConfiguration_id" /> | `string` | The metric name for this resource. |
| <CopyableCode code="MetricTagConfiguration_type" /> | `string` | The metric tag configuration resource type. |
| <CopyableCode code="attributes" /> | `object` | Object containing the definition of a metric tag configuration attributes. |
| <CopyableCode code="type" /> | `string` | The metric resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_tag_configurations" /> | `SELECT` | <CopyableCode code="dd_site" /> | Returns all metrics that can be configured in the Metrics Summary page or with Metrics without Limits™ (matching additional filters if specified). |
| <CopyableCode code="create_tag_configuration" /> | `INSERT` | <CopyableCode code="metric_name, data__data, dd_site" /> | Create and define a list of queryable tag keys for an existing count/gauge/rate/distribution metric.<br />Optionally, include percentile aggregations on any distribution metric or configure custom aggregations<br />on any count, rate, or gauge metric. By setting `exclude_tags_mode` to true the behavior is changed<br />from an allow-list to a deny-list, and tags in the defined list will not be queryable.<br />Can only be used with application keys of users with the `Manage Tags for Metrics` permission. |
| <CopyableCode code="delete_tag_configuration" /> | `DELETE` | <CopyableCode code="metric_name, dd_site" /> | Deletes a metric's tag configuration. Can only be used with application<br />keys from users with the `Manage Tags for Metrics` permission. |
| <CopyableCode code="_list_tag_configurations" /> | `EXEC` | <CopyableCode code="dd_site" /> | Returns all metrics that can be configured in the Metrics Summary page or with Metrics without Limits™ (matching additional filters if specified). |
| <CopyableCode code="update_tag_configuration" /> | `EXEC` | <CopyableCode code="metric_name, data__data, dd_site" /> | Update the tag configuration of a metric or percentile aggregations of a distribution metric or custom aggregations<br />of a count, rate, or gauge metric. By setting `exclude_tags_mode` to true the behavior is changed<br />from an allow-list to a deny-list, and tags in the defined list will not be queryable.<br />Can only be used with application keys from users with the `Manage Tags for Metrics` permission. This endpoint requires<br />a tag configuration to be created first. |
