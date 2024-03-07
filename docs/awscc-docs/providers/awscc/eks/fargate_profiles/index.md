---
title: fargate_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - fargate_profiles
  - eks
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>fargate_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fargate_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>fargate_profiles</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.eks.fargate_profiles</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster_name</code></td><td><code>string</code></td><td>Name of the Cluster</td></tr>
<tr><td><code>fargate_profile_name</code></td><td><code>string</code></td><td>Name of FargateProfile</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>fargate_profiles</code> resource, the following permissions are required:

### Create
```json
eks:CreateFargateProfile,
eks:DescribeFargateProfile,
iam:GetRole,
iam:PassRole,
iam:CreateServiceLinkedRole,
eks:TagResource
```

### List
```json
eks:ListFargateProfiles
```


## Example
```sql
SELECT
region,
cluster_name,
fargate_profile_name
FROM awscc.eks.fargate_profiles
WHERE region = 'us-east-1'
```
