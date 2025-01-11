---
title: local_gateway_route_table_virtual_interface_group_association_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_route_table_virtual_interface_group_association_tags
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

Expands all tag keys and values for <code>local_gateway_route_table_virtual_interface_group_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_gateway_route_table_virtual_interface_group_association_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes a local gateway route table virtual interface group association for a local gateway.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.local_gateway_route_table_virtual_interface_group_association_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="local_gateway_route_table_virtual_interface_group_association_id" /></td><td><code>string</code></td><td>The ID of the local gateway route table virtual interface group association.</td></tr>
<tr><td><CopyableCode code="local_gateway_id" /></td><td><code>string</code></td><td>The ID of the local gateway.</td></tr>
<tr><td><CopyableCode code="local_gateway_route_table_id" /></td><td><code>string</code></td><td>The ID of the local gateway route table.</td></tr>
<tr><td><CopyableCode code="local_gateway_route_table_arn" /></td><td><code>string</code></td><td>The ARN of the local gateway route table.</td></tr>
<tr><td><CopyableCode code="local_gateway_virtual_interface_group_id" /></td><td><code>string</code></td><td>The ID of the local gateway route table virtual interface group.</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>The owner of the local gateway route table virtual interface group association.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the local gateway route table virtual interface group association.</td></tr>
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
Expands tags for all <code>local_gateway_route_table_virtual_interface_group_associations</code> in a region.
```sql
SELECT
region,
local_gateway_route_table_virtual_interface_group_association_id,
local_gateway_id,
local_gateway_route_table_id,
local_gateway_route_table_arn,
local_gateway_virtual_interface_group_id,
owner_id,
state,
tag_key,
tag_value
FROM aws.ec2.local_gateway_route_table_virtual_interface_group_association_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>local_gateway_route_table_virtual_interface_group_association_tags</code> resource, see <a href="/providers/aws/ec2/local_gateway_route_table_virtual_interface_group_associations/#permissions"><code>local_gateway_route_table_virtual_interface_group_associations</code></a>

