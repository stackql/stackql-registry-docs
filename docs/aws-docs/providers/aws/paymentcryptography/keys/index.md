---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - paymentcryptography
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

Creates, updates, deletes or gets a <code>key</code> resource or lists <code>keys</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::PaymentCryptography::Key Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.paymentcryptography.keys" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="exportable" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="key_attributes" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="key_check_value_algorithm" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="key_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="key_origin" /></td><td><code>string</code></td><td>Defines the source of a key</td></tr>
<tr><td><CopyableCode code="key_state" /></td><td><code>string</code></td><td>Defines the state of a key</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="Exportable, KeyAttributes, region" /></td>
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
Gets all <code>keys</code> in a region.
```sql
SELECT
region,
enabled,
exportable,
key_attributes,
key_check_value_algorithm,
key_identifier,
key_origin,
key_state,
tags
FROM aws.paymentcryptography.keys
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>key</code>.
```sql
SELECT
region,
enabled,
exportable,
key_attributes,
key_check_value_algorithm,
key_identifier,
key_origin,
key_state,
tags
FROM aws.paymentcryptography.keys
WHERE region = 'us-east-1' AND data__Identifier = '<KeyIdentifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>key</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.paymentcryptography.keys (
 Exportable,
 KeyAttributes,
 region
)
SELECT 
'{{ Exportable }}',
 '{{ KeyAttributes }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.paymentcryptography.keys (
 Enabled,
 Exportable,
 KeyAttributes,
 KeyCheckValueAlgorithm,
 Tags,
 region
)
SELECT 
 '{{ Enabled }}',
 '{{ Exportable }}',
 '{{ KeyAttributes }}',
 '{{ KeyCheckValueAlgorithm }}',
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
  - name: key
    props:
      - name: Enabled
        value: '{{ Enabled }}'
      - name: Exportable
        value: '{{ Exportable }}'
      - name: KeyAttributes
        value:
          KeyUsage: '{{ KeyUsage }}'
          KeyClass: '{{ KeyClass }}'
          KeyAlgorithm: '{{ KeyAlgorithm }}'
          KeyModesOfUse:
            Encrypt: '{{ Encrypt }}'
            Decrypt: '{{ Decrypt }}'
            Wrap: '{{ Wrap }}'
            Unwrap: '{{ Unwrap }}'
            Generate: '{{ Generate }}'
            Sign: '{{ Sign }}'
            Verify: '{{ Verify }}'
            DeriveKey: '{{ DeriveKey }}'
            NoRestrictions: '{{ NoRestrictions }}'
      - name: KeyCheckValueAlgorithm
        value: '{{ KeyCheckValueAlgorithm }}'
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
DELETE FROM aws.paymentcryptography.keys
WHERE data__Identifier = '<KeyIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>keys</code> resource, the following permissions are required:

### Create
```json
payment-cryptography:GetKey,
payment-cryptography:CreateKey,
payment-cryptography:TagResource
```

### Read
```json
payment-cryptography:GetKey,
payment-cryptography:ListTagsForResource
```

### Update
```json
payment-cryptography:GetKey,
payment-cryptography:ListTagsForResource,
payment-cryptography:TagResource,
payment-cryptography:UntagResource,
payment-cryptography:StartKeyUsage,
payment-cryptography:StopKeyUsage
```

### Delete
```json
payment-cryptography:GetKey,
payment-cryptography:DeleteKey
```

### List
```json
payment-cryptography:ListKeys
```

