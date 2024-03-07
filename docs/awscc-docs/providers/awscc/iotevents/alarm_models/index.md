---
title: alarm_models
hide_title: false
hide_table_of_contents: false
keywords:
  - alarm_models
  - iotevents
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>alarm_models</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarm_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>alarm_models</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotevents.alarm_models</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>alarm_model_name</code></td><td><code>string</code></td><td>The name of the alarm model.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
alarm_model_name
FROM awscc.iotevents.alarm_models
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>alarm_models</code> resource, the following permissions are required:

### Create
```json
iotevents:CreateAlarmModel,
iotevents:UpdateInputRouting,
iotevents:DescribeAlarmModel,
iotevents:ListTagsForResource,
iotevents:TagResource,
iam:PassRole
```

### List
```json
iotevents:ListAlarmModels
```

