---
title: network_interface_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interface_attachments
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

Creates, updates, deletes or gets a <code>network_interface_attachment</code> resource or lists <code>network_interface_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_interface_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::NetworkInterfaceAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.network_interface_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="attachment_id" /></td><td><code>string</code></td><td>The ID of the network interface attachment.</td></tr>
<tr><td><CopyableCode code="delete_on_termination" /></td><td><code>boolean</code></td><td>Whether to delete the network interface when the instance terminates. By default, this value is set to true.</td></tr>
<tr><td><CopyableCode code="device_index" /></td><td><code>string</code></td><td>The network interface's position in the attachment order. For example, the first attached network interface has a DeviceIndex of 0.</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>The ID of the instance to which you will attach the ENI.</td></tr>
<tr><td><CopyableCode code="network_interface_id" /></td><td><code>string</code></td><td>The ID of the ENI that you want to attach.</td></tr>
<tr><td><CopyableCode code="ena_srd_specification" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="DeviceIndex, InstanceId, NetworkInterfaceId, region" /></td>
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
Gets all <code>network_interface_attachments</code> in a region.
```sql
SELECT
region,
attachment_id,
delete_on_termination,
device_index,
instance_id,
network_interface_id,
ena_srd_specification
FROM aws.ec2.network_interface_attachments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>network_interface_attachment</code>.
```sql
SELECT
region,
attachment_id,
delete_on_termination,
device_index,
instance_id,
network_interface_id,
ena_srd_specification
FROM aws.ec2.network_interface_attachments
WHERE region = 'us-east-1' AND data__Identifier = '<AttachmentId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_interface_attachment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.network_interface_attachments (
 DeviceIndex,
 InstanceId,
 NetworkInterfaceId,
 region
)
SELECT 
'{{ DeviceIndex }}',
 '{{ InstanceId }}',
 '{{ NetworkInterfaceId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.network_interface_attachments (
 DeleteOnTermination,
 DeviceIndex,
 InstanceId,
 NetworkInterfaceId,
 EnaSrdSpecification,
 region
)
SELECT 
 '{{ DeleteOnTermination }}',
 '{{ DeviceIndex }}',
 '{{ InstanceId }}',
 '{{ NetworkInterfaceId }}',
 '{{ EnaSrdSpecification }}',
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
  - name: network_interface_attachment
    props:
      - name: DeleteOnTermination
        value: '{{ DeleteOnTermination }}'
      - name: DeviceIndex
        value: '{{ DeviceIndex }}'
      - name: InstanceId
        value: '{{ InstanceId }}'
      - name: NetworkInterfaceId
        value: '{{ NetworkInterfaceId }}'
      - name: EnaSrdSpecification
        value:
          EnaSrdEnabled: '{{ EnaSrdEnabled }}'
          EnaSrdUdpSpecification:
            EnaSrdUdpEnabled: '{{ EnaSrdUdpEnabled }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.network_interface_attachments
WHERE data__Identifier = '<AttachmentId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>network_interface_attachments</code> resource, the following permissions are required:

### Create
```json
ec2:AttachNetworkInterface,
ec2:DescribeNetworkInterfaces,
ec2:ModifyNetworkInterfaceAttribute
```

### Read
```json
ec2:DescribeNetworkInterfaces
```

### List
```json
ec2:DescribeNetworkInterfaces
```

### Update
```json
ec2:ModifyNetworkInterfaceAttribute,
ec2:DescribeNetworkInterfaces,
ec2:AttachNetworkInterface,
ec2:DetachNetworkInterface
```

### Delete
```json
ec2:DetachNetworkInterface,
ec2:DescribeNetworkInterfaces
```

