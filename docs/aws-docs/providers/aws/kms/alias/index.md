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
Gets an individual <code>alias</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>alias</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kms.alias</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>alias_name</code></td><td><code>string</code></td><td>Specifies the alias name. This value must begin with alias&#x2F; followed by a name, such as alias&#x2F;ExampleAlias. The alias name cannot begin with alias&#x2F;aws&#x2F;. The alias&#x2F;aws&#x2F; prefix is reserved for AWS managed keys.</td></tr>
<tr><td><code>target_key_id</code></td><td><code>string</code></td><td>Identifies the AWS KMS key to which the alias refers. Specify the key ID or the Amazon Resource Name (ARN) of the AWS KMS key. You cannot specify another alias. For help finding the key ID and ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
alias_name,
target_key_id
FROM aws.kms.alias
WHERE region = 'us-east-1'
AND data__Identifier = '<AliasName>'
```
