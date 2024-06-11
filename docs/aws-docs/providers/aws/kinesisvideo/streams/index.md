---
title: streams
hide_title: false
hide_table_of_contents: false
keywords:
  - streams
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

Creates, updates, deletes or gets a <code>stream</code> resource or lists <code>streams</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::KinesisVideo::Stream</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kinesisvideo.streams" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Kinesis Video stream.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the Kinesis Video stream.</td></tr>
<tr><td><CopyableCode code="data_retention_in_hours" /></td><td><code>integer</code></td><td>The number of hours till which Kinesis Video will retain the data in the stream</td></tr>
<tr><td><CopyableCode code="device_name" /></td><td><code>string</code></td><td>The name of the device that is writing to the stream.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>AWS KMS key ID that Kinesis Video Streams uses to encrypt stream data.</td></tr>
<tr><td><CopyableCode code="media_type" /></td><td><code>string</code></td><td>The media type of the stream. Consumers of the stream can use this information when processing the stream.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs associated with the Kinesis Video Stream.</td></tr>
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

Gets all properties from a <code>stream</code>.
```sql
SELECT
region,
arn,
name,
data_retention_in_hours,
device_name,
kms_key_id,
media_type,
tags
FROM aws.kinesisvideo.streams
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>stream</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.kinesisvideo.streams (
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
INSERT INTO aws.kinesisvideo.streams (
 Name,
 DataRetentionInHours,
 DeviceName,
 KmsKeyId,
 MediaType,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ DataRetentionInHours }}',
 '{{ DeviceName }}',
 '{{ KmsKeyId }}',
 '{{ MediaType }}',
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
  - name: stream
    props:
      - name: Name
        value: '{{ Name }}'
      - name: DataRetentionInHours
        value: '{{ DataRetentionInHours }}'
      - name: DeviceName
        value: '{{ DeviceName }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: MediaType
        value: '{{ MediaType }}'
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
DELETE FROM aws.kinesisvideo.streams
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>streams</code> resource, the following permissions are required:

### Create
```json
kinesisvideo:DescribeStream,
kinesisvideo:CreateStream
```

### Read
```json
kinesisvideo:DescribeStream
```

### Update
```json
kinesisvideo:DescribeStream,
kinesisvideo:UpdateStream,
kinesisvideo:UpdateDataRetention
```

### Delete
```json
kinesisvideo:DescribeStream,
kinesisvideo:DeleteStream
```

