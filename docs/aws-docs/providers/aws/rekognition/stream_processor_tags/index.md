---
title: stream_processor_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - stream_processor_tags
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

Expands all tag keys and values for <code>stream_processors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stream_processor_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Rekognition::StreamProcessor type is used to create an Amazon Rekognition StreamProcessor that you can use to analyze streaming videos.<br /></td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rekognition.stream_processor_tags" /></td></tr>
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
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>stream_processors</code> in a region.
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
tag_key,
tag_value
FROM aws.rekognition.stream_processor_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>stream_processor_tags</code> resource, see <a href="/providers/aws/rekognition/stream_processors/#permissions"><code>stream_processors</code></a>

