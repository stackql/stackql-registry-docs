---
title: composite_alarms
hide_title: false
hide_table_of_contents: false
keywords:
  - composite_alarms
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>composite_alarms</code> in a region or create a <code>composite_alarms</code> resource, use <code>composite_alarm</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>composite_alarms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CloudWatch::CompositeAlarm type specifies an alarm which aggregates the states of other Alarms (Metric or Composite Alarms) as defined by the AlarmRule expression</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudwatch.composite_alarms" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="alarm_name" /></td><td><code>string</code></td><td>The name of the Composite Alarm</td></tr>
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
alarm_name
FROM aws.cloudwatch.composite_alarms
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>composite_alarms</code> resource, the following permissions are required:

### Create
```json
cloudwatch:DescribeAlarms,
cloudwatch:PutCompositeAlarm,
cloudwatch:TagResource
```

### List
```json
cloudwatch:DescribeAlarms
```

