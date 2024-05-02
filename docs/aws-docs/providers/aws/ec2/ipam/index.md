---
title: ipam
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam
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
Gets an individual <code>ipam</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAM Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.ipam</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ipam_id</code></td><td><code>string</code></td><td>Id of the IPAM.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IPAM.</td></tr>
<tr><td><code>default_resource_discovery_id</code></td><td><code>string</code></td><td>The Id of the default resource discovery, created with this IPAM.</td></tr>
<tr><td><code>default_resource_discovery_association_id</code></td><td><code>string</code></td><td>The Id of the default association to the default resource discovery, created with this IPAM.</td></tr>
<tr><td><code>resource_discovery_association_count</code></td><td><code>integer</code></td><td>The count of resource discoveries associated with this IPAM.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>public_default_scope_id</code></td><td><code>string</code></td><td>The Id of the default scope for publicly routable IP space, created with this IPAM.</td></tr>
<tr><td><code>private_default_scope_id</code></td><td><code>string</code></td><td>The Id of the default scope for publicly routable IP space, created with this IPAM.</td></tr>
<tr><td><code>scope_count</code></td><td><code>integer</code></td><td>The number of scopes that currently exist in this IPAM.</td></tr>
<tr><td><code>operating_regions</code></td><td><code>array</code></td><td>The regions IPAM is enabled for. Allows pools to be created in these regions, as well as enabling monitoring</td></tr>
<tr><td><code>tier</code></td><td><code>string</code></td><td>The tier of the IPAM.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
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
ipam_id,
arn,
default_resource_discovery_id,
default_resource_discovery_association_id,
resource_discovery_association_count,
description,
public_default_scope_id,
private_default_scope_id,
scope_count,
operating_regions,
tier,
tags
FROM aws.ec2.ipam
WHERE data__Identifier = '<IpamId>';
```

## Permissions

To operate on the <code>ipam</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeIpams
```

### Update
```json
ec2:ModifyIpam,
ec2:CreateTags,
ec2:DeleteTags,
ec2:DescribeIpams
```

### Delete
```json
ec2:DeleteIpam,
ec2:DeleteTags,
ec2:DescribeIpams
```

