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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>cluster_parameter_group</code> resource, use <code>cluster_parameter_groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_parameter_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Redshift::ClusterParameterGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.cluster_parameter_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="parameter_group_name" /></td><td><code>string</code></td><td>The name of the cluster parameter group.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the parameter group.</td></tr>
<tr><td><CopyableCode code="parameter_group_family" /></td><td><code>string</code></td><td>The Amazon Redshift engine version to which the cluster parameter group applies. The cluster engine version determines the set of parameters.</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>array</code></td><td>An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
parameter_group_name,
description,
parameter_group_family,
parameters,
tags
FROM aws.redshift.cluster_parameter_group
WHERE region = 'us-east-1' AND data__Identifier = '<ParameterGroupName>';
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

