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


Used to retrieve a list of <code>aliases</code> in a region or to create or delete a <code>aliases</code> resource, use <code>alias</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::KMS::Alias</code> resource specifies a display name for a &#91;KMS key&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;concepts.html#kms_keys). You can use an alias to identify a KMS key in the KMS console, in the &#91;DescribeKey&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_DescribeKey.html) operation, and in &#91;cryptographic operations&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;concepts.html#cryptographic-operations), such as &#91;Decrypt&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_Decrypt.html) and &#91;GenerateDataKey&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_GenerateDataKey.html).&lt;br&#x2F;&gt;  Adding, deleting, or updating an alias can allow or deny permission to the KMS key. For details, see &#91;ABAC for&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;abac.html) in the *Developer Guide*.&lt;br&#x2F;&gt;  Using an alias to refer to a KMS key can help you simplify key management. For example, an alias in your code can be associated with different KMS keys i</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kms.aliases" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="alias_name" /></td><td><code>string</code></td><td>Specifies the alias name. This value must begin with <code>alias&#x2F;</code> followed by a name, such as <code>alias&#x2F;ExampleAlias</code>. &lt;br&#x2F;&gt;  If you change the value of the <code>AliasName</code> property, the existing alias is deleted and a new alias is created for the specified KMS key. This change can disrupt applications that use the alias. It can also allow or deny access to a KMS key affected by attribute-based access control (ABAC).&lt;br&#x2F;&gt;  The alias must be string of 1-256 characters. It can contain only alphanumeric characters, forward slashes (&#x2F;), underscores (_), and dashes (-). The alias name cannot begin with <code>alias&#x2F;aws&#x2F;</code>. The <code>alias&#x2F;aws&#x2F;</code> prefix is reserved for &#91;&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;concepts.html#aws-managed-cmk).</td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
alias_name
FROM aws.kms.aliases
WHERE region = 'us-east-1';
```

## `INSERT` Example

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

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.kms.aliases
WHERE data__Identifier = '<AliasName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>aliases</code> resource, the following permissions are required:

### Create
```json
kms:CreateAlias
```

### List
```json
kms:ListAliases
```

### Delete
```json
kms:DeleteAlias
```

