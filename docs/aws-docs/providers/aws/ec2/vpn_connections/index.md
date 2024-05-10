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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>vpn_connections</code> in a region or to create or delete a <code>vpn_connections</code> resource, use <code>vpn_connection</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPNConnection</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpn_connections" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="vpn_connection_id" /></td><td><code>string</code></td><td>The provider-assigned unique ID for this managed resource</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
vpn_connection_id
FROM aws.ec2.vpn_connections
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "CustomerGatewayId": "{{ CustomerGatewayId }}",
 "Type": "{{ Type }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.vpn_connections (
 CustomerGatewayId,
 Type,
 region
)
SELECT 
{{ CustomerGatewayId }},
 {{ Type }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "CustomerGatewayId": "{{ CustomerGatewayId }}",
 "StaticRoutesOnly": "{{ StaticRoutesOnly }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "TransitGatewayId": "{{ TransitGatewayId }}",
 "Type": "{{ Type }}",
 "VpnGatewayId": "{{ VpnGatewayId }}",
 "VpnTunnelOptionsSpecifications": [
  {
   "PreSharedKey": "{{ PreSharedKey }}",
   "TunnelInsideCidr": "{{ TunnelInsideCidr }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.ec2.vpn_connections (
 CustomerGatewayId,
 StaticRoutesOnly,
 Tags,
 TransitGatewayId,
 Type,
 VpnGatewayId,
 VpnTunnelOptionsSpecifications,
 region
)
SELECT 
 {{ CustomerGatewayId }},
 {{ StaticRoutesOnly }},
 {{ Tags }},
 {{ TransitGatewayId }},
 {{ Type }},
 {{ VpnGatewayId }},
 {{ VpnTunnelOptionsSpecifications }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.vpn_connections
WHERE data__Identifier = '<VpnConnectionId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpn_connections</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeVpnConnections,
ec2:CreateVpnConnection,
ec2:CreateTags
```

### Delete
```json
ec2:DescribeVpnConnections,
ec2:DeleteVpnConnection,
ec2:DeleteTags
```

### List
```json
ec2:DescribeVpnConnections
```

