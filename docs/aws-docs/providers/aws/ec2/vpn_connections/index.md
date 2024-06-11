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

Creates, updates, deletes or gets a <code>vpn_connection</code> resource or lists <code>vpn_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPNConnection</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpn_connections" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="vpn_connection_id" /></td><td><code>string</code></td><td>The provider-assigned unique ID for this managed resource</td></tr>
<tr><td><CopyableCode code="customer_gateway_id" /></td><td><code>string</code></td><td>The ID of the customer gateway at your end of the VPN connection.</td></tr>
<tr><td><CopyableCode code="static_routes_only" /></td><td><code>boolean</code></td><td>Indicates whether the VPN connection uses static routes only.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Any tags assigned to the VPN connection.</td></tr>
<tr><td><CopyableCode code="transit_gateway_id" /></td><td><code>string</code></td><td>The ID of the transit gateway associated with the VPN connection.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of VPN connection.</td></tr>
<tr><td><CopyableCode code="vpn_gateway_id" /></td><td><code>string</code></td><td>The ID of the virtual private gateway at the AWS side of the VPN connection.</td></tr>
<tr><td><CopyableCode code="vpn_tunnel_options_specifications" /></td><td><code>array</code></td><td>The tunnel options for the VPN connection.</td></tr>
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
    <td><CopyableCode code="Type, CustomerGatewayId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>vpn_connections</code> in a region.
```sql
SELECT
region,
vpn_connection_id
FROM aws.ec2.vpn_connections
WHERE region = 'us-east-1';
```
Gets all properties from a <code>vpn_connection</code>.
```sql
SELECT
region,
vpn_connection_id,
customer_gateway_id,
static_routes_only,
tags,
transit_gateway_id,
type,
vpn_gateway_id,
vpn_tunnel_options_specifications
FROM aws.ec2.vpn_connections
WHERE region = 'us-east-1' AND data__Identifier = '<VpnConnectionId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpn_connection</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.ec2.vpn_connections (
 CustomerGatewayId,
 Type,
 region
)
SELECT 
'{{ CustomerGatewayId }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ CustomerGatewayId }}',
 '{{ StaticRoutesOnly }}',
 '{{ Tags }}',
 '{{ TransitGatewayId }}',
 '{{ Type }}',
 '{{ VpnGatewayId }}',
 '{{ VpnTunnelOptionsSpecifications }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: vpn_connection
    props:
      - name: CustomerGatewayId
        value: '{{ CustomerGatewayId }}'
      - name: StaticRoutesOnly
        value: '{{ StaticRoutesOnly }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TransitGatewayId
        value: '{{ TransitGatewayId }}'
      - name: Type
        value: '{{ Type }}'
      - name: VpnGatewayId
        value: '{{ VpnGatewayId }}'
      - name: VpnTunnelOptionsSpecifications
        value:
          - PreSharedKey: '{{ PreSharedKey }}'
            TunnelInsideCidr: '{{ TunnelInsideCidr }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Update
```json
ec2:DescribeVpnConnections,
ec2:CreateTags,
ec2:DeleteTags
```

### Read
```json
ec2:DescribeVpnConnections
```

### List
```json
ec2:DescribeVpnConnections
```

