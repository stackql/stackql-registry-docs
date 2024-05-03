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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>vpn_connection_route</code> resource, use <code>vpn_connection_routes</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_connection_route</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPNConnectionRoute</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpn_connection_route" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="destination_cidr_block" /></td><td><code>string</code></td><td>The CIDR block associated with the local subnet of the customer network.</td></tr>
<tr><td><CopyableCode code="vpn_connection_id" /></td><td><code>string</code></td><td>The ID of the VPN connection.</td></tr>
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
destination_cidr_block,
vpn_connection_id
FROM aws.ec2.vpn_connection_route
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

