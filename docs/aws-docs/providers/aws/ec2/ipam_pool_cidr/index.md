---
title: ipam_pool_cidr
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_pool_cidr
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

Gets or operates on an individual <code>ipam_pool_cidr</code> resource, use <code>ipam_pool_cidrs</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_pool_cidr</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAMPoolCidr Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ipam_pool_cidr" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="ipam_pool_cidr_id" /></td><td><code>string</code></td><td>Id of the IPAM Pool Cidr.</td></tr>
<tr><td><CopyableCode code="ipam_pool_id" /></td><td><code>string</code></td><td>Id of the IPAM Pool.</td></tr>
<tr><td><CopyableCode code="cidr" /></td><td><code>string</code></td><td>Represents a single IPv4 or IPv6 CIDR</td></tr>
<tr><td><CopyableCode code="netmask_length" /></td><td><code>integer</code></td><td>The desired netmask length of the provision. If set, IPAM will choose a block of free space with this size and return the CIDR representing it.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>Provisioned state of the cidr.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
ipam_pool_cidr_id,
ipam_pool_id,
cidr,
netmask_length,
state
FROM aws.ec2.ipam_pool_cidr
WHERE data__Identifier = '<IpamPoolId>|<IpamPoolCidrId>';
```

## Permissions

To operate on the <code>ipam_pool_cidr</code> resource, the following permissions are required:

### Read
```json
ec2:GetIpamPoolCidrs
```

### Delete
```json
ec2:DeprovisionIpamPoolCidr,
ec2:GetIpamPoolCidrs
```

