---
title: cluster_subnet_group
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_subnet_group
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


Gets or updates an individual <code>cluster_subnet_group</code> resource, use <code>cluster_subnet_groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_subnet_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies an Amazon Redshift subnet group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.cluster_subnet_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the parameter group.</td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>The list of VPC subnet IDs</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The list of tags for the cluster parameter group.</td></tr>
<tr><td><CopyableCode code="cluster_subnet_group_name" /></td><td><code>string</code></td><td>This name must be unique for all subnet groups that are created by your AWS account. If costumer do not provide it, cloudformation will generate it. Must not be "Default". </td></tr>
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
description,
subnet_ids,
tags,
cluster_subnet_group_name
FROM aws.redshift.cluster_subnet_group
WHERE region = 'us-east-1' AND data__Identifier = '<ClusterSubnetGroupName>';
```


## Permissions

To operate on the <code>cluster_subnet_group</code> resource, the following permissions are required:

### Read
```json
redshift:DescribeClusterSubnetGroups,
redshift:DescribeTags,
ec2:AllocateAddress,
ec2:AssociateAddress,
ec2:AttachNetworkInterface,
ec2:DescribeAccountAttributes,
ec2:DescribeAddresses,
ec2:DescribeAvailabilityZones,
ec2:DescribeInternetGateways,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcs
```

### Update
```json
redshift:ModifyClusterSubnetGroup,
redshift:DescribeClusterSubnetGroups,
redshift:DescribeTags,
redshift:CreateTags,
redshift:DeleteTags,
ec2:AllocateAddress,
ec2:AssociateAddress,
ec2:AttachNetworkInterface,
ec2:DescribeAccountAttributes,
ec2:DescribeAddresses,
ec2:DescribeAvailabilityZones,
ec2:DescribeInternetGateways,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcs
```

