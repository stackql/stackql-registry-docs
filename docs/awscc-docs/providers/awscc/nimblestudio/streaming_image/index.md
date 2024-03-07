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
<tr><td><b>Description</b></td><td>streaming_image</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.nimblestudio.streaming_image</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>&lt;p&gt;A human-readable description of the streaming image.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>ec2_image_id</code></td><td><code>string</code></td><td>&lt;p&gt;The ID of an EC2 machine image with which to create this streaming image.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>encryption_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>eula_ids</code></td><td><code>array</code></td><td>&lt;p&gt;The list of EULAs that must be accepted before a Streaming Session can be started using this streaming image.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>&lt;p&gt;A friendly name for a streaming image resource.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>owner</code></td><td><code>string</code></td><td>&lt;p&gt;The owner of the streaming image, either the studioId that contains the streaming image, or 'amazon' for images that are provided by Amazon Nimble Studio.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>platform</code></td><td><code>string</code></td><td>&lt;p&gt;The platform of the streaming image, either WINDOWS or LINUX.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>streaming_image_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>studio_id</code></td><td><code>string</code></td><td>&lt;p&gt;The studioId. &lt;&#x2F;p&gt;</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>streaming_image</code> resource, the following permissions are required:

### Read
<pre>
nimble:GetStreamingImage</pre>

### Update
<pre>
nimble:UpdateStreamingImage,
nimble:GetStreamingImage,
kms:Encrypt,
kms:Decrypt,
kms:CreateGrant,
kms:ListGrants,
kms:GenerateDataKey</pre>

### Delete
<pre>
nimble:DeleteStreamingImage,
nimble:GetStreamingImage,
nimble:UntagResource,
ec2:ModifyInstanceAttribute,
ec2:ModifySnapshotAttribute,
ec2:DeregisterImage,
ec2:DeleteSnapshot,
kms:ListGrants,
kms:RetireGrant</pre>


## Example
```sql
SELECT
region,
description,
ec2_image_id,
encryption_configuration,
eula_ids,
name,
owner,
platform,
streaming_image_id,
studio_id,
tags
FROM awscc.nimblestudio.streaming_image
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;StudioId&gt;'
AND data__Identifier = '&lt;StreamingImageId&gt;'
```
