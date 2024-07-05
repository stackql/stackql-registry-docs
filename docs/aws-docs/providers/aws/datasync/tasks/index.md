---
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
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

Creates, updates, deletes or gets a <code>task</code> resource or lists <code>tasks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::Task.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.tasks" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="excludes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="includes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="cloud_watch_log_group_arn" /></td><td><code>string</code></td><td>The ARN of the Amazon CloudWatch log group that is used to monitor and log events in the task.</td></tr>
<tr><td><CopyableCode code="destination_location_arn" /></td><td><code>string</code></td><td>The ARN of an AWS storage resource's location.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of a task. This value is a text reference that is used to identify the task in the console.</td></tr>
<tr><td><CopyableCode code="options" /></td><td><code>object</code></td><td>Represents the options that are available to control the behavior of a StartTaskExecution operation.</td></tr>
<tr><td><CopyableCode code="task_report_config" /></td><td><code>object</code></td><td>Specifies how you want to configure a task report, which provides detailed information about for your Datasync transfer.</td></tr>
<tr><td><CopyableCode code="manifest_config" /></td><td><code>object</code></td><td>Configures a manifest, which is a list of files or objects that you want DataSync to transfer.</td></tr>
<tr><td><CopyableCode code="schedule" /></td><td><code>object</code></td><td>Specifies the schedule you want your task to use for repeated executions.</td></tr>
<tr><td><CopyableCode code="source_location_arn" /></td><td><code>string</code></td><td>The ARN of the source location for the task.</td></tr>
<tr><td><CopyableCode code="task_arn" /></td><td><code>string</code></td><td>The ARN of the task.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the task that was described.</td></tr>
<tr><td><CopyableCode code="source_network_interface_arns" /></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of the source ENIs (Elastic Network Interfaces) that were created for your subnet.</td></tr>
<tr><td><CopyableCode code="destination_network_interface_arns" /></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of the destination ENIs (Elastic Network Interfaces) that were created for your subnet.</td></tr>
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
    <td><CopyableCode code="DestinationLocationArn, SourceLocationArn, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>tasks</code> in a region.
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
FROM aws.datasync.tasks
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>task</code>.
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
FROM aws.datasync.tasks
WHERE region = 'us-east-1' AND data__Identifier = '<TaskArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>task</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.datasync.tasks (
 DestinationLocationArn,
 SourceLocationArn,
 region
)
SELECT 
'{{ DestinationLocationArn }}',
 '{{ SourceLocationArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datasync.tasks (
 Excludes,
 Includes,
 Tags,
 CloudWatchLogGroupArn,
 DestinationLocationArn,
 Name,
 Options,
 TaskReportConfig,
 ManifestConfig,
 Schedule,
 SourceLocationArn,
 region
)
SELECT 
 '{{ Excludes }}',
 '{{ Includes }}',
 '{{ Tags }}',
 '{{ CloudWatchLogGroupArn }}',
 '{{ DestinationLocationArn }}',
 '{{ Name }}',
 '{{ Options }}',
 '{{ TaskReportConfig }}',
 '{{ ManifestConfig }}',
 '{{ Schedule }}',
 '{{ SourceLocationArn }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: task
    props:
      - name: Excludes
        value:
          - FilterType: '{{ FilterType }}'
            Value: '{{ Value }}'
      - name: Includes
        value:
          - null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: CloudWatchLogGroupArn
        value: '{{ CloudWatchLogGroupArn }}'
      - name: DestinationLocationArn
        value: '{{ DestinationLocationArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: Options
        value:
          Atime: '{{ Atime }}'
          BytesPerSecond: '{{ BytesPerSecond }}'
          Gid: '{{ Gid }}'
          LogLevel: '{{ LogLevel }}'
          Mtime: '{{ Mtime }}'
          OverwriteMode: '{{ OverwriteMode }}'
          PosixPermissions: '{{ PosixPermissions }}'
          PreserveDeletedFiles: '{{ PreserveDeletedFiles }}'
          PreserveDevices: '{{ PreserveDevices }}'
          SecurityDescriptorCopyFlags: '{{ SecurityDescriptorCopyFlags }}'
          TaskQueueing: '{{ TaskQueueing }}'
          TransferMode: '{{ TransferMode }}'
          Uid: '{{ Uid }}'
          VerifyMode: '{{ VerifyMode }}'
          ObjectTags: '{{ ObjectTags }}'
      - name: TaskReportConfig
        value:
          Destination:
            S3:
              Subdirectory: '{{ Subdirectory }}'
              BucketAccessRoleArn: '{{ BucketAccessRoleArn }}'
              S3BucketArn: '{{ S3BucketArn }}'
          OutputType: '{{ OutputType }}'
          ReportLevel: '{{ ReportLevel }}'
          ObjectVersionIds: '{{ ObjectVersionIds }}'
          Overrides:
            Transferred:
              ReportLevel: '{{ ReportLevel }}'
            Verified:
              ReportLevel: '{{ ReportLevel }}'
            Deleted:
              ReportLevel: '{{ ReportLevel }}'
            Skipped:
              ReportLevel: '{{ ReportLevel }}'
      - name: ManifestConfig
        value:
          Action: '{{ Action }}'
          Format: '{{ Format }}'
          Source:
            S3:
              ManifestObjectPath: '{{ ManifestObjectPath }}'
              BucketAccessRoleArn: '{{ BucketAccessRoleArn }}'
              S3BucketArn: '{{ S3BucketArn }}'
              ManifestObjectVersionId: '{{ ManifestObjectVersionId }}'
      - name: Schedule
        value:
          ScheduleExpression: '{{ ScheduleExpression }}'
          Status: '{{ Status }}'
      - name: SourceLocationArn
        value: '{{ SourceLocationArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.datasync.tasks
WHERE data__Identifier = '<TaskArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>tasks</code> resource, the following permissions are required:

### Create
```json
datasync:CreateTask,
datasync:DescribeTask,
datasync:ListTagsForResource,
datasync:TagResource,
s3:ListAllMyBuckets,
s3:ListBucket,
s3:GetObject,
s3:GetObjectVersion,
ec2:DescribeNetworkInterfaces,
ec2:CreateNetworkInterface,
ec2:DeleteNetworkInterface,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:CreateNetworkInterfacePermission,
fsx:DescribeFileSystems,
elasticfilesystem:DescribeFileSystems,
elasticfilesystem:DescribeMountTargets,
logs:DescribeLogGroups,
iam:GetRole,
iam:PassRole,
iam:AssumeRole
```

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

### List
```json
datasync:ListTasks
```

