---
title: streaming_image
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_image
  - nimblestudio
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>streaming_image</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streaming_image</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.nimblestudio.streaming_image</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td><p>A human-readable description of the streaming image.</p></td></tr><tr><td><code>Ec2ImageId</code></td><td><code>string</code></td><td><p>The ID of an EC2 machine image with which to create this streaming image.</p></td></tr><tr><td><code>EncryptionConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>EulaIds</code></td><td><code>array</code></td><td><p>The list of EULAs that must be accepted before a Streaming Session can be started using this streaming image.</p></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td><p>A friendly name for a streaming image resource.</p></td></tr><tr><td><code>Owner</code></td><td><code>string</code></td><td><p>The owner of the streaming image, either the studioId that contains the streaming image, or 'amazon' for images that are provided by Amazon Nimble Studio.</p></td></tr><tr><td><code>Platform</code></td><td><code>string</code></td><td><p>The platform of the streaming image, either WINDOWS or LINUX.</p></td></tr><tr><td><code>StreamingImageId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>StudioId</code></td><td><code>string</code></td><td><p>The studioId. </p></td></tr><tr><td><code>Tags</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.nimblestudio.streaming_image
WHERE region = 'us-east-1' AND data__Identifier = '{StudioId}' AND data__Identifier = '{StreamingImageId}'
```
