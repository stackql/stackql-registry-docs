---
title: vpc
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc
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
Gets or operates on an individual <code>vpc</code> resource, use <code>vpcs</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a virtual private cloud (VPC).&lt;br&#x2F;&gt; You can optionally request an IPv6 CIDR block for the VPC. You can request an Amazon-provided IPv6 CIDR block from Amazon's pool of IPv6 addresses, or an IPv6 CIDR block from an IPv6 address pool that you provisioned through bring your own IP addresses (BYOIP).&lt;br&#x2F;&gt; For more information, see &#91;Virtual private clouds (VPC)&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;configure-your-vpc.html) in the *Amazon VPC User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpc</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instance_tenancy</code></td><td><code>string</code></td><td>The allowed tenancy of instances launched into the VPC.&lt;br&#x2F;&gt;  +  ``default``: An instance launched into the VPC runs on shared hardware by default, unless you explicitly specify a different tenancy during instance launch.&lt;br&#x2F;&gt;  +  ``dedicated``: An instance launched into the VPC runs on dedicated hardware by default, unless you explicitly specify a tenancy of ``host`` during instance launch. You cannot specify a tenancy of ``default`` during instance launch.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; Updating ``InstanceTenancy`` requires no replacement only if you are updating its value from ``dedicated`` to ``default``. Updating ``InstanceTenancy`` from ``default`` to ``dedicated`` requires replacement.</td></tr>
<tr><td><code>ipv4_netmask_length</code></td><td><code>integer</code></td><td>The netmask length of the IPv4 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see &#91;What is IPAM?&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;&#x2F;vpc&#x2F;latest&#x2F;ipam&#x2F;what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.</td></tr>
<tr><td><code>cidr_block_associations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>cidr_block</code></td><td><code>string</code></td><td>The IPv4 network range for the VPC, in CIDR notation. For example, ``10.0.0.0&#x2F;16``. We modify the specified CIDR block to its canonical form; for example, if you specify ``100.68.0.18&#x2F;18``, we modify it to ``100.68.0.0&#x2F;18``.&lt;br&#x2F;&gt; You must specify either``CidrBlock`` or ``Ipv4IpamPoolId``.</td></tr>
<tr><td><code>ipv4_ipam_pool_id</code></td><td><code>string</code></td><td>The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR. For more information, see &#91;What is IPAM?&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;&#x2F;vpc&#x2F;latest&#x2F;ipam&#x2F;what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.&lt;br&#x2F;&gt; You must specify either``CidrBlock`` or ``Ipv4IpamPoolId``.</td></tr>
<tr><td><code>default_network_acl</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enable_dns_support</code></td><td><code>boolean</code></td><td>Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range "plus two" succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled. Enabled by default. For more information, see &#91;DNS attributes in your VPC&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;vpc-dns.html#vpc-dns-support).</td></tr>
<tr><td><code>ipv6_cidr_blocks</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>default_security_group</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enable_dns_hostnames</code></td><td><code>boolean</code></td><td>Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not. Disabled by default for nondefault VPCs. For more information, see &#91;DNS attributes in your VPC&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;vpc-dns.html#vpc-dns-support).&lt;br&#x2F;&gt; You can only enable DNS hostnames if you've enabled DNS support.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags for the VPC.</td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
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
vpc_id,
instance_tenancy,
ipv4_netmask_length,
cidr_block_associations,
cidr_block,
ipv4_ipam_pool_id,
default_network_acl,
enable_dns_support,
ipv6_cidr_blocks,
default_security_group,
enable_dns_hostnames,
tags
FROM aws.ec2.vpc
WHERE data__Identifier = '<VpcId>';
```

## Permissions

To operate on the <code>vpc</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeVpcs,
ec2:DescribeSecurityGroups,
ec2:DescribeNetworkAcls,
ec2:DescribeVpcAttribute
```

### Update
```json
ec2:CreateTags,
ec2:ModifyVpcAttribute,
ec2:DeleteTags,
ec2:ModifyVpcTenancy
```

### Delete
```json
ec2:DeleteVpc,
ec2:DescribeVpcs
```

