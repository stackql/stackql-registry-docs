---
title: network_interface_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interface_attachment
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
Gets an individual <code>network_interface_attachment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_interface_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>network_interface_attachment</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.network_interface_attachment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>attachment_id</code></td><td><code>string</code></td><td>The ID of the network interface attachment.</td></tr>
<tr><td><code>delete_on_termination</code></td><td><code>boolean</code></td><td>Whether to delete the network interface when the instance terminates. By default, this value is set to true.</td></tr>
<tr><td><code>device_index</code></td><td><code>string</code></td><td>The network interface's position in the attachment order. For example, the first attached network interface has a DeviceIndex of 0.</td></tr>
<tr><td><code>instance_id</code></td><td><code>string</code></td><td>The ID of the instance to which you will attach the ENI.</td></tr>
<tr><td><code>network_interface_id</code></td><td><code>string</code></td><td>The ID of the ENI that you want to attach.</td></tr>
<tr><td><code>ena_srd_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
attachment_id,
delete_on_termination,
device_index,
instance_id,
network_interface_id,
ena_srd_specification
FROM awscc.ec2.network_interface_attachment
WHERE data__Identifier = '<AttachmentId>';
```

## Permissions

To operate on the <code>network_interface_attachment</code> resource, the following permissions are required:

### Read
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

