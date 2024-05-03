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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>ipam_allocations</code> in a region or create a <code>ipam_allocations</code> resource, use <code>ipam_allocation</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_allocations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAMAllocation Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ipam_allocations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="ipam_pool_id" /></td><td><code>string</code></td><td>Id of the IPAM Pool.</td></tr>
<tr><td><CopyableCode code="ipam_pool_allocation_id" /></td><td><code>string</code></td><td>Id of the allocation.</td></tr>
<tr><td><CopyableCode code="cidr" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
ipam_pool_id,
ipam_pool_allocation_id,
cidr
FROM aws.ec2.ipam_allocations
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

