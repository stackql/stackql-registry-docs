---
title: local_gateway_route_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_route_tables
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


Used to retrieve a list of <code>local_gateway_route_tables</code> in a region or to create or delete a <code>local_gateway_route_tables</code> resource, use <code>local_gateway_route_table</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_gateway_route_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes a route table for a local gateway.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.local_gateway_route_tables" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="local_gateway_route_table_id" /></td><td><code>string</code></td><td>The ID of the local gateway route table.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
local_gateway_route_table_id
FROM aws.ec2.local_gateway_route_tables
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "LocalGatewayId": "{{ LocalGatewayId }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.local_gateway_route_tables (
 LocalGatewayId,
 region
)
SELECT 
{{ .LocalGatewayId }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "LocalGatewayId": "{{ LocalGatewayId }}",
 "Mode": "{{ Mode }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.ec2.local_gateway_route_tables (
 LocalGatewayId,
 Mode,
 Tags,
 region
)
SELECT 
 {{ .LocalGatewayId }},
 {{ .Mode }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.local_gateway_route_tables
WHERE data__Identifier = '<LocalGatewayRouteTableId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>local_gateway_route_tables</code> resource, the following permissions are required:

### Create
```json
ec2:CreateLocalGatewayRouteTable,
ec2:DescribeLocalGatewayRouteTables,
ec2:CreateTags
```

### Delete
```json
ec2:DeleteLocalGatewayRouteTable,
ec2:DescribeLocalGatewayRouteTables,
ec2:DeleteTags
```

### List
```json
ec2:DescribeLocalGatewayRouteTables
```

