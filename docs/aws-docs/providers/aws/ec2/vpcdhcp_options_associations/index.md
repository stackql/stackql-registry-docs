---
title: vpcdhcp_options_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - vpcdhcp_options_associations
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
Retrieves a list of <code>vpcdhcp_options_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpcdhcp_options_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates a set of DHCP options with a VPC, or associates no DHCP options with the VPC.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpcdhcp_options_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>dhcp_options_id</code></td><td><code>string</code></td><td>The ID of the DHCP options set, or default to associate no DHCP options with the VPC.</td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
dhcp_options_id,
vpc_id
FROM aws.ec2.vpcdhcp_options_associations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>vpcdhcp_options_associations</code> resource, the following permissions are required:

### Create
```json
ec2:AssociateDhcpOptions
```

### List
```json
ec2:DescribeVpcs
```

