---
title: encoder_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - encoder_configurations
  - ivs
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

Creates, updates, deletes or gets an <code>encoder_configuration</code> resource or lists <code>encoder_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>encoder_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::EncoderConfiguration.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.encoder_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Encoder configuration identifier.</td></tr>
<tr><td><CopyableCode code="video" /></td><td><code>object</code></td><td>Video configuration. Default: video resolution 1280x720, bitrate 2500 kbps, 30 fps</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Encoder configuration name.</td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>encoder_configurations</code> in a region.
```sql
SELECT
region,
arn
FROM aws.ivs.encoder_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an <code>encoder_configuration</code>.
```sql
SELECT
region,
arn,
video,
name,
tags
FROM aws.ivs.encoder_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>encoder_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ivs.encoder_configurations (
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
INSERT INTO aws.ivs.encoder_configurations (
 Video,
 Name,
 Tags,
 region
)
SELECT 
 '{{ Video }}',
 '{{ Name }}',
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
  - name: encoder_configuration
    props:
      - name: Video
        value:
          Bitrate: '{{ Bitrate }}'
          Framerate: null
          Height: '{{ Height }}'
          Width: '{{ Width }}'
      - name: Name
        value: '{{ Name }}'
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
DELETE FROM aws.ivs.encoder_configurations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>encoder_configurations</code> resource, the following permissions are required:

### Create
```json
ivs:CreateEncoderConfiguration,
ivs:TagResource
```

### Read
```json
ivs:GetEncoderConfiguration,
ivs:ListTagsForResource
```

### Update
```json
ivs:GetEncoderConfiguration,
ivs:ListTagsForResource,
ivs:UntagResource,
ivs:TagResource
```

### Delete
```json
ivs:DeleteEncoderConfiguration,
ivs:UntagResource
```

### List
```json
ivs:ListEncoderConfigurations,
ivs:ListTagsForResource
```

