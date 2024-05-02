---
title: subnets
hide_title: false
hide_table_of_contents: false
keywords:
  - subnets
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
Retrieves a list of <code>subnets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a subnet for the specified VPC.&lt;br&#x2F;&gt; For an IPv4 only subnet, specify an IPv4 CIDR block. If the VPC has an IPv6 CIDR block, you can create an IPv6 only subnet or a dual stack subnet instead. For an IPv6 only subnet, specify an IPv6 CIDR block. For a dual stack subnet, specify both an IPv4 CIDR block and an IPv6 CIDR block.&lt;br&#x2F;&gt; For more information, see &#91;Subnets for your VPC&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;configure-subnets.html) in the *Amazon VPC User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.subnets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td></td></tr>
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
subnet_id
FROM aws.ec2.subnets
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>subnets</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeSubnets,
ec2:CreateSubnet,
ec2:CreateTags,
ec2:ModifySubnetAttribute
```

### List
```json
ec2:DescribeSubnets,
ec2:DescribeNetworkAcls
```

