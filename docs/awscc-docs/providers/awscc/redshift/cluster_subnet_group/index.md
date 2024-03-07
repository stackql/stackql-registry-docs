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
Gets an individual <code>cluster_subnet_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_subnet_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cluster_subnet_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.redshift.cluster_subnet_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the parameter group.</td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td>The list of VPC subnet IDs</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The list of tags for the cluster parameter group.</td></tr>
<tr><td><code>cluster_subnet_group_name</code></td><td><code>string</code></td><td>This name must be unique for all subnet groups that are created by your AWS account. If costumer do not provide it, cloudformation will generate it. Must not be "Default". </td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
subnet_ids,
tags,
cluster_subnet_group_name
FROM awscc.redshift.cluster_subnet_group
WHERE region = 'us-east-1'
AND data__Identifier = '{ClusterSubnetGroupName}';
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

### Delete
```json
redshift:DeleteClusterSubnetGroup,
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

