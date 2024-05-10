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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>monitoring_schedule</code> resource, use <code>monitoring_schedules</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitoring_schedule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::MonitoringSchedule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.monitoring_schedule" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="monitoring_schedule_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the monitoring schedule.</td></tr>
<tr><td><CopyableCode code="monitoring_schedule_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="monitoring_schedule_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time at which the schedule was created.</td></tr>
<tr><td><CopyableCode code="endpoint_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="failure_reason" /></td><td><code>string</code></td><td>Contains the reason a monitoring job failed, if it failed.</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td>A timestamp that indicates the last time the monitoring job was modified.</td></tr>
<tr><td><CopyableCode code="last_monitoring_execution_summary" /></td><td><code>object</code></td><td>Describes metadata on the last execution to run, if there was one.</td></tr>
<tr><td><CopyableCode code="monitoring_schedule_status" /></td><td><code>string</code></td><td>The status of a schedule job.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.sagemaker.monitoring_schedule
WHERE region = 'us-east-1' AND data__Identifier = '<MonitoringScheduleArn>';
```


## Permissions

To operate on the <code>monitoring_schedule</code> resource, the following permissions are required:

### Read
```json
sagemaker:DescribeMonitoringSchedule
```

### Update
```json
sagemaker:UpdateMonitoringSchedule,
sagemaker:DescribeMonitoringSchedule
```

