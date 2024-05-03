---
title: transit_gateway_multicast_group_member
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_multicast_group_member
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

Gets or operates on an individual <code>transit_gateway_multicast_group_member</code> resource, use <code>transit_gateway_multicast_group_members</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_multicast_group_member</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::TransitGatewayMulticastGroupMember registers and deregisters members and sources (network interfaces) with the transit gateway multicast group</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway_multicast_group_member" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="group_ip_address" /></td><td><code>string</code></td><td>The IP address assigned to the transit gateway multicast group.</td></tr>
<tr><td><CopyableCode code="transit_gateway_attachment_id" /></td><td><code>string</code></td><td>The ID of the transit gateway attachment.</td></tr>
<tr><td><CopyableCode code="transit_gateway_multicast_domain_id" /></td><td><code>string</code></td><td>The ID of the transit gateway multicast domain.</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The ID of the subnet.</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>The ID of the resource.</td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>The type of resource, for example a VPC attachment.</td></tr>
<tr><td><CopyableCode code="network_interface_id" /></td><td><code>string</code></td><td>The ID of the transit gateway attachment.</td></tr>
<tr><td><CopyableCode code="group_member" /></td><td><code>boolean</code></td><td>Indicates that the resource is a transit gateway multicast group member.</td></tr>
<tr><td><CopyableCode code="group_source" /></td><td><code>boolean</code></td><td>Indicates that the resource is a transit gateway multicast group member.</td></tr>
<tr><td><CopyableCode code="member_type" /></td><td><code>string</code></td><td>The member type (for example, static).</td></tr>
<tr><td><CopyableCode code="source_type" /></td><td><code>string</code></td><td>The source type.</td></tr>
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
FROM aws.ec2.transit_gateway_multicast_group_member
WHERE data__Identifier = '<TransitGatewayMulticastDomainId>|<GroupIpAddress>|<NetworkInterfaceId>';
```

## Permissions

To operate on the <code>transit_gateway_multicast_group_member</code> resource, the following permissions are required:

### Read
```json
ec2:SearchTransitGatewayMulticastGroups
```

### Delete
```json
ec2:DeregisterTransitGatewayMulticastGroupMembers,
ec2:SearchTransitGatewayMulticastGroups
```
