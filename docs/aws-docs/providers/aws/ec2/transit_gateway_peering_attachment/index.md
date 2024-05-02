---
title: transit_gateway_peering_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_peering_attachment
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
Gets an individual <code>transit_gateway_peering_attachment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_peering_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::TransitGatewayPeeringAttachment type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_peering_attachment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>status</code></td><td><code>object</code></td><td>The status of the transit gateway peering attachment.</td></tr>
<tr><td><code>transit_gateway_id</code></td><td><code>string</code></td><td>The ID of the transit gateway.</td></tr>
<tr><td><code>peer_transit_gateway_id</code></td><td><code>string</code></td><td>The ID of the peer transit gateway.</td></tr>
<tr><td><code>peer_account_id</code></td><td><code>string</code></td><td>The ID of the peer account</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of the transit gateway peering attachment. Note that the initiating state has been deprecated.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>The time the transit gateway peering attachment was created.</td></tr>
<tr><td><code>peer_region</code></td><td><code>string</code></td><td>Peer Region</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags for the transit gateway peering attachment.</td></tr>
<tr><td><code>transit_gateway_attachment_id</code></td><td><code>string</code></td><td>The ID of the transit gateway peering attachment.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
status,
transit_gateway_id,
peer_transit_gateway_id,
peer_account_id,
state,
creation_time,
peer_region,
tags,
transit_gateway_attachment_id
FROM aws.ec2.transit_gateway_peering_attachment
WHERE data__Identifier = '<TransitGatewayAttachmentId>';
```

## Permissions

To operate on the <code>transit_gateway_peering_attachment</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeTransitGatewayPeeringAttachments
```

### Update
```json
ec2:DescribeTransitGatewayPeeringAttachments
```

### Delete
```json
ec2:DeleteTransitGatewayPeeringAttachment,
ec2:DescribeTransitGatewayPeeringAttachments
```

