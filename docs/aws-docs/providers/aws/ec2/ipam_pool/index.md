---
title: ipam_pool
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_pool
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
Gets or operates on an individual <code>ipam_pool</code> resource, use <code>ipam_pools</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAMPool Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.ipam_pool</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ipam_pool_id</code></td><td><code>string</code></td><td>Id of the IPAM Pool.</td></tr>
<tr><td><code>address_family</code></td><td><code>string</code></td><td>The address family of the address space in this pool. Either IPv4 or IPv6.</td></tr>
<tr><td><code>allocation_min_netmask_length</code></td><td><code>integer</code></td><td>The minimum allowed netmask length for allocations made from this pool.</td></tr>
<tr><td><code>allocation_default_netmask_length</code></td><td><code>integer</code></td><td>The default netmask length for allocations made from this pool. This value is used when the netmask length of an allocation isn't specified.</td></tr>
<tr><td><code>allocation_max_netmask_length</code></td><td><code>integer</code></td><td>The maximum allowed netmask length for allocations made from this pool.</td></tr>
<tr><td><code>allocation_resource_tags</code></td><td><code>array</code></td><td>When specified, an allocation will not be allowed unless a resource has a matching set of tags.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IPAM Pool.</td></tr>
<tr><td><code>auto_import</code></td><td><code>boolean</code></td><td>Determines what to do if IPAM discovers resources that haven't been assigned an allocation. If set to true, an allocation will be made automatically.</td></tr>
<tr><td><code>aws_service</code></td><td><code>string</code></td><td>Limits which service in Amazon Web Services that the pool can be used in.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ipam_scope_id</code></td><td><code>string</code></td><td>The Id of the scope this pool is a part of.</td></tr>
<tr><td><code>ipam_scope_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the scope this pool is a part of.</td></tr>
<tr><td><code>ipam_scope_type</code></td><td><code>string</code></td><td>Determines whether this scope contains publicly routable space or space for a private network</td></tr>
<tr><td><code>ipam_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IPAM this pool is a part of.</td></tr>
<tr><td><code>locale</code></td><td><code>string</code></td><td>The region of this pool. If not set, this will default to "None" which will disable non-custom allocations. If the locale has been specified for the source pool, this value must match.</td></tr>
<tr><td><code>pool_depth</code></td><td><code>integer</code></td><td>The depth of this pool in the source pool hierarchy.</td></tr>
<tr><td><code>provisioned_cidrs</code></td><td><code>array</code></td><td>A list of cidrs representing the address space available for allocation in this pool.</td></tr>
<tr><td><code>public_ip_source</code></td><td><code>string</code></td><td>The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is `byoip`.</td></tr>
<tr><td><code>publicly_advertisable</code></td><td><code>boolean</code></td><td>Determines whether or not address space from this pool is publicly advertised. Must be set if and only if the pool is IPv6.</td></tr>
<tr><td><code>source_ipam_pool_id</code></td><td><code>string</code></td><td>The Id of this pool's source. If set, all space provisioned in this pool must be free space provisioned in the parent pool.</td></tr>
<tr><td><code>source_resource</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of this pool. This can be one of the following values: "create-in-progress", "create-complete", "modify-in-progress", "modify-complete", "delete-in-progress", or "delete-complete"</td></tr>
<tr><td><code>state_message</code></td><td><code>string</code></td><td>An explanation of how the pool arrived at it current state.</td></tr>
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
ipam_pool_id,
address_family,
allocation_min_netmask_length,
allocation_default_netmask_length,
allocation_max_netmask_length,
allocation_resource_tags,
arn,
auto_import,
aws_service,
description,
ipam_scope_id,
ipam_scope_arn,
ipam_scope_type,
ipam_arn,
locale,
pool_depth,
provisioned_cidrs,
public_ip_source,
publicly_advertisable,
source_ipam_pool_id,
source_resource,
state,
state_message,
tags
FROM aws.ec2.ipam_pool
WHERE data__Identifier = '<IpamPoolId>';
```

## Permissions

To operate on the <code>ipam_pool</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeIpamPools,
ec2:GetIpamPoolCidrs
```

### Update
```json
ec2:ModifyIpamPool,
ec2:DescribeIpamPools,
ec2:GetIpamPoolCidrs,
ec2:ProvisionIpamPoolCidr,
ec2:DeprovisionIpamPoolCidr,
ec2:CreateTags,
ec2:DeleteTags
```

### Delete
```json
ec2:DeleteIpamPool,
ec2:DescribeIpamPools,
ec2:GetIpamPoolCidrs,
ec2:DeprovisionIpamPoolCidr,
ec2:DeleteTags
```

