---
title: subnet_cidr_block
hide_title: false
hide_table_of_contents: false
keywords:
  - subnet_cidr_block
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
Gets an individual <code>subnet_cidr_block</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_cidr_block</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>subnet_cidr_block</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.subnet_cidr_block</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Information about the IPv6 association.</td></tr>
<tr><td><code>ipv6_cidr_block</code></td><td><code>string</code></td><td>The IPv6 network range for the subnet, in CIDR notation. The subnet size must use a &#x2F;64 prefix length</td></tr>
<tr><td><code>ipv6_ipam_pool_id</code></td><td><code>string</code></td><td>The ID of an IPv6 Amazon VPC IP Address Manager (IPAM) pool from which to allocate, to get the subnet's CIDR</td></tr>
<tr><td><code>ipv6_netmask_length</code></td><td><code>integer</code></td><td>The netmask length of the IPv6 CIDR to allocate to the subnet from an IPAM pool</td></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td>The ID of the subnet</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
ipv6_cidr_block,
ipv6_ipam_pool_id,
ipv6_netmask_length,
subnet_id
FROM awscc.ec2.subnet_cidr_block
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>subnet_cidr_block</code> resource, the following permissions are required:

### Delete
```json
ec2:DisassociateSubnetCidrBlock,
ec2:DescribeSubnets
```

### Read
```json
ec2:DescribeSubnets
```

