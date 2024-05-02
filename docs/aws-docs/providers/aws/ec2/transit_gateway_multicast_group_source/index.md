---
title: transit_gateway_multicast_group_source
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_multicast_group_source
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
Gets an individual <code>transit_gateway_multicast_group_source</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_multicast_group_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::TransitGatewayMulticastGroupSource registers and deregisters members and sources (network interfaces) with the transit gateway multicast group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_multicast_group_source</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>group_ip_address</code></td><td><code>string</code></td><td>The IP address assigned to the transit gateway multicast group.</td></tr>
<tr><td><code>transit_gateway_attachment_id</code></td><td><code>string</code></td><td>The ID of the transit gateway attachment.</td></tr>
<tr><td><code>transit_gateway_multicast_domain_id</code></td><td><code>string</code></td><td>The ID of the transit gateway multicast domain.</td></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td>The ID of the subnet.</td></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td>The ID of the resource.</td></tr>
<tr><td><code>resource_type</code></td><td><code>string</code></td><td>The type of resource, for example a VPC attachment.</td></tr>
<tr><td><code>network_interface_id</code></td><td><code>string</code></td><td>The ID of the transit gateway attachment.</td></tr>
<tr><td><code>group_member</code></td><td><code>boolean</code></td><td>Indicates that the resource is a transit gateway multicast group member.</td></tr>
<tr><td><code>group_source</code></td><td><code>boolean</code></td><td>Indicates that the resource is a transit gateway multicast group member.</td></tr>
<tr><td><code>member_type</code></td><td><code>string</code></td><td>The member type (for example, static).</td></tr>
<tr><td><code>source_type</code></td><td><code>string</code></td><td>The source type.</td></tr>
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
group_ip_address,
transit_gateway_attachment_id,
transit_gateway_multicast_domain_id,
subnet_id,
resource_id,
resource_type,
network_interface_id,
group_member,
group_source,
member_type,
source_type
FROM aws.ec2.transit_gateway_multicast_group_source
WHERE data__Identifier = '<TransitGatewayMulticastDomainId>|<GroupIpAddress>|<NetworkInterfaceId>';
```

## Permissions

To operate on the <code>transit_gateway_multicast_group_source</code> resource, the following permissions are required:

### Read
```json
ec2:SearchTransitGatewayMulticastGroups
```

### Delete
```json
ec2:DeregisterTransitGatewayMulticastGroupSources,
ec2:SearchTransitGatewayMulticastGroups
```

