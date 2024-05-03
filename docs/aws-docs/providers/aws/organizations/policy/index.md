---
title: policy
hide_title: false
hide_table_of_contents: false
keywords:
  - policy
  - organizations
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

Gets or operates on an individual <code>policy</code> resource, use <code>policies</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Policies in AWS Organizations enable you to manage different features of the AWS accounts in your organization.  You can use policies when all features are enabled in your organization.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.organizations.policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the Policy</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of policy to create. You can specify one of the following values: AISERVICES_OPT_OUT_POLICY, BACKUP_POLICY, SERVICE_CONTROL_POLICY, TAG_POLICY</td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>object</code></td><td>The Policy text content. For AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Human readable description of the policy</td></tr>
<tr><td><CopyableCode code="target_ids" /></td><td><code>array</code></td><td>List of unique identifiers (IDs) of the root, OU, or account that you want to attach the policy to</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags that you want to attach to the newly created policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id of the Policy</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN of the Policy</td></tr>
<tr><td><CopyableCode code="aws_managed" /></td><td><code>boolean</code></td><td>A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
name,
type,
content,
description,
target_ids,
tags,
id,
arn,
aws_managed
FROM aws.organizations.policy
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>policy</code> resource, the following permissions are required:

### Read
```json
organizations:DescribePolicy,
organizations:ListTargetsForPolicy,
organizations:ListTagsForResource
```

### Update
```json
organizations:AttachPolicy,
organizations:DetachPolicy,
organizations:UpdatePolicy,
organizations:ListTagsForResource,
organizations:ListTargetsForPolicy,
organizations:TagResource,
organizations:UntagResource,
organizations:DescribePolicy
```

### Delete
```json
organizations:DetachPolicy,
organizations:DeletePolicy
```

