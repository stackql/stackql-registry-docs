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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>monitoring_schedules</code> in a region or create a <code>monitoring_schedules</code> resource, use <code>monitoring_schedule</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitoring_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::MonitoringSchedule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.monitoring_schedules" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="monitoring_schedule_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the monitoring schedule.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
monitoring_schedule_arn
FROM aws.sagemaker.monitoring_schedules
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>monitoring_schedules</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateMonitoringSchedule,
sagemaker:DescribeMonitoringSchedule,
iam:PassRole
```

### List
```json
sagemaker:ListMonitoringSchedule
```

