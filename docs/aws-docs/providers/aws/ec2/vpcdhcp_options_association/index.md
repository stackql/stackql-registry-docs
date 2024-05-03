---
title: vpcdhcp_options_association
hide_title: false
hide_table_of_contents: false
keywords:
  - vpcdhcp_options_association
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

Gets or operates on an individual <code>vpcdhcp_options_association</code> resource, use <code>vpcdhcp_options_associations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpcdhcp_options_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates a set of DHCP options with a VPC, or associates no DHCP options with the VPC.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpcdhcp_options_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="dhcp_options_id" /></td><td><code>string</code></td><td>The ID of the DHCP options set, or default to associate no DHCP options with the VPC.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
dhcp_options_id,
vpc_id
FROM aws.ec2.vpcdhcp_options_association
WHERE data__Identifier = '<DhcpOptionsId>|<VpcId>';
```

## Permissions

To operate on the <code>vpcdhcp_options_association</code> resource, the following permissions are required:

### Update
```json
ec2:AssociateDhcpOptions
```

### Delete
```json
ec2:AssociateDhcpOptions
```

### Read
```json
ec2:DescribeVpcs
```

