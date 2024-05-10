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


Used to retrieve a list of <code>tasks</code> in a region or to create or delete a <code>tasks</code> resource, use <code>task</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::Task.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.tasks" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="task_arn" /></td><td><code>string</code></td><td>The ARN of the task.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
task_arn
FROM aws.datasync.tasks
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "DestinationLocationArn": "{{ DestinationLocationArn }}",
 "SourceLocationArn": "{{ SourceLocationArn }}"
}
>>>
--required properties only
INSERT INTO aws.datasync.tasks (
 DestinationLocationArn,
 SourceLocationArn,
 region
)
SELECT 
{{ .DestinationLocationArn }},
 {{ .SourceLocationArn }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Excludes": [
  {
   "FilterType": "{{ FilterType }}",
   "Value": "{{ Value }}"
  }
 ],
 "Includes": [
  null
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "CloudWatchLogGroupArn": "{{ CloudWatchLogGroupArn }}",
 "DestinationLocationArn": "{{ DestinationLocationArn }}",
 "Name": "{{ Name }}",
 "Options": {
  "Atime": "{{ Atime }}",
  "BytesPerSecond": "{{ BytesPerSecond }}",
  "Gid": "{{ Gid }}",
  "LogLevel": "{{ LogLevel }}",
  "Mtime": "{{ Mtime }}",
  "OverwriteMode": "{{ OverwriteMode }}",
  "PosixPermissions": "{{ PosixPermissions }}",
  "PreserveDeletedFiles": "{{ PreserveDeletedFiles }}",
  "PreserveDevices": "{{ PreserveDevices }}",
  "SecurityDescriptorCopyFlags": "{{ SecurityDescriptorCopyFlags }}",
  "TaskQueueing": "{{ TaskQueueing }}",
  "TransferMode": "{{ TransferMode }}",
  "Uid": "{{ Uid }}",
  "VerifyMode": "{{ VerifyMode }}",
  "ObjectTags": "{{ ObjectTags }}"
 },
 "TaskReportConfig": {
  "Destination": {
   "S3": {
    "Subdirectory": "{{ Subdirectory }}",
    "BucketAccessRoleArn": "{{ BucketAccessRoleArn }}",
    "S3BucketArn": "{{ S3BucketArn }}"
   }
  },
  "OutputType": "{{ OutputType }}",
  "ReportLevel": "{{ ReportLevel }}",
  "ObjectVersionIds": "{{ ObjectVersionIds }}",
  "Overrides": {
   "Transferred": {
    "ReportLevel": "{{ ReportLevel }}"
   },
   "Verified": {
    "ReportLevel": "{{ ReportLevel }}"
   },
   "Deleted": {
    "ReportLevel": "{{ ReportLevel }}"
   },
   "Skipped": {
    "ReportLevel": "{{ ReportLevel }}"
   }
  }
 },
 "ManifestConfig": {
  "Action": "{{ Action }}",
  "Format": "{{ Format }}",
  "Source": {
   "S3": {
    "ManifestObjectPath": "{{ ManifestObjectPath }}",
    "BucketAccessRoleArn": "{{ BucketAccessRoleArn }}",
    "S3BucketArn": "{{ S3BucketArn }}",
    "ManifestObjectVersionId": "{{ ManifestObjectVersionId }}"
   }
  }
 },
 "Schedule": {
  "ScheduleExpression": "{{ ScheduleExpression }}"
 },
 "SourceLocationArn": "{{ SourceLocationArn }}"
}
>>>
--all properties
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
 {{ .Excludes }},
 {{ .Includes }},
 {{ .Tags }},
 {{ .CloudWatchLogGroupArn }},
 {{ .DestinationLocationArn }},
 {{ .Name }},
 {{ .Options }},
 {{ .TaskReportConfig }},
 {{ .ManifestConfig }},
 {{ .Schedule }},
 {{ .SourceLocationArn }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

