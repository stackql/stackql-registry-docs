---
title: alarm
hide_title: false
hide_table_of_contents: false
keywords:
  - alarm
  - cloudwatch
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>alarm</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarm</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>alarm</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudwatch.alarm</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>threshold_metric_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>evaluate_low_sample_count_percentile</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>extended_statistic</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>comparison_operator</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>treat_missing_data</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dimensions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>period</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>evaluation_periods</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>unit</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>namespace</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>o_kactions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>alarm_actions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>metric_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>actions_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>metrics</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>alarm_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>alarm_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>statistic</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>insufficient_data_actions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>datapoints_to_alarm</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>threshold</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
threshold_metric_id,
evaluate_low_sample_count_percentile,
extended_statistic,
comparison_operator,
treat_missing_data,
dimensions,
period,
evaluation_periods,
unit,
namespace,
o_kactions,
alarm_actions,
metric_name,
actions_enabled,
metrics,
alarm_description,
alarm_name,
statistic,
insufficient_data_actions,
id,
arn,
datapoints_to_alarm,
threshold
FROM aws.cloudwatch.alarm
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
