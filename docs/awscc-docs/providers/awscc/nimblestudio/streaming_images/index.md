---
title: streaming_images
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_images
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
Retrieves a list of <code>streaming_images</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streaming_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>streaming_images</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.nimblestudio.streaming_images</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>studio_id</code></td><td><code>string</code></td><td>&lt;p&gt;The studioId. &lt;&#x2F;p&gt;</td></tr>
<tr><td><code>streaming_image_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
studio_id,
streaming_image_id
FROM awscc.nimblestudio.streaming_images
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>streaming_images</code> resource, the following permissions are required:

### Create
```json
nimble:CreateStreamingImage,
nimble:GetStreamingImage,
nimble:TagResource,
ec2:DescribeImages,
ec2:DescribeSnapshots,
ec2:ModifyInstanceAttribute,
ec2:ModifySnapshotAttribute,
ec2:ModifyImageAttribute,
ec2:RegisterImage,
kms:Encrypt,
kms:Decrypt,
kms:CreateGrant,
kms:ListGrants,
kms:GenerateDataKey
```

### List
```json
nimble:ListStreamingImages
```

