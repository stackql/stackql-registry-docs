---
title: log_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - log_metrics
  - log_metrics
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
<tr><td><b>Name</b></td><td><code>log_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.log_metrics.log_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The name of the log-based metric. |
| <CopyableCode code="attributes" /> | `object` | The object describing a Datadog log-based metric. |
| <CopyableCode code="type" /> | `string` | The type of the resource. The value should always be logs_metrics. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_logs_metric" /> | `SELECT` | <CopyableCode code="metric_id, dd_site" /> | Get a specific log-based metric from your organization. |
| <CopyableCode code="list_logs_metrics" /> | `SELECT` | <CopyableCode code="dd_site" /> | Get the list of configured log-based metrics with their definitions. |
| <CopyableCode code="create_logs_metric" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create a metric based on your ingested logs in your organization.<br />Returns the log-based metric object from the request body when the request is successful. |
| <CopyableCode code="delete_logs_metric" /> | `DELETE` | <CopyableCode code="metric_id, dd_site" /> | Delete a specific log-based metric from your organization. |
| <CopyableCode code="_get_logs_metric" /> | `EXEC` | <CopyableCode code="metric_id, dd_site" /> | Get a specific log-based metric from your organization. |
| <CopyableCode code="_list_logs_metrics" /> | `EXEC` | <CopyableCode code="dd_site" /> | Get the list of configured log-based metrics with their definitions. |
| <CopyableCode code="update_logs_metric" /> | `EXEC` | <CopyableCode code="metric_id, data__data, dd_site" /> | Update a specific log-based metric from your organization.<br />Returns the log-based metric object from the request body when the request is successful. |
