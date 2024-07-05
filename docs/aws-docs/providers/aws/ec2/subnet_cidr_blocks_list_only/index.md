---
title: subnet_cidr_blocks_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - subnet_cidr_blocks_list_only
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

Lists <code>subnet_cidr_blocks</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/subnet_cidr_blocks/"><code>subnet_cidr_blocks</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_cidr_blocks_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::SubnetCidrBlock resource creates association between subnet and IPv6 CIDR</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.subnet_cidr_blocks_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Information about the IPv6 association.</td></tr>
<tr><td><CopyableCode code="ipv6_cidr_block" /></td><td><code>string</code></td><td>The IPv6 network range for the subnet, in CIDR notation. The subnet size must use a /64 prefix length</td></tr>
<tr><td><CopyableCode code="ipv6_ipam_pool_id" /></td><td><code>string</code></td><td>The ID of an IPv6 Amazon VPC IP Address Manager (IPAM) pool from which to allocate, to get the subnet's CIDR</td></tr>
<tr><td><CopyableCode code="ipv6_netmask_length" /></td><td><code>integer</code></td><td>The netmask length of the IPv6 CIDR to allocate to the subnet from an IPAM pool</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The ID of the subnet</td></tr>
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
Lists all <code>subnet_cidr_blocks</code> in a region.
```sql
SELECT
region,
id
FROM aws.ec2.subnet_cidr_blocks_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>subnet_cidr_blocks_list_only</code> resource, see <a href="/providers/aws/ec2/subnet_cidr_blocks/#permissions"><code>subnet_cidr_blocks</code></a>


