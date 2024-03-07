---
title: cluster_parameter_group
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_parameter_group
  - redshift
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>cluster_parameter_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_parameter_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cluster_parameter_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.redshift.cluster_parameter_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>parameter_group_name</code></td><td><code>string</code></td><td>The name of the cluster parameter group.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the parameter group.</td></tr>
<tr><td><code>parameter_group_family</code></td><td><code>string</code></td><td>The Amazon Redshift engine version to which the cluster parameter group applies. The cluster engine version determines the set of parameters.</td></tr>
<tr><td><code>parameters</code></td><td><code>array</code></td><td>An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
parameter_group_name,
description,
parameter_group_family,
parameters,
tags
FROM awscc.redshift.cluster_parameter_group
WHERE region = 'us-east-1'
AND data__Identifier = '{ParameterGroupName}';
```

## Permissions

To operate on the <code>cluster_parameter_group</code> resource, the following permissions are required:

### Read
```json
redshift:DescribeClusterParameterGroups,
initech:DescribeReport,
redshift:DescribeClusterParameters,
redshift:DescribeTags
```

### Update
```json
redshift:DescribeClusterParameterGroups,
redshift:ResetClusterParameterGroup,
redshift:ModifyClusterParameterGroup,
redshift:DescribeClusterParameters,
redshift:DescribeTags,
redshift:CreateTags,
redshift:DeleteTags,
initech:UpdateReport
```

### Delete
```json
redshift:DescribeTags,
redshift:DescribeClusterParameterGroups,
redshift:DeleteClusterParameterGroup,
redshift:DescribeClusterParameters,
initech:DeleteReport
```

