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

Creates, updates, deletes or gets a <code>stream_processor</code> resource or lists <code>stream_processors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stream_processors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Rekognition::StreamProcessor type is used to create an Amazon Rekognition StreamProcessor that you can use to analyze streaming videos.<br /></td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rekognition.stream_processors" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the stream processor</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the stream processor. It's an identifier you assign to the stream processor. You can use it to manage the stream processor.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The KMS key that is used by Rekognition to encrypt any intermediate customer metadata and store in the customer's S3 bucket.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>ARN of the IAM role that allows access to the stream processor, and provides Rekognition read permissions for KVS stream and write permissions to S3 bucket and SNS topic.</td></tr>
<tr><td><CopyableCode code="kinesis_video_stream" /></td><td><code>object</code></td><td>The Kinesis Video Stream that streams the source video.</td></tr>
<tr><td><CopyableCode code="face_search_settings" /></td><td><code>object</code></td><td>Face search settings to use on a streaming video. Note that either FaceSearchSettings or ConnectedHomeSettings should be set. Not both</td></tr>
<tr><td><CopyableCode code="connected_home_settings" /></td><td><code>object</code></td><td>Connected home settings to use on a streaming video. Note that either ConnectedHomeSettings or FaceSearchSettings should be set. Not both</td></tr>
<tr><td><CopyableCode code="kinesis_data_stream" /></td><td><code>object</code></td><td>The Amazon Kinesis Data Stream stream to which the Amazon Rekognition stream processor streams the analysis results, as part of face search feature.</td></tr>
<tr><td><CopyableCode code="s3_destination" /></td><td><code>object</code></td><td>The S3 location in customer's account where inference output & artifacts are stored, as part of connected home feature.</td></tr>
<tr><td><CopyableCode code="notification_channel" /></td><td><code>object</code></td><td>The ARN of the SNS notification channel where events of interests are published, as part of connected home feature.</td></tr>
<tr><td><CopyableCode code="data_sharing_preference" /></td><td><code>object</code></td><td>Indicates whether Rekognition is allowed to store the video stream data for model-training.</td></tr>
<tr><td><CopyableCode code="polygon_regions_of_interest" /></td><td><code>array</code></td><td>The PolygonRegionsOfInterest specifies a set of polygon areas of interest in the video frames to analyze, as part of connected home feature. Each polygon is in turn, an ordered list of Point</td></tr>
<tr><td><CopyableCode code="bounding_box_regions_of_interest" /></td><td><code>array</code></td><td>The BoundingBoxRegionsOfInterest specifies an array of bounding boxes of interest in the video frames to analyze, as part of connected home feature. If an object is partially in a region of interest, Rekognition will tag it as detected if the overlap of the object with the region-of-interest is greater than 20%.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Current status of the stream processor.</td></tr>
<tr><td><CopyableCode code="status_message" /></td><td><code>string</code></td><td>Detailed status message about the stream processor.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="RoleArn, KinesisVideoStream, region" /></td>
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
Gets all <code>stream_processors</code> in a region.
```sql
SELECT
region,
arn,
name,
kms_key_id,
role_arn,
kinesis_video_stream,
face_search_settings,
connected_home_settings,
kinesis_data_stream,
s3_destination,
notification_channel,
data_sharing_preference,
polygon_regions_of_interest,
bounding_box_regions_of_interest,
status,
status_message,
tags
FROM aws.rekognition.stream_processors
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>stream_processor</code>.
```sql
SELECT
region,
arn,
name,
kms_key_id,
role_arn,
kinesis_video_stream,
face_search_settings,
connected_home_settings,
kinesis_data_stream,
s3_destination,
notification_channel,
data_sharing_preference,
polygon_regions_of_interest,
bounding_box_regions_of_interest,
status,
status_message,
tags
FROM aws.rekognition.stream_processors
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
rekognition:DescribeStreamProcessor,
rekognition:ListTagsForResource
```

### Update
```json
rekognition:TagResource,
rekognition:UntagResource,
rekognition:ListTagsForResource,
rekognition:DescribeStreamProcessor
```

### Delete
```json
rekognition:DeleteStreamProcessor
```

### List
```json
rekognition:ListStreamProcessors
```

