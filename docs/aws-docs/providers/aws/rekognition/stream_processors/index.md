---
title: stream_processors
hide_title: false
hide_table_of_contents: false
keywords:
  - stream_processors
  - rekognition
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


Used to retrieve a list of <code>stream_processors</code> in a region or to create or delete a <code>stream_processors</code> resource, use <code>stream_processor</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stream_processors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Rekognition::StreamProcessor type is used to create an Amazon Rekognition StreamProcessor that you can use to analyze streaming videos.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rekognition.stream_processors" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the stream processor. It's an identifier you assign to the stream processor. You can use it to manage the stream processor.</td></tr>
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
name
FROM aws.rekognition.stream_processors
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>stream_processor</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- stream_processor.iql (required properties only)
INSERT INTO aws.rekognition.stream_processors (
 RoleArn,
 KinesisVideoStream,
 region
)
SELECT 
'{{ RoleArn }}',
 '{{ KinesisVideoStream }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- stream_processor.iql (all properties)
INSERT INTO aws.rekognition.stream_processors (
 Name,
 KmsKeyId,
 RoleArn,
 KinesisVideoStream,
 FaceSearchSettings,
 ConnectedHomeSettings,
 KinesisDataStream,
 S3Destination,
 NotificationChannel,
 DataSharingPreference,
 PolygonRegionsOfInterest,
 BoundingBoxRegionsOfInterest,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ KmsKeyId }}',
 '{{ RoleArn }}',
 '{{ KinesisVideoStream }}',
 '{{ FaceSearchSettings }}',
 '{{ ConnectedHomeSettings }}',
 '{{ KinesisDataStream }}',
 '{{ S3Destination }}',
 '{{ NotificationChannel }}',
 '{{ DataSharingPreference }}',
 '{{ PolygonRegionsOfInterest }}',
 '{{ BoundingBoxRegionsOfInterest }}',
 '{{ Tags }}',
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
  - name: stream_processor
    props:
      - name: Name
        value: '{{ Name }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: KinesisVideoStream
        value:
          Arn: '{{ Arn }}'
      - name: FaceSearchSettings
        value:
          CollectionId: '{{ CollectionId }}'
          FaceMatchThreshold: null
      - name: ConnectedHomeSettings
        value:
          Labels:
            - '{{ Labels[0] }}'
          MinConfidence: null
      - name: KinesisDataStream
        value:
          Arn: '{{ Arn }}'
      - name: S3Destination
        value:
          BucketName: '{{ BucketName }}'
          ObjectKeyPrefix: '{{ ObjectKeyPrefix }}'
      - name: NotificationChannel
        value:
          Arn: '{{ Arn }}'
      - name: DataSharingPreference
        value:
          OptIn: '{{ OptIn }}'
      - name: PolygonRegionsOfInterest
        value:
          - - X: null
              'Y': null
      - name: BoundingBoxRegionsOfInterest
        value:
          - Height: null
            Width: null
            Left: null
            Top: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.rekognition.stream_processors
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>stream_processors</code> resource, the following permissions are required:

### Create
```json
rekognition:CreateStreamProcessor,
iam:PassRole,
rekognition:DescribeStreamProcessor,
rekognition:ListTagsForResource,
rekognition:TagResource
```

### Delete
```json
rekognition:DeleteStreamProcessor
```

### List
```json
rekognition:ListStreamProcessors
```

