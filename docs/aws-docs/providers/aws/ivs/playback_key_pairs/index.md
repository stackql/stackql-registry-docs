---
title: playback_key_pairs
hide_title: false
hide_table_of_contents: false
keywords:
  - playback_key_pairs
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


Used to retrieve a list of <code>playback_key_pairs</code> in a region or to create or delete a <code>playback_key_pairs</code> resource, use <code>playback_key_pair</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>playback_key_pairs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::PlaybackKeyPair</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.playback_key_pairs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Key-pair identifier.</td></tr>
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
arn
FROM aws.ivs.playback_key_pairs
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>playback_key_pair</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- playback_key_pair.iql (required properties only)
INSERT INTO aws.ivs.playback_key_pairs (
 Name,
 PublicKeyMaterial,
 Tags,
 region
)
SELECT 
'{{ Name }}',
 '{{ PublicKeyMaterial }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- playback_key_pair.iql (all properties)
INSERT INTO aws.ivs.playback_key_pairs (
 Name,
 PublicKeyMaterial,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ PublicKeyMaterial }}',
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
  - name: playback_key_pair
    props:
      - name: Name
        value: '{{ Name }}'
      - name: PublicKeyMaterial
        value: '{{ PublicKeyMaterial }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ivs.playback_key_pairs
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>playback_key_pairs</code> resource, the following permissions are required:

### Create
```json
ivs:ImportPlaybackKeyPair,
ivs:TagResource
```

### Delete
```json
ivs:DeletePlaybackKeyPair,
ivs:UntagResource
```

### List
```json
ivs:ListPlaybackKeyPairs,
ivs:ListTagsForResource
```

