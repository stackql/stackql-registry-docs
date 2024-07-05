---
title: placement_groups_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - placement_groups_list_only
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

Lists <code>placement_groups</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/placement_groups/"><code>placement_groups</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>placement_groups_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::PlacementGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.placement_groups_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="strategy" /></td><td><code>string</code></td><td>The placement strategy.</td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td>The Group Name of Placement Group.</td></tr>
<tr><td><CopyableCode code="spread_level" /></td><td><code>string</code></td><td>The Spread Level of Placement Group is an enum where it accepts either host or rack when strategy is spread</td></tr>
<tr><td><CopyableCode code="partition_count" /></td><td><code>integer</code></td><td>The number of partitions. Valid only when **Strategy** is set to `partition`</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
Lists all <code>placement_groups</code> in a region.
```sql
SELECT
region,
group_name
FROM aws.ec2.placement_groups_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>placement_groups_list_only</code> resource, see <a href="/providers/aws/ec2/placement_groups/#permissions"><code>placement_groups</code></a>


