---
title: monitoring_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - monitoring_schedules
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>monitoring_schedules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitoring_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>monitoring_schedules</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.monitoring_schedules</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>MonitoringScheduleArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the monitoring schedule.</td></tr>
<tr><td><code>MonitoringScheduleName</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>MonitoringScheduleConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>CreationTime</code></td><td><code>string</code></td><td>The time at which the schedule was created.</td></tr>
<tr><td><code>EndpointName</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>FailureReason</code></td><td><code>string</code></td><td>Contains the reason a monitoring job failed, if it failed.</td></tr>
<tr><td><code>LastModifiedTime</code></td><td><code>string</code></td><td>A timestamp that indicates the last time the monitoring job was modified.</td></tr>
<tr><td><code>LastMonitoringExecutionSummary</code></td><td><code>undefined</code></td><td>Describes metadata on the last execution to run, if there was one.</td></tr>
<tr><td><code>MonitoringScheduleStatus</code></td><td><code>string</code></td><td>The status of a schedule job.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.sagemaker.monitoring_schedules<br/>WHERE region = 'us-east-1'
</pre>
