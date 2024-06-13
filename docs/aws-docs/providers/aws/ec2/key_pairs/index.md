---
title: key_pairs
hide_title: false
hide_table_of_contents: false
keywords:
  - key_pairs
  - ec2
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

Creates, updates, deletes or gets a <code>key_pair</code> resource or lists <code>key_pairs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_pairs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a key pair for use with an EC2long instance as follows:<br />+ To import an existing key pair, include the <code>PublicKeyMaterial</code> property.<br />+ To create a new key pair, omit the <code>PublicKeyMaterial</code> property.<br /><br />When you import an existing key pair, you specify the public key material for the key. We assume that you have the private key material for the key. CFNlong does not create or return the private key material when you import a key pair.<br />When you create a new key pair, the private key is saved to SYSlong Parameter Store, using a parameter with the following name: <code>/ec2/keypair/&#123;key_pair_id&#125;</code>. For more information about retrieving private key, and the required permissions, see &#91;Create a key pair using&#93;(https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html#create-key-pair-cloudformation) in the *User Guide*.<br />When CFN deletes a key pair that was created or imported by a stack, it also deletes the parameter that was used to store the private key material in Parameter Store.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.key_pairs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="key_name" /></td><td><code>string</code></td><td>A unique name for the key pair.<br />Constraints: Up to 255 ASCII characters</td></tr>
<tr><td><CopyableCode code="key_type" /></td><td><code>string</code></td><td>The type of key pair. Note that ED25519 keys are not supported for Windows instances.<br />If the <code>PublicKeyMaterial</code> property is specified, the <code>KeyType</code> property is ignored, and the key type is inferred from the <code>PublicKeyMaterial</code> value.<br />Default: <code>rsa</code></td></tr>
<tr><td><CopyableCode code="key_format" /></td><td><code>string</code></td><td>The format of the key pair.<br />Default: <code>pem</code></td></tr>
<tr><td><CopyableCode code="public_key_material" /></td><td><code>string</code></td><td>The public key material. The <code>PublicKeyMaterial</code> property is used to import a key pair. If this property is not specified, then a new key pair will be created.</td></tr>
<tr><td><CopyableCode code="key_fingerprint" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="key_pair_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to apply to the key pair.</td></tr>
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
    <td><CopyableCode code="KeyName, region" /></td>
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
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>key_pairs</code> in a region.
```sql
SELECT
region,
key_name
FROM aws.ec2.key_pairs
WHERE region = 'us-east-1';
```
Gets all properties from a <code>key_pair</code>.
```sql
SELECT
region,
key_name,
key_type,
key_format,
public_key_material,
key_fingerprint,
key_pair_id,
tags
FROM aws.ec2.key_pairs
WHERE region = 'us-east-1' AND data__Identifier = '<KeyName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>key_pair</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.key_pairs (
 KeyName,
 region
)
SELECT 
'{{ KeyName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.key_pairs (
 KeyName,
 KeyType,
 KeyFormat,
 PublicKeyMaterial,
 Tags,
 region
)
SELECT 
 '{{ KeyName }}',
 '{{ KeyType }}',
 '{{ KeyFormat }}',
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
  - name: key_pair
    props:
      - name: KeyName
        value: '{{ KeyName }}'
      - name: KeyType
        value: '{{ KeyType }}'
      - name: KeyFormat
        value: '{{ KeyFormat }}'
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
DELETE FROM aws.ec2.key_pairs
WHERE data__Identifier = '<KeyName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>key_pairs</code> resource, the following permissions are required:

### Create
```json
ec2:CreateKeyPair,
ec2:ImportKeyPair,
ec2:CreateTags,
ssm:PutParameter
```

### Read
```json
ec2:DescribeKeyPairs
```

### List
```json
ec2:DescribeKeyPairs
```

### Delete
```json
ec2:DeleteKeyPair,
ssm:DeleteParameter,
ec2:DescribeKeyPairs
```

