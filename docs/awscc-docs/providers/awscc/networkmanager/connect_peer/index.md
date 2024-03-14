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
Gets an individual <code>connect_peer</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connect_peer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>connect_peer</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.networkmanager.connect_peer</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>peer_address</code></td><td><code>string</code></td><td>The IP address of the Connect peer.</td></tr>
<tr><td><code>core_network_address</code></td><td><code>string</code></td><td>The IP address of a core network.</td></tr>
<tr><td><code>bgp_options</code></td><td><code>object</code></td><td>Bgp options for connect peer.</td></tr>
<tr><td><code>inside_cidr_blocks</code></td><td><code>array</code></td><td>The inside IP addresses used for a Connect peer configuration.</td></tr>
<tr><td><code>core_network_id</code></td><td><code>string</code></td><td>The ID of the core network.</td></tr>
<tr><td><code>connect_attachment_id</code></td><td><code>string</code></td><td>The ID of the attachment to connect.</td></tr>
<tr><td><code>connect_peer_id</code></td><td><code>string</code></td><td>The ID of the Connect peer.</td></tr>
<tr><td><code>edge_location</code></td><td><code>string</code></td><td>The Connect peer Regions where edges are located.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>State of the connect peer.</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>Connect peer creation time.</td></tr>
<tr><td><code>configuration</code></td><td><code>object</code></td><td>Configuration of the connect peer.</td></tr>
<tr><td><code>subnet_arn</code></td><td><code>string</code></td><td>The subnet ARN for the connect peer.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.networkmanager.connect_peer
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

