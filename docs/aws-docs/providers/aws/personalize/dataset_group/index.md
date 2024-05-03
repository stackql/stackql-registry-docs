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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>dataset_group</code> resource, use <code>dataset_groups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::Personalize::DatasetGroup.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.personalize.dataset_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="dataset_group_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the dataset group.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the new dataset group.</td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name(ARN) of a AWS Key Management Service (KMS) key used to encrypt the datasets.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the AWS Identity and Access Management (IAM) role that has permissions to access the AWS Key Management Service (KMS) key. Supplying an IAM role is only valid when also specifying a KMS key.</td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td>The domain of a Domain dataset group.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
dataset_group_arn,
name,
kms_key_arn,
role_arn,
domain
FROM aws.personalize.dataset_group
WHERE data__Identifier = '<DatasetGroupArn>';
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

