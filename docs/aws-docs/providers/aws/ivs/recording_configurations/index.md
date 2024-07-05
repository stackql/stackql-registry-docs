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

Creates, updates, deletes or gets a <code>recording_configuration</code> resource or lists <code>recording_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recording_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::RecordingConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.recording_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Recording Configuration ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Recording Configuration Name.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>Recording Configuration State.</td></tr>
<tr><td><CopyableCode code="recording_reconnect_window_seconds" /></td><td><code>integer</code></td><td>Recording Reconnect Window Seconds. (0 means disabled)</td></tr>
<tr><td><CopyableCode code="destination_configuration" /></td><td><code>object</code></td><td>Recording Destination Configuration.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset model.</td></tr>
<tr><td><CopyableCode code="thumbnail_configuration" /></td><td><code>object</code></td><td>Recording Thumbnail Configuration.</td></tr>
<tr><td><CopyableCode code="rendition_configuration" /></td><td><code>object</code></td><td>Rendition Configuration describes which renditions should be recorded for a stream.</td></tr>
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
    <td><CopyableCode code="DestinationConfiguration, region" /></td>
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
Gets all <code>recording_configurations</code> in a region.
```sql
SELECT
region,
arn,
name,
state,
recording_reconnect_window_seconds,
destination_configuration,
tags,
thumbnail_configuration,
rendition_configuration
FROM aws.ivs.recording_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>recording_configuration</code>.
```sql
SELECT
region,
arn,
name,
state,
recording_reconnect_window_seconds,
destination_configuration,
tags,
thumbnail_configuration,
rendition_configuration
FROM aws.ivs.recording_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>recording_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ivs.recording_configurations (
 DestinationConfiguration,
 region
)
SELECT 
'{{ DestinationConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ Name }}',
 '{{ RecordingReconnectWindowSeconds }}',
 '{{ DestinationConfiguration }}',
 '{{ Tags }}',
 '{{ ThumbnailConfiguration }}',
 '{{ RenditionConfiguration }}',
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
  - name: recording_configuration
    props:
      - name: Name
        value: '{{ Name }}'
      - name: RecordingReconnectWindowSeconds
        value: '{{ RecordingReconnectWindowSeconds }}'
      - name: DestinationConfiguration
        value:
          S3:
            BucketName: '{{ BucketName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: ThumbnailConfiguration
        value:
          RecordingMode: '{{ RecordingMode }}'
          TargetIntervalSeconds: '{{ TargetIntervalSeconds }}'
          Resolution: '{{ Resolution }}'
          Storage:
            - '{{ Storage[0] }}'
      - name: RenditionConfiguration
        value:
          RenditionSelection: '{{ RenditionSelection }}'
          Renditions:
            - '{{ Renditions[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
ivs:GetRecordingConfiguration,
s3:GetBucketLocation,
ivs:ListTagsForResource
```

### Update
```json
ivs:GetRecordingConfiguration,
sts:AssumeRole,
iam:CreateServiceLinkedRole,
iam:PutRolePolicy,
iam:AttachRolePolicy,
s3:ListBucket,
ivs:TagResource,
ivs:UntagResource,
ivs:ListTagsForResource
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

