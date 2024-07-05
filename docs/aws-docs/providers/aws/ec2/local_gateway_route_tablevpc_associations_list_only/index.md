---
title: local_gateway_route_tablevpc_associations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_route_tablevpc_associations_list_only
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

Lists <code>local_gateway_route_tablevpc_associations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/local_gateway_route_tablevpc_associations/"><code>local_gateway_route_tablevpc_associations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_gateway_route_tablevpc_associations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes an association between a local gateway route table and a VPC.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.local_gateway_route_tablevpc_associations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="local_gateway_id" /></td><td><code>string</code></td><td>The ID of the local gateway.</td></tr>
<tr><td><CopyableCode code="local_gateway_route_table_id" /></td><td><code>string</code></td><td>The ID of the local gateway route table.</td></tr>
<tr><td><CopyableCode code="local_gateway_route_table_vpc_association_id" /></td><td><code>string</code></td><td>The ID of the association.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the association.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the association.</td></tr>
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
Lists all <code>local_gateway_route_tablevpc_associations</code> in a region.
```sql
SELECT
region,
local_gateway_route_table_vpc_association_id
FROM aws.ec2.local_gateway_route_tablevpc_associations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>local_gateway_route_tablevpc_associations_list_only</code> resource, see <a href="/providers/aws/ec2/local_gateway_route_tablevpc_associations/#permissions"><code>local_gateway_route_tablevpc_associations</code></a>


