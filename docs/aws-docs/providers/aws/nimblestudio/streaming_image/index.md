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
Gets or operates on an individual <code>streaming_image</code> resource, use <code>streaming_images</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streaming_image</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a streaming session machine image that can be used to launch a streaming session</td></tr>
<tr><td><b>Id</b></td><td><code>aws.nimblestudio.streaming_image</code></td></tr>
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

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.nimblestudio.streaming_image
WHERE data__Identifier = '<StudioId>|<StreamingImageId>';
```

## Permissions

To operate on the <code>streaming_image</code> resource, the following permissions are required:

### Read
```json
nimble:GetStreamingImage
```

### Update
```json
nimble:UpdateStreamingImage,
nimble:GetStreamingImage,
kms:Encrypt,
kms:Decrypt,
kms:CreateGrant,
kms:ListGrants,
kms:GenerateDataKey
```

### Delete
```json
nimble:DeleteStreamingImage,
nimble:GetStreamingImage,
nimble:UntagResource,
ec2:ModifyInstanceAttribute,
ec2:ModifySnapshotAttribute,
ec2:DeregisterImage,
ec2:DeleteSnapshot,
kms:ListGrants,
kms:RetireGrant
```

