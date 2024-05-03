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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>cluster_subnet_groups</code> in a region or create a <code>cluster_subnet_groups</code> resource, use <code>cluster_subnet_group</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_subnet_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies an Amazon Redshift subnet group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.cluster_subnet_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
cluster_subnet_group_name
FROM aws.redshift.cluster_subnet_groups
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>cluster_subnet_groups</code> resource, the following permissions are required:

### Create
```json
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
ec2:DescribeVpcs
```

### List
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

