---
title: alias
hide_title: false
hide_table_of_contents: false
keywords:
  - alias
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
Gets or operates on an individual <code>alias</code> resource, use <code>aliases</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::KMS::Alias`` resource specifies a display name for a &#91;KMS key&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;concepts.html#kms_keys). You can use an alias to identify a KMS key in the KMS console, in the &#91;DescribeKey&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_DescribeKey.html) operation, and in &#91;cryptographic operations&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;concepts.html#cryptographic-operations), such as &#91;Decrypt&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_Decrypt.html) and &#91;GenerateDataKey&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_GenerateDataKey.html).&lt;br&#x2F;&gt;  Adding, deleting, or updating an alias can allow or deny permission to the KMS key. For details, see &#91;ABAC for&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;abac.html) in the *Developer Guide*.&lt;br&#x2F;&gt;  Using an alias to refer to a KMS key can help you simplify key management. For example, an alias in your code can be associated with different KMS keys i</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kms.alias</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>target_key_id</code></td><td><code>string</code></td><td>Associates the alias with the specified &#91;&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;concepts.html#customer-cmk). The KMS key must be in the same AWS-account and Region.&lt;br&#x2F;&gt; A valid key ID is required. If you supply a null or empty string value, this operation returns an error.&lt;br&#x2F;&gt; For help finding the key ID and ARN, see &#91;Finding the key ID and ARN&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;viewing-keys.html#find-cmk-id-arn) in the *Developer Guide*.&lt;br&#x2F;&gt; Specify the key ID or the key ARN of the KMS key.&lt;br&#x2F;&gt; For example:&lt;br&#x2F;&gt;  +  Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab`` &lt;br&#x2F;&gt;  +  Key ARN: ``arn:aws:kms:us-east-2:111122223333:key&#x2F;1234abcd-12ab-34cd-56ef-1234567890ab`` &lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; To get the key ID and key ARN for a KMS key, use &#91;ListKeys&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_ListKeys.html) or &#91;DescribeKey&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_DescribeKey.html).</td></tr>
<tr><td><code>alias_name</code></td><td><code>string</code></td><td>Specifies the alias name. This value must begin with ``alias&#x2F;`` followed by a name, such as ``alias&#x2F;ExampleAlias``. &lt;br&#x2F;&gt;  If you change the value of the ``AliasName`` property, the existing alias is deleted and a new alias is created for the specified KMS key. This change can disrupt applications that use the alias. It can also allow or deny access to a KMS key affected by attribute-based access control (ABAC).&lt;br&#x2F;&gt;  The alias must be string of 1-256 characters. It can contain only alphanumeric characters, forward slashes (&#x2F;), underscores (_), and dashes (-). The alias name cannot begin with ``alias&#x2F;aws&#x2F;``. The ``alias&#x2F;aws&#x2F;`` prefix is reserved for &#91;&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;concepts.html#aws-managed-cmk).</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
target_key_id,
alias_name
FROM aws.kms.alias
WHERE data__Identifier = '<AliasName>';
```

## Permissions

To operate on the <code>alias</code> resource, the following permissions are required:

### Read
```json
kms:ListAliases
```

### Update
```json
kms:UpdateAlias
```

### Delete
```json
kms:DeleteAlias
```

