---
title: eip_association
hide_title: false
hide_table_of_contents: false
keywords:
  - eip_association
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
Gets an individual <code>eip_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>eip_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for EC2 EIP association.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.eip_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Composite ID of non-empty properties, to determine the identification.</td></tr>
<tr><td><code>allocation_id</code></td><td><code>string</code></td><td>The allocation ID. This is required for EC2-VPC.</td></tr>
<tr><td><code>network_interface_id</code></td><td><code>string</code></td><td>The ID of the network interface.</td></tr>
<tr><td><code>instance_id</code></td><td><code>string</code></td><td>The ID of the instance.</td></tr>
<tr><td><code>private_ip_address</code></td><td><code>string</code></td><td>The primary or secondary private IP address to associate with the Elastic IP address.</td></tr>
<tr><td><code>e_ip</code></td><td><code>string</code></td><td>The Elastic IP address to associate with the instance.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id,
allocation_id,
network_interface_id,
instance_id,
private_ip_address,
e_ip
FROM aws.ec2.eip_association
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>eip_association</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeAddresses
```

### Delete
```json
ec2:DisassociateAddress,
ec2:DescribeAddresses
```

