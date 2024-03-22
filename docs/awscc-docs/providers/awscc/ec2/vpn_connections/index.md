---
title: vpn_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_connections
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
Retrieves a list of <code>vpn_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpn_connections</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.vpn_connections</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>vpn_connection_id</code></td><td><code>string</code></td><td>The provider-assigned unique ID for this managed resource</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
vpn_connection_id
FROM awscc.ec2.vpn_connections
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>vpn_connections</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeVpnConnections,
ec2:CreateVpnConnection,
ec2:CreateTags
```

### List
```json
ec2:DescribeVpnConnections
```

