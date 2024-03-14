---
title: replica_key
hide_title: false
hide_table_of_contents: false
keywords:
  - replica_key
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
Gets an individual <code>replica_key</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replica_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>replica_key</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.kms.replica_key</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.</td></tr>
<tr><td><code>pending_window_in_days</code></td><td><code>integer</code></td><td>Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.</td></tr>
<tr><td><code>key_policy</code></td><td><code>object</code></td><td>The key policy that authorizes use of the AWS KMS key. The key policy must observe the following rules.</td></tr>
<tr><td><code>primary_key_arn</code></td><td><code>string</code></td><td>Identifies the primary AWS KMS key to create a replica of. Specify the Amazon Resource Name (ARN) of the AWS KMS key. You cannot specify an alias or key ID. For help finding the ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide.</td></tr>
<tr><td><code>enabled</code></td><td><code>boolean</code></td><td>Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.</td></tr>
<tr><td><code>key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
pending_window_in_days,
key_policy,
primary_key_arn,
enabled,
key_id,
arn,
tags
FROM awscc.kms.replica_key
WHERE data__Identifier = '<KeyId>';
```

## Permissions

To operate on the <code>replica_key</code> resource, the following permissions are required:

### Read
```json
kms:DescribeKey,
kms:GetKeyPolicy,
kms:ListResourceTags
```

### Update
```json
kms:DescribeKey,
kms:DisableKey,
kms:EnableKey,
kms:PutKeyPolicy,
kms:TagResource,
kms:UntagResource,
kms:UpdateKeyDescription
```

### Delete
```json
kms:DescribeKey,
kms:ScheduleKeyDeletion
```

