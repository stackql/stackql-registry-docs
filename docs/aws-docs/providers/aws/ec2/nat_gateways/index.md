---
title: nat_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - nat_gateways
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


Used to retrieve a list of <code>nat_gateways</code> in a region or to create or delete a <code>nat_gateways</code> resource, use <code>nat_gateway</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nat_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a network address translation (NAT) gateway in the specified subnet. You can create either a public NAT gateway or a private NAT gateway. The default is a public NAT gateway. If you create a public NAT gateway, you must specify an elastic IP address.&lt;br&#x2F;&gt; With a NAT gateway, instances in a private subnet can connect to the internet, other AWS services, or an on-premises network using the IP address of the NAT gateway. For more information, see &#91;NAT gateways&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;vpc-nat-gateway.html) in the *Amazon VPC User Guide*.&lt;br&#x2F;&gt; If you add a default route (``AWS::EC2::Route`` resource) that points to a NAT gateway, specify the NAT gateway ID for the route's ``NatGatewayId`` property.&lt;br&#x2F;&gt;  When you associate an Elastic IP address or secondary Elastic IP address with a public NAT gateway, the network border group of the Elastic IP address must match the network border group of the Availability Zone (AZ) that the public NAT gateway is in. Otherwise, the NAT gateway fails to launch. You can see the network border group for the AZ by viewing the details of the subnet. Similarly, you can view the network border group for the Elastic IP address by viewing its details. For more information, see &#91;Allocate an Elastic IP address&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;vpc-eips.html#allocate-eip) in the *Amazon VPC User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.nat_gateways" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="nat_gateway_id" /></td><td><code>string</code></td><td></td></tr>
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
nat_gateway_id
FROM aws.ec2.nat_gateways
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>nat_gateway</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- nat_gateway.iql (required properties only)
INSERT INTO aws.ec2.nat_gateways (
 SubnetId,
 region
)
SELECT 
'{{ SubnetId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- nat_gateway.iql (all properties)
INSERT INTO aws.ec2.nat_gateways (
 SecondaryAllocationIds,
 PrivateIpAddress,
 ConnectivityType,
 SecondaryPrivateIpAddresses,
 SecondaryPrivateIpAddressCount,
 AllocationId,
 SubnetId,
 Tags,
 MaxDrainDurationSeconds,
 region
)
SELECT 
 '{{ SecondaryAllocationIds }}',
 '{{ PrivateIpAddress }}',
 '{{ ConnectivityType }}',
 '{{ SecondaryPrivateIpAddresses }}',
 '{{ SecondaryPrivateIpAddressCount }}',
 '{{ AllocationId }}',
 '{{ SubnetId }}',
 '{{ Tags }}',
 '{{ MaxDrainDurationSeconds }}',
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
  - name: nat_gateway
    props:
      - name: SecondaryAllocationIds
        value:
          - '{{ SecondaryAllocationIds[0] }}'
      - name: PrivateIpAddress
        value: '{{ PrivateIpAddress }}'
      - name: ConnectivityType
        value: '{{ ConnectivityType }}'
      - name: SecondaryPrivateIpAddresses
        value:
          - '{{ SecondaryPrivateIpAddresses[0] }}'
      - name: SecondaryPrivateIpAddressCount
        value: '{{ SecondaryPrivateIpAddressCount }}'
      - name: AllocationId
        value: '{{ AllocationId }}'
      - name: SubnetId
        value: '{{ SubnetId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: MaxDrainDurationSeconds
        value: '{{ MaxDrainDurationSeconds }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.nat_gateways
WHERE data__Identifier = '<NatGatewayId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>nat_gateways</code> resource, the following permissions are required:

### Create
```json
ec2:CreateNatGateway,
ec2:DescribeNatGateways,
ec2:CreateTags
```

### List
```json
ec2:DescribeNatGateways
```

### Delete
```json
ec2:DeleteNatGateway,
ec2:DescribeNatGateways
```

