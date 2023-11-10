---
title: anomaly_monitor
hide_title: false
hide_table_of_contents: false
keywords:
  - anomaly_monitor
  - ce
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>anomaly_monitor</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_monitor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>anomaly_monitor</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ce.anomaly_monitor</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>monitor_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>monitor_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>monitor_name</code></td><td><code>string</code></td><td>The name of the monitor.</td></tr>
<tr><td><code>creation_date</code></td><td><code>string</code></td><td>The date when the monitor was created. </td></tr>
<tr><td><code>last_evaluated_date</code></td><td><code>string</code></td><td>The date when the monitor last evaluated for anomalies.</td></tr>
<tr><td><code>last_updated_date</code></td><td><code>string</code></td><td>The date when the monitor was last updated.</td></tr>
<tr><td><code>monitor_dimension</code></td><td><code>string</code></td><td>The dimensions to evaluate</td></tr>
<tr><td><code>monitor_specification</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dimensional_value_count</code></td><td><code>integer</code></td><td>The value for evaluated dimensions.</td></tr>
<tr><td><code>resource_tags</code></td><td><code>array</code></td><td>Tags to assign to monitor.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
monitor_arn,
monitor_type,
monitor_name,
creation_date,
last_evaluated_date,
last_updated_date,
monitor_dimension,
monitor_specification,
dimensional_value_count,
resource_tags
FROM aws.ce.anomaly_monitor
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;MonitorArn&gt;'
```
