---
title: placement_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - placement_group_tags
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

Expands all tag keys and values for <code>placement_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>placement_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::PlacementGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.placement_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="strategy" /></td><td><code>string</code></td><td>The placement strategy.</td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td>The Group Name of Placement Group.</td></tr>
<tr><td><CopyableCode code="spread_level" /></td><td><code>string</code></td><td>The Spread Level of Placement Group is an enum where it accepts either host or rack when strategy is spread</td></tr>
<tr><td><CopyableCode code="partition_count" /></td><td><code>integer</code></td><td>The number of partitions. Valid only when **Strategy** is set to `partition`</td></tr>
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
Expands tags for all <code>placement_groups</code> in a region.
```sql
SELECT
region,
strategy,
group_name,
spread_level,
partition_count,
tag_key,
tag_value
FROM aws.ec2.placement_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>placement_group_tags</code> resource, see <a href="/providers/aws/ec2/placement_groups/#permissions"><code>placement_groups</code></a>

