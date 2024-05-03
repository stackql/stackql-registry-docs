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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>monitor</code> resource, use <code>monitors</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a monitor, which defines the monitoring boundaries for measurements that Internet Monitor publishes information about for an application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.internetmonitor.monitor" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="monitor_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="monitor_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="linked_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="include_linked_accounts" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="processing_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="processing_status_info" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resources" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resources_to_add" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resources_to_remove" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="max_city_networks_to_monitor" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="traffic_percentage_to_monitor" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="internet_measurements_log_delivery" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="health_events_config" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
created_at,
modified_at,
monitor_arn,
monitor_name,
linked_account_id,
include_linked_accounts,
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
FROM aws.internetmonitor.monitor
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

