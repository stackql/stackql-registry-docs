---
title: replica_keys_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - replica_keys_list_only
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

Lists <code>replica_keys</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/replica_keys/"><code>replica_keys</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replica_keys_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::KMS::ReplicaKey resource specifies a multi-region replica AWS KMS key in AWS Key Management Service (AWS KMS).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kms.replica_keys_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.</td></tr>
<tr><td><CopyableCode code="pending_window_in_days" /></td><td><code>integer</code></td><td>Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.</td></tr>
<tr><td><CopyableCode code="key_policy" /></td><td><code>object</code></td><td>The key policy that authorizes use of the AWS KMS key. The key policy must observe the following rules.</td></tr>
<tr><td><CopyableCode code="primary_key_arn" /></td><td><code>string</code></td><td>Identifies the primary AWS KMS key to create a replica of. Specify the Amazon Resource Name (ARN) of the AWS KMS key. You cannot specify an alias or key ID. For help finding the ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide.</td></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td>Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.</td></tr>
<tr><td><CopyableCode code="key_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>replica_keys</code> in a region.
```sql
SELECT
region,
key_id
FROM aws.kms.replica_keys_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>replica_keys_list_only</code> resource, see <a href="/providers/aws/kms/replica_keys/#permissions"><code>replica_keys</code></a>


