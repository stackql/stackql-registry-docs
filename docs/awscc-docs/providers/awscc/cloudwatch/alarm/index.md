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
<tr><td><b>Id</b></td><td><code>awscc.cloudwatch.alarm</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>threshold_metric_id</code></td><td><code>string</code></td><td>In an alarm based on an anomaly detection model, this is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.</td></tr>
<tr><td><code>evaluate_low_sample_count_percentile</code></td><td><code>string</code></td><td>Used only for alarms based on percentiles.</td></tr>
<tr><td><code>extended_statistic</code></td><td><code>string</code></td><td>The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.</td></tr>
<tr><td><code>comparison_operator</code></td><td><code>string</code></td><td>The arithmetic operation to use when comparing the specified statistic and threshold.</td></tr>
<tr><td><code>treat_missing_data</code></td><td><code>string</code></td><td>Sets how this alarm is to handle missing data points. Valid values are breaching, notBreaching, ignore, and missing.</td></tr>
<tr><td><code>dimensions</code></td><td><code>array</code></td><td>The dimensions for the metric associated with the alarm. For an alarm based on a math expression, you can't specify Dimensions. Instead, you use Metrics.</td></tr>
<tr><td><code>period</code></td><td><code>integer</code></td><td>The period in seconds, over which the statistic is applied.</td></tr>
<tr><td><code>evaluation_periods</code></td><td><code>integer</code></td><td>The number of periods over which data is compared to the specified threshold.</td></tr>
<tr><td><code>unit</code></td><td><code>string</code></td><td>The unit of the metric associated with the alarm.</td></tr>
<tr><td><code>namespace</code></td><td><code>string</code></td><td>The namespace of the metric associated with the alarm.</td></tr>
<tr><td><code>o_kactions</code></td><td><code>array</code></td><td>The actions to execute when this alarm transitions to the OK state from any other state.</td></tr>
<tr><td><code>alarm_actions</code></td><td><code>array</code></td><td>The list of actions to execute when this alarm transitions into an ALARM state from any other state.</td></tr>
<tr><td><code>metric_name</code></td><td><code>string</code></td><td>The name of the metric associated with the alarm.</td></tr>
<tr><td><code>actions_enabled</code></td><td><code>boolean</code></td><td>Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.</td></tr>
<tr><td><code>metrics</code></td><td><code>array</code></td><td>An array that enables you to create an alarm based on the result of a metric math expression.</td></tr>
<tr><td><code>alarm_description</code></td><td><code>string</code></td><td>The description of the alarm.</td></tr>
<tr><td><code>alarm_name</code></td><td><code>string</code></td><td>The name of the alarm.</td></tr>
<tr><td><code>statistic</code></td><td><code>string</code></td><td>The statistic for the metric associated with the alarm, other than percentile.</td></tr>
<tr><td><code>insufficient_data_actions</code></td><td><code>array</code></td><td>The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Amazon Resource Name is a unique name for each resource.</td></tr>
<tr><td><code>datapoints_to_alarm</code></td><td><code>integer</code></td><td>The number of datapoints that must be breaching to trigger the alarm.</td></tr>
<tr><td><code>threshold</code></td><td><code>number</code></td><td>In an alarm based on an anomaly detection model, this is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>alarm</code> resource, the following permissions are required:

### Update
<pre>
cloudwatch:PutMetricAlarm,
cloudwatch:DescribeAlarms</pre>

### Delete
<pre>
cloudwatch:DeleteAlarms,
cloudwatch:DescribeAlarms</pre>

### Read
<pre>
cloudwatch:DescribeAlarms</pre>


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
arn,
datapoints_to_alarm,
threshold
FROM awscc.cloudwatch.alarm
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AlarmName&gt;'
```
