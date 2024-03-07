---
title: db_cluster_parameter_group
hide_title: false
hide_table_of_contents: false
keywords:
  - db_cluster_parameter_group
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
Gets an individual <code>db_cluster_parameter_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_cluster_parameter_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_cluster_parameter_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rds.db_cluster_parameter_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A friendly description for this DB cluster parameter group.</td></tr>
<tr><td><code>family</code></td><td><code>string</code></td><td>The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a DB engine and engine version compatible with that DB cluster parameter group family.</td></tr>
<tr><td><code>parameters</code></td><td><code>object</code></td><td>An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.</td></tr>
<tr><td><code>d_bcluster_parameter_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The list of tags for the cluster parameter group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
family,
parameters,
d_bcluster_parameter_group_name,
tags
FROM awscc.rds.db_cluster_parameter_group
WHERE region = 'us-east-1'
AND data__Identifier = '{DBClusterParameterGroupName}';
```

## Permissions

To operate on the <code>db_cluster_parameter_group</code> resource, the following permissions are required:

### Read
```json
rds:DescribeDBClusterParameterGroups,
rds:DescribeDBClusterParameters,
rds:DescribeEngineDefaultClusterParameters,
rds:ListTagsForResource
```

### Update
```json
rds:AddTagsToResource,
rds:DescribeDBClusterParameterGroups,
rds:DescribeDBClusterParameters,
rds:DescribeDBClusters,
rds:DescribeEngineDefaultClusterParameters,
rds:ListTagsForResource,
rds:ModifyDBClusterParameterGroup,
rds:RemoveTagsFromResource,
rds:ResetDBClusterParameterGroup
```

### Delete
```json
rds:DeleteDBClusterParameterGroup
```

