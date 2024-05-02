---
title: fargate_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - fargate_profile
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
Gets or operates on an individual <code>fargate_profile</code> resource, use <code>fargate_profiles</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fargate_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::EKS::FargateProfile</td></tr>
<tr><td><b>Id</b></td><td><code>aws.eks.fargate_profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster_name</code></td><td><code>string</code></td><td>Name of the Cluster</td></tr>
<tr><td><code>fargate_profile_name</code></td><td><code>string</code></td><td>Name of FargateProfile</td></tr>
<tr><td><code>pod_execution_role_arn</code></td><td><code>string</code></td><td>The IAM policy arn for pods</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subnets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>selectors</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
cluster_name,
fargate_profile_name,
pod_execution_role_arn,
arn,
subnets,
selectors,
tags
FROM aws.eks.fargate_profile
WHERE data__Identifier = '<ClusterName>|<FargateProfileName>';
```

## Permissions

To operate on the <code>fargate_profile</code> resource, the following permissions are required:

### Read
```json
eks:DescribeFargateProfile
```

### Delete
```json
eks:DeleteFargateProfile,
eks:DescribeFargateProfile
```

### Update
```json
eks:DescribeFargateProfile,
eks:ListTagsForResource,
eks:TagResource,
eks:UntagResource
```

