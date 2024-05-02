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
Gets or operates on an individual <code>task</code> resource, use <code>tasks</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::Task.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.datasync.task</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>excludes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>includes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>cloud_watch_log_group_arn</code></td><td><code>string</code></td><td>The ARN of the Amazon CloudWatch log group that is used to monitor and log events in the task.</td></tr>
<tr><td><code>destination_location_arn</code></td><td><code>string</code></td><td>The ARN of an AWS storage resource's location.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of a task. This value is a text reference that is used to identify the task in the console.</td></tr>
<tr><td><code>options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>task_report_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>manifest_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>schedule</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>source_location_arn</code></td><td><code>string</code></td><td>The ARN of the source location for the task.</td></tr>
<tr><td><code>task_arn</code></td><td><code>string</code></td><td>The ARN of the task.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the task that was described.</td></tr>
<tr><td><code>source_network_interface_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>destination_network_interface_arns</code></td><td><code>array</code></td><td></td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
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
WHERE data__Identifier = '<TaskArn>';
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

### Delete
```json
datasync:DeleteTask,
ec2:DescribeNetworkInterfaces,
ec2:DeleteNetworkInterface,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
fsx:DescribeFileSystems,
elasticfilesystem:DescribeFileSystems,
elasticfilesystem:DescribeMountTargets,
iam:GetRole
```

