---
title: streaming_image_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_image_tags
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

Expands all tag keys and values for <code>streaming_images</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streaming_image_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a streaming session machine image that can be used to launch a streaming session</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.streaming_image_tags" /></td></tr>
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
Expands tags for all <code>streaming_images</code> in a region.
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
tag_key,
tag_value
FROM aws.nimblestudio.streaming_image_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>streaming_image_tags</code> resource, see <a href="/providers/aws/nimblestudio/streaming_images/#permissions"><code>streaming_images</code></a>


