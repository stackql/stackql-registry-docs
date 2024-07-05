---
title: vpc_cidr_blocks_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_cidr_blocks_list_only
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

Lists <code>vpc_cidr_blocks</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/vpc_cidr_blocks/"><code>vpc_cidr_blocks</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_cidr_blocks_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCCidrBlock</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_cidr_blocks_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cidr_block" /></td><td><code>string</code></td><td>An IPv4 CIDR block to associate with the VPC.</td></tr>
<tr><td><CopyableCode code="ipv6_pool" /></td><td><code>string</code></td><td>The ID of an IPv6 address pool from which to allocate the IPv6 CIDR block.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The Id of the VPC associated CIDR Block.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
<tr><td><CopyableCode code="ipv6_cidr_block" /></td><td><code>string</code></td><td>An IPv6 CIDR block from the IPv6 address pool.</td></tr>
<tr><td><CopyableCode code="ipv4_ipam_pool_id" /></td><td><code>string</code></td><td>The ID of the IPv4 IPAM pool to Associate a CIDR from to a VPC.</td></tr>
<tr><td><CopyableCode code="ipv4_netmask_length" /></td><td><code>integer</code></td><td>The netmask length of the IPv4 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool.</td></tr>
<tr><td><CopyableCode code="ipv6_ipam_pool_id" /></td><td><code>string</code></td><td>The ID of the IPv6 IPAM pool to Associate a CIDR from to a VPC.</td></tr>
<tr><td><CopyableCode code="ipv6_netmask_length" /></td><td><code>integer</code></td><td>The netmask length of the IPv6 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool.</td></tr>
<tr><td><CopyableCode code="amazon_provided_ipv6_cidr_block" /></td><td><code>boolean</code></td><td>Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IPv6 addresses, or the size of the CIDR block.</td></tr>
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
Lists all <code>vpc_cidr_blocks</code> in a region.
```sql
SELECT
region,
id,
vpc_id
FROM aws.ec2.vpc_cidr_blocks_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>vpc_cidr_blocks_list_only</code> resource, see <a href="/providers/aws/ec2/vpc_cidr_blocks/#permissions"><code>vpc_cidr_blocks</code></a>


