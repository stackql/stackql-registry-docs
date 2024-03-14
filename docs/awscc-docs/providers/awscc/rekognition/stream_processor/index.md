---
title: stream_processor
hide_title: false
hide_table_of_contents: false
keywords:
  - stream_processor
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
Gets an individual <code>stream_processor</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stream_processor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>stream_processor</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rekognition.stream_processor</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the stream processor. It's an identifier you assign to the stream processor. You can use it to manage the stream processor.</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>The KMS key that is used by Rekognition to encrypt any intermediate customer metadata and store in the customer's S3 bucket.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>ARN of the IAM role that allows access to the stream processor, and provides Rekognition read permissions for KVS stream and write permissions to S3 bucket and SNS topic.</td></tr>
<tr><td><code>kinesis_video_stream</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>face_search_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>connected_home_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>kinesis_data_stream</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>s3_destination</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>notification_channel</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>data_sharing_preference</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>polygon_regions_of_interest</code></td><td><code>array</code></td><td>The PolygonRegionsOfInterest specifies a set of polygon areas of interest in the video frames to analyze, as part of connected home feature. Each polygon is in turn, an ordered list of Point</td></tr>
<tr><td><code>bounding_box_regions_of_interest</code></td><td><code>array</code></td><td>The BoundingBoxRegionsOfInterest specifies an array of bounding boxes of interest in the video frames to analyze, as part of connected home feature. If an object is partially in a region of interest, Rekognition will tag it as detected if the overlap of the object with the region-of-interest is greater than 20%.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>Current status of the stream processor.</td></tr>
<tr><td><code>status_message</code></td><td><code>string</code></td><td>Detailed status message about the stream processor.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.rekognition.stream_processor
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>stream_processor</code> resource, the following permissions are required:

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

