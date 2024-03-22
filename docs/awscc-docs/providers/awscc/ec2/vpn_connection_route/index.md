---
title: vpn_connection_route
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_connection_route
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
Gets an individual <code>vpn_connection_route</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_connection_route</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpn_connection_route</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.vpn_connection_route</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>destination_cidr_block</code></td><td><code>string</code></td><td>The CIDR block associated with the local subnet of the customer network.</td></tr>
<tr><td><code>vpn_connection_id</code></td><td><code>string</code></td><td>The ID of the VPN connection.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
destination_cidr_block,
vpn_connection_id
FROM awscc.ec2.vpn_connection_route
WHERE data__Identifier = '<DestinationCidrBlock>|<VpnConnectionId>';
```

## Permissions

To operate on the <code>vpn_connection_route</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeVpnConnections
```

### Delete
```json
ec2:DeleteVpnConnectionRoute,
ec2:DescribeVpnConnections
```

