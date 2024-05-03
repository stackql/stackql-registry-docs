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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>fargate_profile</code> resource, use <code>fargate_profiles</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fargate_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::EKS::FargateProfile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.fargate_profile" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>Name of the Cluster</td></tr>
<tr><td><CopyableCode code="fargate_profile_name" /></td><td><code>string</code></td><td>Name of FargateProfile</td></tr>
<tr><td><CopyableCode code="pod_execution_role_arn" /></td><td><code>string</code></td><td>The IAM policy arn for pods</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subnets" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="selectors" /></td><td><code>array</code></td><td></td></tr>
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

