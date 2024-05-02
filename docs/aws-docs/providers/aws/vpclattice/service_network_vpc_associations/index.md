---
title: service_network_vpc_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - service_network_vpc_associations
  - vpclattice
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Used to retrieve a list of <code>service_network_vpc_associations</code> in a region or create a <code>service_network_vpc_associations</code> resource, use <code>service_network_vpc_association</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_network_vpc_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates a VPC with a service network.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.vpclattice.service_network_vpc_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.vpclattice.service_network_vpc_associations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>service_network_vpc_associations</code> resource, the following permissions are required:

### Create
```json
vpc-lattice:CreateServiceNetworkVpcAssociation,
vpc-lattice:GetServiceNetworkVpcAssociation,
vpc-lattice:ListServiceNetworkVpcAssociations,
vpc-lattice:ListTagsForResource,
ec2:DescribeSecurityGroups,
ec2:DescribeVpcs,
vpc-lattice:TagResource
```

### List
```json
vpc-lattice:ListServiceNetworkVpcAssociations
```

