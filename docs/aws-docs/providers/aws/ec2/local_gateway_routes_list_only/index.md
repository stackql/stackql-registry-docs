---
title: local_gateway_routes_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_routes_list_only
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

Lists <code>local_gateway_routes</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/local_gateway_routes/"><code>local_gateway_routes</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_gateway_routes_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes a route for a local gateway route table.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.local_gateway_routes_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="destination_cidr_block" /></td><td><code>string</code></td><td>The CIDR block used for destination matches.</td></tr>
<tr><td><CopyableCode code="local_gateway_route_table_id" /></td><td><code>string</code></td><td>The ID of the local gateway route table.</td></tr>
<tr><td><CopyableCode code="local_gateway_virtual_interface_group_id" /></td><td><code>string</code></td><td>The ID of the virtual interface group.</td></tr>
<tr><td><CopyableCode code="network_interface_id" /></td><td><code>string</code></td><td>The ID of the network interface.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the route.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The route type.</td></tr>
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
Lists all <code>local_gateway_routes</code> in a region.
```sql
SELECT
region,
destination_cidr_block,
local_gateway_route_table_id
FROM aws.ec2.local_gateway_routes_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>local_gateway_routes_list_only</code> resource, see <a href="/providers/aws/ec2/local_gateway_routes/#permissions"><code>local_gateway_routes</code></a>


