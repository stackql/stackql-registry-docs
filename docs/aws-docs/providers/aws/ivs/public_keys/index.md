---
title: public_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - public_keys
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

Creates, updates, deletes or gets a <code>public_key</code> resource or lists <code>public_keys</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::PublicKey</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.public_keys" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the public key to be imported. The value does not need to be unique.</td></tr>
<tr><td><CopyableCode code="public_key_material" /></td><td><code>string</code></td><td>The public portion of a customer-generated key pair.</td></tr>
<tr><td><CopyableCode code="fingerprint" /></td><td><code>string</code></td><td>Key-pair identifier.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Key-pair identifier.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset model.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-publickey.html"><code>AWS::IVS::PublicKey</code></a>.

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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>public_keys</code> in a region.
```sql
SELECT
region,
name,
public_key_material,
fingerprint,
arn,
tags
FROM aws.ivs.public_keys
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>public_key</code>.
```sql
SELECT
region,
name,
public_key_material,
fingerprint,
arn,
tags
FROM aws.ivs.public_keys
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>public_key</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ivs.public_keys (
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
/*+ create */
INSERT INTO aws.ivs.public_keys (
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
  - name: public_key
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

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ivs.public_keys
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>public_keys</code> resource, the following permissions are required:

### Create
```json
ivs:ImportPublicKey,
ivs:TagResource
```

### Read
```json
ivs:GetPublicKey
```

### Update
```json
ivs:GetPublicKey,
ivs:ListTagsForResource,
ivs:UntagResource,
ivs:TagResource
```

### Delete
```json
ivs:DeletePublicKey,
ivs:UntagResource
```

### List
```json
ivs:ListPublicKeys,
ivs:ListTagsForResource
```
