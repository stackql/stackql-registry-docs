---
title: ipam_allocation
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_allocation
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
Gets an individual <code>ipam_allocation</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_allocation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>ipam_allocation</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.ipam_allocation</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ipam_pool_allocation_id</code></td><td><code>string</code></td><td>Id of the allocation.</td></tr>
<tr><td><code>ipam_pool_id</code></td><td><code>string</code></td><td>Id of the IPAM Pool.</td></tr>
<tr><td><code>cidr</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>netmask_length</code></td><td><code>integer</code></td><td>The desired netmask length of the allocation. If set, IPAM will choose a block of free space with this size and return the CIDR representing it.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
ipam_pool_allocation_id,
ipam_pool_id,
cidr,
netmask_length,
description
FROM awscc.ec2.ipam_allocation
WHERE data__Identifier = '<IpamPoolId>|<IpamPoolAllocationId>|<Cidr>';
```

## Permissions

To operate on the <code>ipam_allocation</code> resource, the following permissions are required:

### Read
```json
ec2:GetIpamPoolAllocations
```

### Delete
```json
ec2:ReleaseIpamPoolAllocation
```

