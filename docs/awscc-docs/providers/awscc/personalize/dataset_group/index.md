---
title: dataset_group
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset_group
  - personalize
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>dataset_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>dataset_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.personalize.dataset_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>dataset_group_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the dataset group.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name for the new dataset group.</td></tr>
<tr><td><code>kms_key_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name(ARN) of a AWS Key Management Service (KMS) key used to encrypt the datasets.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The ARN of the AWS Identity and Access Management (IAM) role that has permissions to access the AWS Key Management Service (KMS) key. Supplying an IAM role is only valid when also specifying a KMS key.</td></tr>
<tr><td><code>domain</code></td><td><code>string</code></td><td>The domain of a Domain dataset group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
dataset_group_arn,
name,
kms_key_arn,
role_arn,
domain
FROM awscc.personalize.dataset_group
WHERE region = 'us-east-1'
AND data__Identifier = '{DatasetGroupArn}';
```

## Permissions

To operate on the <code>dataset_group</code> resource, the following permissions are required:

### Read
```json
personalize:DescribeDatasetGroup
```

### Delete
```json
personalize:DescribeDatasetGroup,
personalize:DeleteDatasetGroup
```

