---
title: verified_access_group
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_access_group
  - ec2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>verified_access_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_access_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>verified_access_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.verified_access_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>verified_access_group_id</code></td><td><code>string</code></td><td>The ID of the AWS Verified Access group.</td></tr>
<tr><td><code>verified_access_instance_id</code></td><td><code>string</code></td><td>The ID of the AWS Verified Access instance.</td></tr>
<tr><td><code>verified_access_group_arn</code></td><td><code>string</code></td><td>The ARN of the Verified Access group.</td></tr>
<tr><td><code>owner</code></td><td><code>string</code></td><td>The AWS account number that owns the group.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>Time this Verified Access Group was created.</td></tr>
<tr><td><code>last_updated_time</code></td><td><code>string</code></td><td>Time this Verified Access Group was last updated.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description for the AWS Verified Access group.</td></tr>
<tr><td><code>policy_document</code></td><td><code>string</code></td><td>The AWS Verified Access policy document.</td></tr>
<tr><td><code>policy_enabled</code></td><td><code>boolean</code></td><td>The status of the Verified Access policy.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>sse_specification</code></td><td><code>object</code></td><td>The configuration options for customer provided KMS encryption.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
verified_access_group_id,
verified_access_instance_id,
verified_access_group_arn,
owner,
creation_time,
last_updated_time,
description,
policy_document,
policy_enabled,
tags,
sse_specification
FROM awscc.ec2.verified_access_group
WHERE data__Identifier = '<VerifiedAccessGroupId>';
```

## Permissions

To operate on the <code>verified_access_group</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeVerifiedAccessGroups,
ec2:GetVerifiedAccessGroupPolicy,
ec2:DescribeTags,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

### Update
```json
ec2:ModifyVerifiedAccessGroup,
ec2:ModifyVerifiedAccessGroupPolicy,
ec2:DescribeVerifiedAccessGroups,
ec2:GetVerifiedAccessGroupPolicy,
ec2:DescribeTags,
ec2:DeleteTags,
ec2:CreateTags,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
ec2:DeleteVerifiedAccessGroup,
ec2:DeleteTags,
ec2:DescribeVerifiedAccessGroups,
ec2:DescribeTags,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

