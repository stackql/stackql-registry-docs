---
title: monitor
hide_title: false
hide_table_of_contents: false
keywords:
  - monitor
  - internetmonitor
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>monitor</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>monitor</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.internetmonitor.monitor</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>modified_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>monitor_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>monitor_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>processing_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>processing_status_info</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resources</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>resources_to_add</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>resources_to_remove</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>max_city_networks_to_monitor</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>traffic_percentage_to_monitor</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>internet_measurements_log_delivery</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>health_events_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
created_at,
modified_at,
monitor_arn,
monitor_name,
processing_status,
processing_status_info,
resources,
resources_to_add,
resources_to_remove,
status,
tags,
max_city_networks_to_monitor,
traffic_percentage_to_monitor,
internet_measurements_log_delivery,
health_events_config
FROM awscc.internetmonitor.monitor
WHERE data__Identifier = '<MonitorName>';
```

## Permissions

To operate on the <code>monitor</code> resource, the following permissions are required:

### Read
```json
internetmonitor:GetMonitor,
internetmonitor:ListTagsForResource,
logs:GetLogDelivery
```

### Update
```json
internetmonitor:CreateMonitor,
internetmonitor:GetMonitor,
internetmonitor:UpdateMonitor,
internetmonitor:TagResource,
internetmonitor:UntagResource,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
s3:ListBucket,
iam:PassRole
```

### Delete
```json
internetmonitor:UpdateMonitor,
internetmonitor:DeleteMonitor,
internetmonitor:GetMonitor,
logs:DeleteLogDelivery
```

