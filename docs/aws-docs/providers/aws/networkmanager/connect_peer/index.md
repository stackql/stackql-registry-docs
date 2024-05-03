---
title: connect_peer
hide_title: false
hide_table_of_contents: false
keywords:
  - connect_peer
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

Gets or operates on an individual <code>connect_peer</code> resource, use <code>connect_peers</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connect_peer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::NetworkManager::ConnectPeer Resource Type Definition.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.connect_peer" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="peer_address" /></td><td><code>string</code></td><td>The IP address of the Connect peer.</td></tr>
<tr><td><CopyableCode code="core_network_address" /></td><td><code>string</code></td><td>The IP address of a core network.</td></tr>
<tr><td><CopyableCode code="bgp_options" /></td><td><code>object</code></td><td>Bgp options for connect peer.</td></tr>
<tr><td><CopyableCode code="inside_cidr_blocks" /></td><td><code>array</code></td><td>The inside IP addresses used for a Connect peer configuration.</td></tr>
<tr><td><CopyableCode code="core_network_id" /></td><td><code>string</code></td><td>The ID of the core network.</td></tr>
<tr><td><CopyableCode code="connect_attachment_id" /></td><td><code>string</code></td><td>The ID of the attachment to connect.</td></tr>
<tr><td><CopyableCode code="connect_peer_id" /></td><td><code>string</code></td><td>The ID of the Connect peer.</td></tr>
<tr><td><CopyableCode code="edge_location" /></td><td><code>string</code></td><td>The Connect peer Regions where edges are located.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>State of the connect peer.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Connect peer creation time.</td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>object</code></td><td>Configuration of the connect peer.</td></tr>
<tr><td><CopyableCode code="subnet_arn" /></td><td><code>string</code></td><td>The subnet ARN for the connect peer.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
peer_address,
core_network_address,
bgp_options,
inside_cidr_blocks,
core_network_id,
connect_attachment_id,
connect_peer_id,
edge_location,
state,
created_at,
configuration,
subnet_arn,
tags
FROM aws.networkmanager.connect_peer
WHERE data__Identifier = '<ConnectPeerId>';
```

## Permissions

To operate on the <code>connect_peer</code> resource, the following permissions are required:

### Read
```json
networkmanager:GetConnectPeer
```

### Update
```json
networkmanager:GetConnectPeer,
networkmanager:ListTagsForResource,
networkmanager:TagResource,
networkmanager:UntagResource,
ec2:DescribeRegions
```

### Delete
```json
networkmanager:GetConnectPeer,
networkmanager:DeleteConnectPeer,
ec2:DescribeRegions
```

