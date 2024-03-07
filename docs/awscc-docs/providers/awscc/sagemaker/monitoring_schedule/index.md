---
title: monitoring_schedule
hide_title: false
hide_table_of_contents: false
keywords:
  - monitoring_schedule
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
Gets an individual <code>monitoring_schedule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitoring_schedule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>monitoring_schedule</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.monitoring_schedule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>monitoring_schedule_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the monitoring schedule.</td></tr>
<tr><td><code>monitoring_schedule_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>monitoring_schedule_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>The time at which the schedule was created.</td></tr>
<tr><td><code>endpoint_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>failure_reason</code></td><td><code>string</code></td><td>Contains the reason a monitoring job failed, if it failed.</td></tr>
<tr><td><code>last_modified_time</code></td><td><code>string</code></td><td>A timestamp that indicates the last time the monitoring job was modified.</td></tr>
<tr><td><code>last_monitoring_execution_summary</code></td><td><code>object</code></td><td>Describes metadata on the last execution to run, if there was one.</td></tr>
<tr><td><code>monitoring_schedule_status</code></td><td><code>string</code></td><td>The status of a schedule job.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
monitoring_schedule_arn,
monitoring_schedule_name,
monitoring_schedule_config,
tags,
creation_time,
endpoint_name,
failure_reason,
last_modified_time,
last_monitoring_execution_summary,
monitoring_schedule_status
FROM awscc.sagemaker.monitoring_schedule
WHERE region = 'us-east-1'
AND data__Identifier = '{MonitoringScheduleArn}';
```

## Permissions

To operate on the <code>monitoring_schedule</code> resource, the following permissions are required:

### Delete
```json
sagemaker:DeleteMonitoringSchedule,
sagemaker:DescribeMonitoringSchedule
```

### Read
```json
sagemaker:DescribeMonitoringSchedule
```

### Update
```json
sagemaker:UpdateMonitoringSchedule,
sagemaker:DescribeMonitoringSchedule
```

