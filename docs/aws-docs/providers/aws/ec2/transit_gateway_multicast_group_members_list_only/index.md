---
title: transit_gateway_multicast_group_members_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_multicast_group_members_list_only
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

Lists <code>transit_gateway_multicast_group_members</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/transit_gateway_multicast_group_members/"><code>transit_gateway_multicast_group_members</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_multicast_group_members_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::TransitGatewayMulticastGroupMember registers and deregisters members and sources (network interfaces) with the transit gateway multicast group</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway_multicast_group_members_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="group_ip_address" /></td><td><code>string</code></td><td>The IP address assigned to the transit gateway multicast group.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>transit_gateway_multicast_group_members</code> in a region.
```sql
SELECT
region,
transit_gateway_multicast_domain_id,
group_ip_address,
network_interface_id
FROM aws.ec2.transit_gateway_multicast_group_members_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>transit_gateway_multicast_group_members_list_only</code> resource, see <a href="/providers/aws/ec2/transit_gateway_multicast_group_members/#permissions"><code>transit_gateway_multicast_group_members</code></a>


