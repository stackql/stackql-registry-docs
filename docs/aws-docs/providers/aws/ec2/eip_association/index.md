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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>eip_association</code> resource, use <code>eip_associations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>eip_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for EC2 EIP association.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.eip_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Composite ID of non-empty properties, to determine the identification.</td></tr>
<tr><td><CopyableCode code="allocation_id" /></td><td><code>string</code></td><td>The allocation ID. This is required for EC2-VPC.</td></tr>
<tr><td><CopyableCode code="network_interface_id" /></td><td><code>string</code></td><td>The ID of the network interface.</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>The ID of the instance.</td></tr>
<tr><td><CopyableCode code="private_ip_address" /></td><td><code>string</code></td><td>The primary or secondary private IP address to associate with the Elastic IP address.</td></tr>
<tr><td><CopyableCode code="e_ip" /></td><td><code>string</code></td><td>The Elastic IP address to associate with the instance.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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

