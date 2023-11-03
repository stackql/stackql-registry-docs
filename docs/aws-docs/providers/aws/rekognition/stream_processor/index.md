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
null
<tr><td><b>Id</b></td><td><code>aws.rekognition.stream_processor</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>Name of the stream processor. It's an identifier you assign to the stream processor. You can use it to manage the stream processor.</td></tr><tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td>The KMS key that is used by Rekognition to encrypt any intermediate customer metadata and store in the customer's S3 bucket.</td></tr><tr><td><code>RoleArn</code></td><td><code>string</code></td><td>ARN of the IAM role that allows access to the stream processor, and provides Rekognition read permissions for KVS stream and write permissions to S3 bucket and SNS topic.</td></tr><tr><td><code>KinesisVideoStream</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>FaceSearchSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ConnectedHomeSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>KinesisDataStream</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>S3Destination</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>NotificationChannel</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DataSharingPreference</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>PolygonRegionsOfInterest</code></td><td><code>array</code></td><td>The PolygonRegionsOfInterest specifies a set of polygon areas of interest in the video frames to analyze, as part of connected home feature. Each polygon is in turn, an ordered list of Point</td></tr><tr><td><code>BoundingBoxRegionsOfInterest</code></td><td><code>array</code></td><td>The BoundingBoxRegionsOfInterest specifies an array of bounding boxes of interest in the video frames to analyze, as part of connected home feature. If an object is partially in a region of interest, Rekognition will tag it as detected if the overlap of the object with the region-of-interest is greater than 20%.</td></tr><tr><td><code>Status</code></td><td><code>string</code></td><td>Current status of the stream processor.</td></tr><tr><td><code>StatusMessage</code></td><td><code>string</code></td><td>Detailed status message about the stream processor.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.rekognition.stream_processor
WHERE region = 'us-east-1' AND data__Identifier = '{Name}'
</pre>
