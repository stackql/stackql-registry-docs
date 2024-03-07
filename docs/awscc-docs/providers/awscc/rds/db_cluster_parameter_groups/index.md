---
title: db_cluster_parameter_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - db_cluster_parameter_groups
  - rds
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>db_cluster_parameter_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_cluster_parameter_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_cluster_parameter_groups</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rds.db_cluster_parameter_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>d_bcluster_parameter_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>db_cluster_parameter_groups</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
rds:AddTagsToResource,
rds:CreateDBClusterParameterGroup,
rds:DescribeDBClusterParameterGroups,
rds:DescribeDBClusterParameters,
rds:DescribeDBClusters,
rds:DescribeEngineDefaultClusterParameters,
rds:ListTagsForResource,
rds:ModifyDBClusterParameterGroup,
rds:RemoveTagsFromResource
```

### List
```json
rds:DescribeDBClusterParameterGroups
```


## Example
```sql
SELECT
region,
d_bcluster_parameter_group_name
FROM awscc.rds.db_cluster_parameter_groups
WHERE region = 'us-east-1'
```
