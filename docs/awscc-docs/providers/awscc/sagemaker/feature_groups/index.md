---
title: feature_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_groups
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>feature_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feature_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>feature_groups</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.feature_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>feature_group_name</code></td><td><code>string</code></td><td>The Name of the FeatureGroup.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
feature_group_name
FROM awscc.sagemaker.feature_groups
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>feature_groups</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
kms:CreateGrant,
kms:DescribeKey,
glue:CreateTable,
glue:GetTable,
glue:CreateDatabase,
glue:GetDatabase,
sagemaker:CreateFeatureGroup,
sagemaker:DescribeFeatureGroup,
sagemaker:AddTags,
sagemaker:ListTags
```

### List
```json
sagemaker:ListFeatureGroups
```

