---
title: vpn_connection_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_connection_routes
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

Creates, updates, deletes or gets a <code>vpn_connection_route</code> resource or lists <code>vpn_connection_routes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_connection_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPNConnectionRoute</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpn_connection_routes" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="destination_cidr_block" /></td><td><code>string</code></td><td>The CIDR block associated with the local subnet of the customer network.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="DestinationCidrBlock, VpnConnectionId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>vpn_connection_routes</code> in a region.
```sql
SELECT
region,
destination_cidr_block,
vpn_connection_id
FROM aws.ec2.vpn_connection_routes
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>vpn_connection_route</code>.
```sql
SELECT
region,
destination_cidr_block,
vpn_connection_id
FROM aws.ec2.vpn_connection_routes
WHERE region = 'us-east-1' AND data__Identifier = '<DestinationCidrBlock>|<VpnConnectionId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpn_connection_route</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.vpn_connection_routes (
 DestinationCidrBlock,
 VpnConnectionId,
 region
)
SELECT 
'{{ DestinationCidrBlock }}',
 '{{ VpnConnectionId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.vpn_connection_routes (
 DestinationCidrBlock,
 VpnConnectionId,
 region
)
SELECT 
 '{{ DestinationCidrBlock }}',
 '{{ VpnConnectionId }}',
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
  - name: vpn_connection_route
    props:
      - name: DestinationCidrBlock
        value: '{{ DestinationCidrBlock }}'
      - name: VpnConnectionId
        value: '{{ VpnConnectionId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.vpn_connection_routes
WHERE data__Identifier = '<DestinationCidrBlock|VpnConnectionId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpn_connection_routes</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVpnConnectionRoute,
ec2:DescribeVpnConnections
```

### Read
```json
ec2:DescribeVpnConnections
```

### Delete
```json
ec2:DeleteVpnConnectionRoute,
ec2:DescribeVpnConnections
```

### List
```json
ec2:DescribeVpnConnections
```

