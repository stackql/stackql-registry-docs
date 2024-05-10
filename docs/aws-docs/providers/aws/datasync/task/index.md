---
title: task
hide_title: false
hide_table_of_contents: false
keywords:
  - task
  - datasync
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


Gets or updates an individual <code>task</code> resource, use <code>tasks</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::Task.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.task" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="excludes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="includes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="cloud_watch_log_group_arn" /></td><td><code>string</code></td><td>The ARN of the Amazon CloudWatch log group that is used to monitor and log events in the task.</td></tr>
<tr><td><CopyableCode code="destination_location_arn" /></td><td><code>string</code></td><td>The ARN of an AWS storage resource's location.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of a task. This value is a text reference that is used to identify the task in the console.</td></tr>
<tr><td><CopyableCode code="options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="task_report_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="manifest_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="schedule" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="source_location_arn" /></td><td><code>string</code></td><td>The ARN of the source location for the task.</td></tr>
<tr><td><CopyableCode code="task_arn" /></td><td><code>string</code></td><td>The ARN of the task.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the task that was described.</td></tr>
<tr><td><CopyableCode code="source_network_interface_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="destination_network_interface_arns" /></td><td><code>array</code></td><td></td></tr>
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
excludes,
includes,
tags,
cloud_watch_log_group_arn,
destination_location_arn,
name,
options,
task_report_config,
manifest_config,
schedule,
source_location_arn,
task_arn,
status,
source_network_interface_arns,
destination_network_interface_arns
FROM aws.datasync.task
WHERE region = 'us-east-1' AND data__Identifier = '<TaskArn>';
```


## Permissions

To operate on the <code>task</code> resource, the following permissions are required:

### Read
```json
datasync:DescribeTask,
datasync:ListTagsForResource
```

### Update
```json
datasync:UpdateTask,
datasync:DescribeTask,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource,
logs:DescribeLogGroups,
iam:PassRole
```

