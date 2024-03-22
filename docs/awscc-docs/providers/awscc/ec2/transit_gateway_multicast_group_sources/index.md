---
title: transit_gateway_multicast_group_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_multicast_group_sources
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
Retrieves a list of <code>transit_gateway_multicast_group_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_multicast_group_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>transit_gateway_multicast_group_sources</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.transit_gateway_multicast_group_sources</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>transit_gateway_multicast_domain_id</code></td><td><code>string</code></td><td>The ID of the transit gateway multicast domain.</td></tr>
<tr><td><code>group_ip_address</code></td><td><code>string</code></td><td>The IP address assigned to the transit gateway multicast group.</td></tr>
<tr><td><code>network_interface_id</code></td><td><code>string</code></td><td>The ID of the transit gateway attachment.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
transit_gateway_multicast_domain_id,
group_ip_address,
network_interface_id
FROM awscc.ec2.transit_gateway_multicast_group_sources
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>transit_gateway_multicast_group_sources</code> resource, the following permissions are required:

### Create
```json
ec2:RegisterTransitGatewayMulticastGroupSources,
ec2:SearchTransitGatewayMulticastGroups
```

### List
```json
ec2:SearchTransitGatewayMulticastGroups
```

