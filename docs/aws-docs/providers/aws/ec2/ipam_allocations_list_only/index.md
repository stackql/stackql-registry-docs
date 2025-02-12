---
title: ipam_allocations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_allocations_list_only
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

Lists <code>ipam_allocations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/ipam_allocations/"><code>ipam_allocations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_allocations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAMAllocation Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ipam_allocations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ipam_pool_allocation_id" /></td><td><code>string</code></td><td>Id of the allocation.</td></tr>
<tr><td><CopyableCode code="ipam_pool_id" /></td><td><code>string</code></td><td>Id of the IPAM Pool.</td></tr>
<tr><td><CopyableCode code="cidr" /></td><td><code>string</code></td><td>Represents a single IPv4 or IPv6 CIDR</td></tr>
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
Lists all <code>ipam_allocations</code> in a region.
```sql
SELECT
region,
ipam_pool_id,
ipam_pool_allocation_id,
cidr
FROM aws.ec2.ipam_allocations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>ipam_allocations_list_only</code> resource, see <a href="/providers/aws/ec2/ipam_allocations/#permissions"><code>ipam_allocations</code></a>

