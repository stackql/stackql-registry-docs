---
title: active_metric_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - active_metric_configurations
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
<tr><td><b>Name</b></td><td><code>active_metric_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.metrics.active_metric_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The metric name for this resource. |
| <CopyableCode code="attributes" /> | `object` | Object containing the definition of a metric's actively queried tags and aggregations. |
| <CopyableCode code="type" /> | `string` | The metric actively queried configuration resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_active_metric_configurations" /> | `SELECT` | <CopyableCode code="metric_name, dd_site" /> | List tags and aggregations that are actively queried on dashboards and monitors for a given metric name. |
| <CopyableCode code="create_bulk_tags_metrics_configuration" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create and define a list of queryable tag keys for a set of existing count, gauge, rate, and distribution metrics.<br />Metrics are selected by passing a metric name prefix. Use the Delete method of this API path to remove tag configurations.<br />Results can be sent to a set of account email addresses, just like the same operation in the Datadog web app.<br />If multiple calls include the same metric, the last configuration applied (not by submit order) is used, do not<br />expect deterministic ordering of concurrent calls. The `exclude_tags_mode` value will set all metrics that match the prefix to<br />the same exclusion state, metric tag configurations do not support mixed inclusion and exclusion for tags on the same metric.<br />Can only be used with application keys of users with the `Manage Tags for Metrics` permission. |
| <CopyableCode code="delete_bulk_tags_metrics_configuration" /> | `DELETE` | <CopyableCode code="data__data, dd_site" /> | Delete all custom lists of queryable tag keys for a set of existing count, gauge, rate, and distribution metrics.<br />Metrics are selected by passing a metric name prefix.<br />Results can be sent to a set of account email addresses, just like the same operation in the Datadog web app.<br />Can only be used with application keys of users with the `Manage Tags for Metrics` permission. |
| <CopyableCode code="_list_active_metric_configurations" /> | `EXEC` | <CopyableCode code="metric_name, dd_site" /> | List tags and aggregations that are actively queried on dashboards and monitors for a given metric name. |
