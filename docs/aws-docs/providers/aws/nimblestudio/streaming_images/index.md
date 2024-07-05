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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>streaming_image</code> resource or lists <code>streaming_images</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streaming_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a streaming session machine image that can be used to launch a streaming session</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.streaming_images" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td><p>A human-readable description of the streaming image.</p></td></tr>
<tr><td><CopyableCode code="ec2_image_id" /></td><td><code>string</code></td><td><p>The ID of an EC2 machine image with which to create this streaming image.</p></td></tr>
<tr><td><CopyableCode code="encryption_configuration" /></td><td><code>object</code></td><td><p>TODO</p></td></tr>
<tr><td><CopyableCode code="eula_ids" /></td><td><code>array</code></td><td><p>The list of EULAs that must be accepted before a Streaming Session can be started using this streaming image.</p></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td><p>A friendly name for a streaming image resource.</p></td></tr>
<tr><td><CopyableCode code="owner" /></td><td><code>string</code></td><td><p>The owner of the streaming image, either the studioId that contains the streaming image, or 'amazon' for images that are provided by Amazon Nimble Studio.</p></td></tr>
<tr><td><CopyableCode code="platform" /></td><td><code>string</code></td><td><p>The platform of the streaming image, either WINDOWS or LINUX.</p></td></tr>
<tr><td><CopyableCode code="streaming_image_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td><p>The studioId. </p></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="StudioId, Ec2ImageId, Name, region" /></td>
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
Gets all <code>streaming_images</code> in a region.
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
FROM aws.nimblestudio.streaming_images
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>streaming_image</code>.
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
FROM aws.nimblestudio.streaming_images
WHERE region = 'us-east-1' AND data__Identifier = '<StudioId>|<StreamingImageId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>streaming_image</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.nimblestudio.streaming_images (
 Ec2ImageId,
 Name,
 StudioId,
 region
)
SELECT 
'{{ Ec2ImageId }}',
 '{{ Name }}',
 '{{ StudioId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.nimblestudio.streaming_images (
 Description,
 Ec2ImageId,
 Name,
 StudioId,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Ec2ImageId }}',
 '{{ Name }}',
 '{{ StudioId }}',
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
  - name: streaming_image
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Ec2ImageId
        value: '{{ Ec2ImageId }}'
      - name: Name
        value: '{{ Name }}'
      - name: StudioId
        value: '{{ StudioId }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.nimblestudio.streaming_images
WHERE data__Identifier = '<StudioId|StreamingImageId>'
AND region = 'us-east-1';
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

### List
```json
nimble:ListStreamingImages
```

