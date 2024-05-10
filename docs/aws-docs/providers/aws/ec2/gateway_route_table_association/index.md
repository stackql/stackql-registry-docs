---
title: gateway_route_table_association
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_route_table_association
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


Gets or updates an individual <code>gateway_route_table_association</code> resource, use <code>gateway_route_table_associations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway_route_table_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates a gateway with a route table. The gateway and route table must be in the same VPC. This association causes the incoming traffic to the gateway to be routed according to the routes in the route table.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.gateway_route_table_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="route_table_id" /></td><td><code>string</code></td><td>The ID of the route table.</td></tr>
<tr><td><CopyableCode code="gateway_id" /></td><td><code>string</code></td><td>The ID of the gateway.</td></tr>
<tr><td><CopyableCode code="association_id" /></td><td><code>string</code></td><td>The route table association ID.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
route_table_id,
gateway_id,
association_id
FROM aws.ec2.gateway_route_table_association
WHERE region = 'us-east-1' AND data__Identifier = '<GatewayId>';
```


## Permissions

To operate on the <code>gateway_route_table_association</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeRouteTables
```

### Update
```json
ec2:DescribeRouteTables,
ec2:ReplaceRouteTableAssociation
```

