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


Used to retrieve a list of <code>streaming_images</code> in a region or to create or delete a <code>streaming_images</code> resource, use <code>streaming_image</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streaming_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a streaming session machine image that can be used to launch a streaming session</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.streaming_images" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td>&lt;p&gt;The studioId. &lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="streaming_image_id" /></td><td><code>string</code></td><td></td></tr>
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
studio_id,
streaming_image_id
FROM aws.nimblestudio.streaming_images
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Ec2ImageId": "{{ Ec2ImageId }}",
 "Name": "{{ Name }}",
 "StudioId": "{{ StudioId }}"
}
>>>
--required properties only
INSERT INTO aws.nimblestudio.streaming_images (
 Ec2ImageId,
 Name,
 StudioId,
 region
)
SELECT 
{{ Ec2ImageId }},
 {{ Name }},
 {{ StudioId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "Ec2ImageId": "{{ Ec2ImageId }}",
 "Name": "{{ Name }}",
 "StudioId": "{{ StudioId }}",
 "Tags": {}
}
>>>
--all properties
INSERT INTO aws.nimblestudio.streaming_images (
 Description,
 Ec2ImageId,
 Name,
 StudioId,
 Tags,
 region
)
SELECT 
 {{ Description }},
 {{ Ec2ImageId }},
 {{ Name }},
 {{ StudioId }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

