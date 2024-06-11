---
title: signaling_channels
hide_title: false
hide_table_of_contents: false
keywords:
  - signaling_channels
  - kinesisvideo
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

Creates, updates, deletes or gets a <code>signaling_channel</code> resource or lists <code>signaling_channels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>signaling_channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::KinesisVideo::SignalingChannel</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kinesisvideo.signaling_channels" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Kinesis Video Signaling Channel.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the Kinesis Video Signaling Channel.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the Kinesis Video Signaling Channel to create. Currently, SINGLE_MASTER is the only supported channel type.</td></tr>
<tr><td><CopyableCode code="message_ttl_seconds" /></td><td><code>integer</code></td><td>The period of time a signaling channel retains undelivered messages before they are discarded.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code=", region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from a <code>signaling_channel</code>.
```sql
SELECT
region,
arn,
name,
type,
message_ttl_seconds,
tags
FROM aws.kinesisvideo.signaling_channels
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>signaling_channel</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.kinesisvideo.signaling_channels (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.kinesisvideo.signaling_channels (
 Name,
 Type,
 MessageTtlSeconds,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Type }}',
 '{{ MessageTtlSeconds }}',
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
  - name: signaling_channel
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Type
        value: '{{ Type }}'
      - name: MessageTtlSeconds
        value: '{{ MessageTtlSeconds }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.kinesisvideo.signaling_channels
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>signaling_channels</code> resource, the following permissions are required:

### Create
```json
kinesisvideo:CreateSignalingChannel,
kinesisvideo:DescribeSignalingChannel
```

### Read
```json
kinesisvideo:DescribeSignalingChannel
```

### Update
```json
kinesisvideo:UpdateSignalingChannel,
kinesisvideo:DescribeSignalingChannel
```

### Delete
```json
kinesisvideo:DeleteSignalingChannel,
kinesisvideo:DescribeSignalingChannel
```

