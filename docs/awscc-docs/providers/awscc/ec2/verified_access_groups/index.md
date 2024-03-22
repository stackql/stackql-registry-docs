---
title: verified_access_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_access_groups
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
Retrieves a list of <code>verified_access_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_access_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>verified_access_groups</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.verified_access_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>verified_access_group_id</code></td><td><code>string</code></td><td>The ID of the AWS Verified Access group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
verified_access_group_id
FROM awscc.ec2.verified_access_groups
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>verified_access_groups</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVerifiedAccessGroup,
ec2:DescribeVerifiedAccessGroups,
ec2:GetVerifiedAccessGroupPolicy,
ec2:CreateTags,
ec2:DescribeTags,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

### List
```json
ec2:DescribeVerifiedAccessGroups,
ec2:DescribeTags,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

