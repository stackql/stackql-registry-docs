---
title: key
hide_title: false
hide_table_of_contents: false
keywords:
  - key
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
Gets an individual <code>key</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>key</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kms.key</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.</td></tr>
<tr><td><code>enabled</code></td><td><code>boolean</code></td><td>Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.</td></tr>
<tr><td><code>enable_key_rotation</code></td><td><code>boolean</code></td><td>Enables automatic rotation of the key material for the specified AWS KMS key. By default, automation key rotation is not enabled.</td></tr>
<tr><td><code>key_policy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>key_usage</code></td><td><code>string</code></td><td>Determines the cryptographic operations for which you can use the AWS KMS key. The default value is ENCRYPT_DECRYPT. This property is required only for asymmetric AWS KMS keys. You can't change the KeyUsage value after the AWS KMS key is created.</td></tr>
<tr><td><code>key_spec</code></td><td><code>string</code></td><td>Specifies the type of AWS KMS key to create. The default value is SYMMETRIC_DEFAULT. This property is required only for asymmetric AWS KMS keys. You can't change the KeySpec value after the AWS KMS key is created.</td></tr>
<tr><td><code>multi_region</code></td><td><code>boolean</code></td><td>Specifies whether the AWS KMS key should be Multi-Region. You can't change the MultiRegion value after the AWS KMS key is created.</td></tr>
<tr><td><code>pending_window_in_days</code></td><td><code>integer</code></td><td>Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
enabled,
enable_key_rotation,
key_policy,
key_usage,
key_spec,
multi_region,
pending_window_in_days,
tags,
arn,
key_id
FROM aws.kms.key
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;KeyId&gt;'
```
