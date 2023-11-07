---
title: replica_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - replica_keys
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
Retrieves a list of <code>replica_keys</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replica_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>replica_keys</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kms.replica_keys</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>PrimaryKeyArn</code></td><td><code>string</code></td><td>Identifies the primary AWS KMS key to create a replica of. Specify the Amazon Resource Name (ARN) of the AWS KMS key. You cannot specify an alias or key ID. For help finding the ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.</td></tr>
<tr><td><code>Enabled</code></td><td><code>boolean</code></td><td>Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.</td></tr>
<tr><td><code>KeyPolicy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PendingWindowInDays</code></td><td><code>integer</code></td><td>Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>KeyId</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.kms.replica_keys<br/>WHERE region = 'us-east-1'
</pre>
