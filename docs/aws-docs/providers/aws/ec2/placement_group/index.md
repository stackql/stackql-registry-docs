---
title: placement_group
hide_title: false
hide_table_of_contents: false
keywords:
  - placement_group
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


Gets or updates an individual <code>placement_group</code> resource, use <code>placement_groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>placement_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::PlacementGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.placement_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="strategy" /></td><td><code>string</code></td><td>The placement strategy.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
strategy,
group_name,
spread_level,
partition_count,
tags
FROM aws.ec2.placement_group
WHERE region = 'us-east-1' AND data__Identifier = '<GroupName>';
```


## Permissions

To operate on the <code>placement_group</code> resource, the following permissions are required:

### Read
```json
ec2:DescribePlacementGroups
```

