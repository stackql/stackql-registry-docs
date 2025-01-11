---
title: eip_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - eip_associations
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

Creates, updates, deletes or gets an <code>eip_association</code> resource or lists <code>eip_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>eip_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates an Elastic IP address with an instance or a network interface. Before you can use an Elastic IP address, you must allocate it to your account. For more information about working with Elastic IP addresses, see &#91;Elastic IP address concepts and rules&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html#vpc-eip-overview).<br />You must specify <code>AllocationId</code> and either <code>InstanceId</code>, <code>NetworkInterfaceId</code>, or <code>PrivateIpAddress</code>.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.eip_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="allocation_id" /></td><td><code>string</code></td><td>The allocation ID. This is required.</td></tr>
<tr><td><CopyableCode code="network_interface_id" /></td><td><code>string</code></td><td>The ID of the network interface. If the instance has more than one network interface, you must specify a network interface ID.<br />You can specify either the instance ID or the network interface ID, but not both.</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>The ID of the instance. The instance must have exactly one attached network interface. You can specify either the instance ID or the network interface ID, but not both.</td></tr>
<tr><td><CopyableCode code="private_ip_address" /></td><td><code>string</code></td><td>The primary or secondary private IP address to associate with the Elastic IP address. If no private IP address is specified, the Elastic IP address is associated with the primary private IP address.</td></tr>
<tr><td><CopyableCode code="e_ip" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eipassociation.html"><code>AWS::EC2::EIPAssociation</code></a>.

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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>eip_associations</code> in a region.
```sql
SELECT
region,
id,
allocation_id,
network_interface_id,
instance_id,
private_ip_address,
e_ip
FROM aws.ec2.eip_associations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>eip_association</code>.
```sql
SELECT
region,
id,
allocation_id,
network_interface_id,
instance_id,
private_ip_address,
e_ip
FROM aws.ec2.eip_associations
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>eip_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.eip_associations (
 AllocationId,
 NetworkInterfaceId,
 InstanceId,
 PrivateIpAddress,
 EIP,
 region
)
SELECT 
'{{ AllocationId }}',
 '{{ NetworkInterfaceId }}',
 '{{ InstanceId }}',
 '{{ PrivateIpAddress }}',
 '{{ EIP }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.eip_associations (
 AllocationId,
 NetworkInterfaceId,
 InstanceId,
 PrivateIpAddress,
 EIP,
 region
)
SELECT 
 '{{ AllocationId }}',
 '{{ NetworkInterfaceId }}',
 '{{ InstanceId }}',
 '{{ PrivateIpAddress }}',
 '{{ EIP }}',
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
  - name: eip_association
    props:
      - name: AllocationId
        value: '{{ AllocationId }}'
      - name: NetworkInterfaceId
        value: '{{ NetworkInterfaceId }}'
      - name: InstanceId
        value: '{{ InstanceId }}'
      - name: PrivateIpAddress
        value: '{{ PrivateIpAddress }}'
      - name: EIP
        value: '{{ EIP }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.eip_associations
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>eip_associations</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeAddresses,
ec2:AssociateAddress
```

### Read
```json
ec2:DescribeAddresses
```

### Delete
```json
ec2:DisassociateAddress,
ec2:DescribeAddresses
```

### List
```json
ec2:DescribeAddresses
```
