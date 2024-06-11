---
title: partner_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_accounts
  - iotwireless
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

Creates, updates, deletes or gets a <code>partner_account</code> resource or lists <code>partner_accounts</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partner_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage partner account</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.partner_accounts" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="sidewalk" /></td><td><code>object</code></td><td>The Sidewalk account credentials.</td></tr>
<tr><td><CopyableCode code="partner_account_id" /></td><td><code>string</code></td><td>The partner account ID to disassociate from the AWS account</td></tr>
<tr><td><CopyableCode code="partner_type" /></td><td><code>string</code></td><td>The partner type</td></tr>
<tr><td><CopyableCode code="sidewalk_response" /></td><td><code>object</code></td><td>The Sidewalk account credentials.</td></tr>
<tr><td><CopyableCode code="account_linked" /></td><td><code>boolean</code></td><td>Whether the partner account is linked to the AWS account.</td></tr>
<tr><td><CopyableCode code="sidewalk_update" /></td><td><code>object</code></td><td>The Sidewalk account credentials.</td></tr>
<tr><td><CopyableCode code="fingerprint" /></td><td><code>string</code></td><td>The fingerprint of the Sidewalk application server private key.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>PartnerAccount arn. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the destination.</td></tr>
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
List all <code>partner_accounts</code> in a region.
```sql
SELECT
region,
partner_account_id
FROM aws.iotwireless.partner_accounts
WHERE region = 'us-east-1';
```
Gets all properties from a <code>partner_account</code>.
```sql
SELECT
region,
sidewalk,
partner_account_id,
partner_type,
sidewalk_response,
account_linked,
sidewalk_update,
fingerprint,
arn,
tags
FROM aws.iotwireless.partner_accounts
WHERE region = 'us-east-1' AND data__Identifier = '<PartnerAccountId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>partner_account</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotwireless.partner_accounts (
 Sidewalk,
 PartnerAccountId,
 PartnerType,
 SidewalkResponse,
 AccountLinked,
 SidewalkUpdate,
 Tags,
 region
)
SELECT 
'{{ Sidewalk }}',
 '{{ PartnerAccountId }}',
 '{{ PartnerType }}',
 '{{ SidewalkResponse }}',
 '{{ AccountLinked }}',
 '{{ SidewalkUpdate }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotwireless.partner_accounts (
 Sidewalk,
 PartnerAccountId,
 PartnerType,
 SidewalkResponse,
 AccountLinked,
 SidewalkUpdate,
 Tags,
 region
)
SELECT 
 '{{ Sidewalk }}',
 '{{ PartnerAccountId }}',
 '{{ PartnerType }}',
 '{{ SidewalkResponse }}',
 '{{ AccountLinked }}',
 '{{ SidewalkUpdate }}',
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
  - name: partner_account
    props:
      - name: Sidewalk
        value:
          AppServerPrivateKey: '{{ AppServerPrivateKey }}'
      - name: PartnerAccountId
        value: '{{ PartnerAccountId }}'
      - name: PartnerType
        value: '{{ PartnerType }}'
      - name: SidewalkResponse
        value:
          AmazonId: '{{ AmazonId }}'
          Fingerprint: '{{ Fingerprint }}'
          Arn: '{{ Arn }}'
      - name: AccountLinked
        value: '{{ AccountLinked }}'
      - name: SidewalkUpdate
        value:
          AppServerPrivateKey: '{{ AppServerPrivateKey }}'
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
DELETE FROM aws.iotwireless.partner_accounts
WHERE data__Identifier = '<PartnerAccountId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>partner_accounts</code> resource, the following permissions are required:

### Create
```json
iotwireless:AssociateAwsAccountWithPartnerAccount,
iotwireless:TagResource,
iotwireless:ListTagsForResource
```

### Read
```json
iotwireless:GetPartnerAccount,
iotwireless:ListTagsForResource
```

### List
```json
iotwireless:ListPartnerAccounts,
iotwireless:ListTagsForResource
```

### Update
```json
iotwireless:UpdatePartnerAccount,
iotwireless:UntagResource,
iotwireless:ListTagsForResource
```

### Delete
```json
iotwireless:DisassociateAwsAccountFromPartnerAccount
```

