---
title: vpc_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>vpcs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a virtual private cloud (VPC).<br />You can optionally request an IPv6 CIDR block for the VPC. You can request an Amazon-provided IPv6 CIDR block from Amazon's pool of IPv6 addresses, or an IPv6 CIDR block from an IPv6 address pool that you provisioned through bring your own IP addresses (BYOIP).<br />For more information, see &#91;Virtual private clouds (VPC)&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/configure-your-vpc.html) in the *Amazon VPC User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_tenancy" /></td><td><code>string</code></td><td>The allowed tenancy of instances launched into the VPC.<br />+ <code>default</code>: An instance launched into the VPC runs on shared hardware by default, unless you explicitly specify a different tenancy during instance launch.<br />+ <code>dedicated</code>: An instance launched into the VPC runs on dedicated hardware by default, unless you explicitly specify a tenancy of <code>host</code> during instance launch. You cannot specify a tenancy of <code>default</code> during instance launch.<br /><br />Updating <code>InstanceTenancy</code> requires no replacement only if you are updating its value from <code>dedicated</code> to <code>default</code>. Updating <code>InstanceTenancy</code> from <code>default</code> to <code>dedicated</code> requires replacement.</td></tr>
<tr><td><CopyableCode code="ipv4_netmask_length" /></td><td><code>integer</code></td><td>The netmask length of the IPv4 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see &#91;What is IPAM?&#93;(https://docs.aws.amazon.com//vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.</td></tr>
<tr><td><CopyableCode code="cidr_block_associations" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="cidr_block" /></td><td><code>string</code></td><td>The IPv4 network range for the VPC, in CIDR notation. For example, <code>10.0.0.0/16</code>. We modify the specified CIDR block to its canonical form; for example, if you specify <code>100.68.0.18/18</code>, we modify it to <code>100.68.0.0/18</code>.<br />You must specify either<code>CidrBlock</code> or <code>Ipv4IpamPoolId</code>.</td></tr>
<tr><td><CopyableCode code="ipv4_ipam_pool_id" /></td><td><code>string</code></td><td>The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR. For more information, see &#91;What is IPAM?&#93;(https://docs.aws.amazon.com//vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.<br />You must specify either<code>CidrBlock</code> or <code>Ipv4IpamPoolId</code>.</td></tr>
<tr><td><CopyableCode code="default_network_acl" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_dns_support" /></td><td><code>boolean</code></td><td>Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range "plus two" succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled. Enabled by default. For more information, see &#91;DNS attributes in your VPC&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).</td></tr>
<tr><td><CopyableCode code="ipv6_cidr_blocks" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="default_security_group" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_dns_hostnames" /></td><td><code>boolean</code></td><td>Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not. Disabled by default for nondefault VPCs. For more information, see &#91;DNS attributes in your VPC&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).<br />You can only enable DNS hostnames if you've enabled DNS support.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>vpcs</code> in a region.
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
tag_key,
tag_value
FROM aws.ec2.vpc_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>vpc_tags</code> resource, see <a href="/providers/aws/ec2/vpcs/#permissions"><code>vpcs</code></a>


