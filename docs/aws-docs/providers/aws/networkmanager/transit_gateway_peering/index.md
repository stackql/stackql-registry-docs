---
title: transit_gateway_peering
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_peering
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


Gets or updates an individual <code>transit_gateway_peering</code> resource, use <code>transit_gateway_peerings</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_peering</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::NetworkManager::TransitGatewayPeering Resoruce Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.transit_gateway_peering" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="core_network_id" /></td><td><code>string</code></td><td>The Id of the core network that you want to peer a transit gateway to.</td></tr>
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
FROM aws.networkmanager.transit_gateway_peering
WHERE region = 'us-east-1' AND data__Identifier = '<PeeringId>';
```


## Permissions

To operate on the <code>transit_gateway_peering</code> resource, the following permissions are required:

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

