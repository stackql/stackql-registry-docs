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
Gets an individual <code>task</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>task</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datasync.task</code></td></tr>
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
<tr><td><code>schedule</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>source_location_arn</code></td><td><code>string</code></td><td>The ARN of the source location for the task.</td></tr>
<tr><td><code>task_arn</code></td><td><code>string</code></td><td>The ARN of the task.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the task that was described.</td></tr>
<tr><td><code>source_network_interface_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>destination_network_interface_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>task</code> resource, the following permissions are required:

### Read
<pre>
datasync:DescribeTask,
datasync:ListTagsForResource</pre>

### Update
<pre>
datasync:UpdateTask,
datasync:DescribeTask,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource,
logs:DescribeLogGroups,
iam:PassRole</pre>

### Delete
<pre>
datasync:DeleteTask,
ec2:DescribeNetworkInterfaces,
ec2:DeleteNetworkInterface,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
fsx:DescribeFileSystems,
elasticfilesystem:DescribeFileSystems,
elasticfilesystem:DescribeMountTargets,
iam:GetRole</pre>


## Example
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
schedule,
source_location_arn,
task_arn,
status,
source_network_interface_arns,
destination_network_interface_arns
FROM awscc.datasync.task
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;TaskArn&gt;'
```
