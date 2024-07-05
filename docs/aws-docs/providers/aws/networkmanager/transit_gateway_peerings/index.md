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

Creates, updates, deletes or gets a <code>transit_gateway_peering</code> resource or lists <code>transit_gateway_peerings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::NetworkManager::TransitGatewayPeering Resoruce Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.transit_gateway_peerings" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="core_network_id" /></td><td><code>string</code></td><td>The Id of the core network that you want to peer a transit gateway to.</td></tr>
<tr><td><CopyableCode code="core_network_arn" /></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the core network that you want to peer a transit gateway to.</td></tr>
<tr><td><CopyableCode code="transit_gateway_arn" /></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the transit gateway that you will peer to a core network</td></tr>
<tr><td><CopyableCode code="transit_gateway_peering_attachment_id" /></td><td><code>string</code></td><td>The ID of the TransitGatewayPeeringAttachment</td></tr>
<tr><td><CopyableCode code="peering_id" /></td><td><code>string</code></td><td>The Id of the transit gateway peering</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the transit gateway peering</td></tr>
<tr><td><CopyableCode code="edge_location" /></td><td><code>string</code></td><td>The location of the transit gateway peering</td></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the resource that you will peer to a core network</td></tr>
<tr><td><CopyableCode code="owner_account_id" /></td><td><code>string</code></td><td>Peering owner account Id</td></tr>
<tr><td><CopyableCode code="peering_type" /></td><td><code>string</code></td><td>Peering type (TransitGatewayPeering)</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The creation time of the transit gateway peering</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="CoreNetworkId, TransitGatewayArn, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>transit_gateway_peerings</code> in a region.
```sql
SELECT
region,
core_network_id,
core_network_arn,
transit_gateway_arn,
transit_gateway_peering_attachment_id,
peering_id,
state,
edge_location,
resource_arn,
owner_account_id,
peering_type,
created_at,
tags
FROM aws.networkmanager.transit_gateway_peerings
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>transit_gateway_peering</code>.
```sql
SELECT
region,
core_network_id,
core_network_arn,
transit_gateway_arn,
transit_gateway_peering_attachment_id,
peering_id,
state,
edge_location,
resource_arn,
owner_account_id,
peering_type,
created_at,
tags
FROM aws.networkmanager.transit_gateway_peerings
WHERE region = 'us-east-1' AND data__Identifier = '<PeeringId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>transit_gateway_peering</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.networkmanager.transit_gateway_peerings (
 CoreNetworkId,
 TransitGatewayArn,
 region
)
SELECT 
'{{ CoreNetworkId }}',
 '{{ TransitGatewayArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.networkmanager.transit_gateway_peerings (
 CoreNetworkId,
 TransitGatewayArn,
 Tags,
 region
)
SELECT 
 '{{ CoreNetworkId }}',
 '{{ TransitGatewayArn }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: transit_gateway_peering
    props:
      - name: CoreNetworkId
        value: '{{ CoreNetworkId }}'
      - name: TransitGatewayArn
        value: '{{ TransitGatewayArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
networkmanager:GetTransitGatewayPeering,
networkmanager:TagResource
```

### Update
```json
networkmanager:TagResource,
networkmanager:UntagResource,
networkmanager:ListTagsForResource,
networkmanager:GetTransitGatewayPeering,
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

