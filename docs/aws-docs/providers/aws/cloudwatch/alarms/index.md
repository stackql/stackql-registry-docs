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
<tr><td><b>Description</b></td><td>The ``AWS::CloudWatch::Alarm`` type specifies an alarm and associates it with the specified metric or metric math expression.&lt;br&#x2F;&gt; When this operation creates an alarm, the alarm state is immediately set to ``INSUFFICIENT_DATA``. The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.&lt;br&#x2F;&gt; When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudwatch.alarms</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>alarm_name</code></td><td><code>string</code></td><td>The name of the alarm. If you don't specify a name, CFN generates a unique physical ID and uses that ID for the alarm name. &lt;br&#x2F;&gt;  If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
alarm_name
FROM aws.cloudwatch.alarms
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>alarms</code> resource, the following permissions are required:

### Create
```json
cloudwatch:PutMetricAlarm,
cloudwatch:DescribeAlarms,
cloudwatch:TagResource
```

### List
```json
cloudwatch:DescribeAlarms
```

