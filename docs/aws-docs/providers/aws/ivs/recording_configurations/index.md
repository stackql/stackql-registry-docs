---
title: recording_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - recording_configurations
  - ivs
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


Used to retrieve a list of <code>recording_configurations</code> in a region or to create or delete a <code>recording_configurations</code> resource, use <code>recording_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recording_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::RecordingConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.recording_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Recording Configuration ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
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
arn
FROM aws.ivs.recording_configurations
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
 "DestinationConfiguration": {
  "S3": {
   "BucketName": "{{ BucketName }}"
  }
 }
}
>>>
--required properties only
INSERT INTO aws.ivs.recording_configurations (
 DestinationConfiguration,
 region
)
SELECT 
{{ .DestinationConfiguration }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "RecordingReconnectWindowSeconds": "{{ RecordingReconnectWindowSeconds }}",
 "DestinationConfiguration": {
  "S3": {
   "BucketName": "{{ BucketName }}"
  }
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "ThumbnailConfiguration": {
  "RecordingMode": "{{ RecordingMode }}",
  "TargetIntervalSeconds": "{{ TargetIntervalSeconds }}",
  "Resolution": "{{ Resolution }}",
  "Storage": [
   "{{ Storage[0] }}"
  ]
 },
 "RenditionConfiguration": {
  "RenditionSelection": "{{ RenditionSelection }}",
  "Renditions": [
   "{{ Renditions[0] }}"
  ]
 }
}
>>>
--all properties
INSERT INTO aws.ivs.recording_configurations (
 Name,
 RecordingReconnectWindowSeconds,
 DestinationConfiguration,
 Tags,
 ThumbnailConfiguration,
 RenditionConfiguration,
 region
)
SELECT 
 {{ .Name }},
 {{ .RecordingReconnectWindowSeconds }},
 {{ .DestinationConfiguration }},
 {{ .Tags }},
 {{ .ThumbnailConfiguration }},
 {{ .RenditionConfiguration }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ivs.recording_configurations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>recording_configurations</code> resource, the following permissions are required:

### Create
```json
ivs:CreateRecordingConfiguration,
ivs:GetRecordingConfiguration,
ivs:TagResource,
iam:CreateServiceLinkedRole,
iam:PutRolePolicy,
iam:AttachRolePolicy,
s3:ListBucket,
s3:GetBucketLocation,
cloudformation:ListExports
```

### Delete
```json
ivs:DeleteRecordingConfiguration,
ivs:UntagResource,
iam:CreateServiceLinkedRole
```

### List
```json
ivs:ListRecordingConfigurations,
s3:GetBucketLocation,
ivs:ListTagsForResource
```

