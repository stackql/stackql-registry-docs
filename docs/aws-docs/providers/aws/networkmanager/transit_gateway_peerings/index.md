---
title: transit_gateway_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_peerings
  - networkmanager
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


Used to retrieve a list of <code>transit_gateway_peerings</code> in a region or to create or delete a <code>transit_gateway_peerings</code> resource, use <code>transit_gateway_peering</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::NetworkManager::TransitGatewayPeering Resoruce Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.transit_gateway_peerings" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="peering_id" /></td><td><code>string</code></td><td>The Id of the transit gateway peering</td></tr>
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
peering_id
FROM aws.networkmanager.transit_gateway_peerings
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
 "CoreNetworkId": "{{ CoreNetworkId }}",
 "TransitGatewayArn": "{{ TransitGatewayArn }}"
}
>>>
--required properties only
INSERT INTO aws.networkmanager.transit_gateway_peerings (
 CoreNetworkId,
 TransitGatewayArn,
 region
)
SELECT 
{{ CoreNetworkId }},
 {{ TransitGatewayArn }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "CoreNetworkId": "{{ CoreNetworkId }}",
 "TransitGatewayArn": "{{ TransitGatewayArn }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.networkmanager.transit_gateway_peerings (
 CoreNetworkId,
 TransitGatewayArn,
 Tags,
 region
)
SELECT 
 {{ CoreNetworkId }},
 {{ TransitGatewayArn }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.networkmanager.transit_gateway_peerings
WHERE data__Identifier = '<PeeringId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>transit_gateway_peerings</code> resource, the following permissions are required:

### Create
```json
networkmanager:CreateTransitGatewayPeering,
networkmanager:TagResource,
networkmanager:GetTransitGatewayPeering,
iam:CreateServiceLinkedRole,
ec2:CreateTransitGatewayPeeringAttachment,
ec2:AcceptTransitGatewayPeeringAttachment,
ec2:DescribeRegions
```

### Delete
```json
networkmanager:DeletePeering,
networkmanager:GetTransitGatewayPeering,
ec2:DescribeRegions
```

### List
```json
networkmanager:ListPeerings
```

