---
title: aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - aliases
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

Creates, updates, deletes or gets an <code>alias</code> resource or lists <code>aliases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::PaymentCryptography::Alias Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.paymentcryptography.aliases" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="alias_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="key_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="AliasName, region" /></td>
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
Gets all <code>aliases</code> in a region.
```sql
SELECT
region,
alias_name,
key_arn
FROM aws.paymentcryptography.aliases
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>alias</code>.
```sql
SELECT
region,
alias_name,
key_arn
FROM aws.paymentcryptography.aliases
WHERE region = 'us-east-1' AND data__Identifier = '<AliasName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>alias</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.paymentcryptography.aliases (
 AliasName,
 region
)
SELECT 
'{{ AliasName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.paymentcryptography.aliases (
 AliasName,
 KeyArn,
 region
)
SELECT 
 '{{ AliasName }}',
 '{{ KeyArn }}',
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
  - name: alias
    props:
      - name: AliasName
        value: '{{ AliasName }}'
      - name: KeyArn
        value: '{{ KeyArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.paymentcryptography.aliases
WHERE data__Identifier = '<AliasName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>aliases</code> resource, the following permissions are required:

### Create
```json
payment-cryptography:CreateAlias
```

### Read
```json
payment-cryptography:GetAlias
```

### Update
```json
payment-cryptography:UpdateAlias
```

### Delete
```json
payment-cryptography:DeleteAlias
```

### List
```json
payment-cryptography:ListAliases
```

