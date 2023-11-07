---
title: alarms
hide_title: false
hide_table_of_contents: false
keywords:
  - alarms
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
Retrieves a list of <code>alarms</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.cloudwatch.alarms</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ThresholdMetricId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EvaluateLowSampleCountPercentile</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ExtendedStatistic</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ComparisonOperator</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>TreatMissingData</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Dimensions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Period</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>EvaluationPeriods</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Unit</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Namespace</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>OKActions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>AlarmActions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>MetricName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ActionsEnabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>Metrics</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>AlarmDescription</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AlarmName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Statistic</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>InsufficientDataActions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DatapointsToAlarm</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Threshold</code></td><td><code>number</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.cloudwatch.alarms
WHERE region = 'us-east-1'
</pre>
