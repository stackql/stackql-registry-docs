---
title: ipam_allocations
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_allocations
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
Retrieves a list of <code>ipam_allocations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_allocations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>ipam_allocations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.ipam_allocations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ipam_pool_id</code></td><td><code>string</code></td><td>Id of the IPAM Pool.</td></tr>
<tr><td><code>ipam_pool_allocation_id</code></td><td><code>string</code></td><td>Id of the allocation.</td></tr>
<tr><td><code>cidr</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
ipam_pool_id,
ipam_pool_allocation_id,
cidr
FROM awscc.ec2.ipam_allocations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>ipam_allocations</code> resource, the following permissions are required:

### Create
```json
ec2:AllocateIpamPoolCidr,
ec2:GetIpamPoolAllocations
```

### List
```json
ec2:GetIpamPoolAllocations
```

