---
title: aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - aliases
  - kms
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
<tr><td><b>Description</b></td><td>The <code>AWS::KMS::Alias</code> resource specifies a display name for a &#91;KMS key&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys). You can use an alias to identify a KMS key in the KMS console, in the &#91;DescribeKey&#93;(https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html) operation, and in &#91;cryptographic operations&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations), such as &#91;Decrypt&#93;(https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) and &#91;GenerateDataKey&#93;(https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html).<br />Adding, deleting, or updating an alias can allow or deny permission to the KMS key. For details, see &#91;ABAC for&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/abac.html) in the *Developer Guide*.<br />Using an alias to refer to a KMS key can help you simplify key management. For example, an alias in your code can be associated with different KMS keys in different AWS-Regions. For more information, see &#91;Using aliases&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/kms-alias.html) in the *Developer Guide*.<br />When specifying an alias, observe the following rules.<br />+ Each alias is associated with one KMS key, but multiple aliases can be associated with the same KMS key.<br />+ The alias and its associated KMS key must be in the same AWS-account and Region.<br />+ The alias name must be unique in the AWS-account and Region. However, you can create aliases with the same name in different AWS-Regions. For example, you can have an <code>alias/projectKey</code> in multiple Regions, each of which is associated with a KMS key in its Region.<br />+ Each alias name must begin with <code>alias/</code> followed by a name, such as <code>alias/exampleKey</code>. The alias name can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). Alias names cannot begin with <code>alias/aws/</code>. That alias name prefix is reserved for &#91;&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk).<br /><br />*Regions* <br />KMS CloudFormation resources are available in all AWS-Regions in which KMS and CFN are supported.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kms.aliases" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="target_key_id" /></td><td><code>string</code></td><td>Associates the alias with the specified &#91;&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk). The KMS key must be in the same AWS-account and Region.<br />A valid key ID is required. If you supply a null or empty string value, this operation returns an error.<br />For help finding the key ID and ARN, see &#91;Finding the key ID and ARN&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html#find-cmk-id-arn) in the *Developer Guide*.<br />Specify the key ID or the key ARN of the KMS key.<br />For example:<br />+ Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> <br />+ Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> <br /><br />To get the key ID and key ARN for a KMS key, use &#91;ListKeys&#93;(https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html) or &#91;DescribeKey&#93;(https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html).</td></tr>
<tr><td><CopyableCode code="alias_name" /></td><td><code>string</code></td><td>Specifies the alias name. This value must begin with <code>alias/</code> followed by a name, such as <code>alias/ExampleAlias</code>. <br />If you change the value of the <code>AliasName</code> property, the existing alias is deleted and a new alias is created for the specified KMS key. This change can disrupt applications that use the alias. It can also allow or deny access to a KMS key affected by attribute-based access control (ABAC).<br />The alias must be string of 1-256 characters. It can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). The alias name cannot begin with <code>alias/aws/</code>. The <code>alias/aws/</code> prefix is reserved for &#91;&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk).</td></tr>
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
    <td><CopyableCode code="AliasName, TargetKeyId, region" /></td>
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
List all <code>aliases</code> in a region.
```sql
SELECT
region,
alias_name
FROM aws.kms.aliases
WHERE region = 'us-east-1';
```
Gets all properties from an <code>alias</code>.
```sql
SELECT
region,
target_key_id,
alias_name
FROM aws.kms.aliases
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
INSERT INTO aws.kms.aliases (
 TargetKeyId,
 AliasName,
 region
)
SELECT 
'{{ TargetKeyId }}',
 '{{ AliasName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.kms.aliases (
 TargetKeyId,
 AliasName,
 region
)
SELECT 
 '{{ TargetKeyId }}',
 '{{ AliasName }}',
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
      - name: TargetKeyId
        value: '{{ TargetKeyId }}'
      - name: AliasName
        value: '{{ AliasName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.kms.aliases
WHERE data__Identifier = '<AliasName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>aliases</code> resource, the following permissions are required:

### Read
```json
kms:ListAliases
```

### Create
```json
kms:CreateAlias
```

### Update
```json
kms:UpdateAlias
```

### List
```json
kms:ListAliases
```

### Delete
```json
kms:DeleteAlias
```

