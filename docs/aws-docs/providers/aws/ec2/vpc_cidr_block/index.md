---
title: vpc_cidr_block
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_cidr_block
  - ec2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>vpc_cidr_block</code> resource, use <code>vpc_cidr_blocks</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_cidr_block</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCCidrBlock</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpc_cidr_block</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cidr_block</code></td><td><code>string</code></td><td>An IPv4 CIDR block to associate with the VPC.</td></tr>
<tr><td><code>ipv6_pool</code></td><td><code>string</code></td><td>The ID of an IPv6 address pool from which to allocate the IPv6 CIDR block.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The Id of the VPC associated CIDR Block.</td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
<tr><td><code>ipv6_cidr_block</code></td><td><code>string</code></td><td>An IPv6 CIDR block from the IPv6 address pool.</td></tr>
<tr><td><code>ipv4_ipam_pool_id</code></td><td><code>string</code></td><td>The ID of the IPv4 IPAM pool to Associate a CIDR from to a VPC.</td></tr>
<tr><td><code>ipv4_netmask_length</code></td><td><code>integer</code></td><td>The netmask length of the IPv4 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool.</td></tr>
<tr><td><code>ipv6_ipam_pool_id</code></td><td><code>string</code></td><td>The ID of the IPv6 IPAM pool to Associate a CIDR from to a VPC.</td></tr>
<tr><td><code>ipv6_netmask_length</code></td><td><code>integer</code></td><td>The netmask length of the IPv6 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool.</td></tr>
<tr><td><code>amazon_provided_ipv6_cidr_block</code></td><td><code>boolean</code></td><td>Requests an Amazon-provided IPv6 CIDR block with a &#x2F;56 prefix length for the VPC. You cannot specify the range of IPv6 addresses, or the size of the CIDR block.</td></tr>
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
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
cidr_block,
ipv6_pool,
id,
vpc_id,
ipv6_cidr_block,
ipv4_ipam_pool_id,
ipv4_netmask_length,
ipv6_ipam_pool_id,
ipv6_netmask_length,
amazon_provided_ipv6_cidr_block
FROM aws.ec2.vpc_cidr_block
WHERE data__Identifier = '<Id>|<VpcId>';
```

## Permissions

To operate on the <code>vpc_cidr_block</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeVpcs
```

### Delete
```json
ec2:DescribeVpcs,
ec2:DisassociateVpcCidrBlock
```

