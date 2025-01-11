---
title: vpn_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_gateways
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

Creates, updates, deletes or gets a <code>vpn_gateway</code> resource or lists <code>vpn_gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a virtual private gateway. A virtual private gateway is the endpoint on the VPC side of your VPN connection. You can create a virtual private gateway before creating the VPC itself.<br />For more information, see &#91;&#93;(https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpn_gateways" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="v_pn_gateway_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="amazon_side_asn" /></td><td><code>integer</code></td><td>The private Autonomous System Number (ASN) for the Amazon side of a BGP session.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Any tags assigned to the virtual private gateway.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of VPN connection the virtual private gateway supports.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpngateway.html"><code>AWS::EC2::VPNGateway</code></a>.

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
    <td><CopyableCode code="Type, region" /></td>
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
Gets all <code>vpn_gateways</code> in a region.
```sql
SELECT
region,
v_pn_gateway_id,
amazon_side_asn,
tags,
type
FROM aws.ec2.vpn_gateways
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>vpn_gateway</code>.
```sql
SELECT
region,
v_pn_gateway_id,
amazon_side_asn,
tags,
type
FROM aws.ec2.vpn_gateways
WHERE region = 'us-east-1' AND data__Identifier = '<VPNGatewayId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpn_gateway</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.vpn_gateways (
 Type,
 region
)
SELECT 
'{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.vpn_gateways (
 AmazonSideAsn,
 Tags,
 Type,
 region
)
SELECT 
 '{{ AmazonSideAsn }}',
 '{{ Tags }}',
 '{{ Type }}',
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
  - name: vpn_gateway
    props:
      - name: AmazonSideAsn
        value: '{{ AmazonSideAsn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.vpn_gateways
WHERE data__Identifier = '<VPNGatewayId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpn_gateways</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVpnGateway,
ec2:DescribeVpnGateways,
ec2:CreateTags
```

### Read
```json
ec2:DescribeVpnGateways
```

### Update
```json
ec2:DescribeVpnGateways,
ec2:CreateTags,
ec2:DeleteTags
```

### Delete
```json
ec2:DeleteVpnGateway,
ec2:DescribeVpnGateways
```

### List
```json
ec2:DescribeVpnGateways
```
