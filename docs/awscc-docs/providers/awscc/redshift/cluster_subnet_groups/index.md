---
title: cluster_subnet_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_subnet_groups
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
Retrieves a list of <code>cluster_subnet_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_subnet_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cluster_subnet_groups</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.redshift.cluster_subnet_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster_subnet_group_name</code></td><td><code>string</code></td><td>This name must be unique for all subnet groups that are created by your AWS account. If costumer do not provide it, cloudformation will generate it. Must not be "Default". </td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>cluster_subnet_groups</code> resource, the following permissions are required:

### Create
<pre>
redshift:CreateClusterSubnetGroup,
redshift:CreateTags,
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
ec2:DescribeVpcs</pre>

### List
<pre>
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
ec2:DescribeVpcs</pre>


## Example
```sql
SELECT
region,
cluster_subnet_group_name
FROM awscc.redshift.cluster_subnet_groups
WHERE region = 'us-east-1'
```
