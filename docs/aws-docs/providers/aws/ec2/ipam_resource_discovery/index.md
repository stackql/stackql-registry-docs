---
title: ipam_resource_discovery
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_resource_discovery
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
Gets or operates on an individual <code>ipam_resource_discovery</code> resource, use <code>ipam_resource_discoveries</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_resource_discovery</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAMResourceDiscovery Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.ipam_resource_discovery</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ipam_resource_discovery_id</code></td><td><code>string</code></td><td>Id of the IPAM Pool.</td></tr>
<tr><td><code>owner_id</code></td><td><code>string</code></td><td>Owner Account ID of the Resource Discovery</td></tr>
<tr><td><code>operating_regions</code></td><td><code>array</code></td><td>The regions Resource Discovery is enabled for. Allows resource discoveries to be created in these regions, as well as enabling monitoring</td></tr>
<tr><td><code>ipam_resource_discovery_region</code></td><td><code>string</code></td><td>The region the resource discovery is setup in. </td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>is_default</code></td><td><code>boolean</code></td><td>Determines whether or not address space from this pool is publicly advertised. Must be set if and only if the pool is IPv6.</td></tr>
<tr><td><code>ipam_resource_discovery_arn</code></td><td><code>string</code></td><td>Amazon Resource Name (Arn) for the Resource Discovery.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of this Resource Discovery.</td></tr>
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
ipam_resource_discovery_id,
owner_id,
operating_regions,
ipam_resource_discovery_region,
description,
is_default,
ipam_resource_discovery_arn,
state,
tags
FROM aws.ec2.ipam_resource_discovery
WHERE data__Identifier = '<IpamResourceDiscoveryId>';
```

## Permissions

To operate on the <code>ipam_resource_discovery</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeIpamResourceDiscoveries
```

### Update
```json
ec2:ModifyIpamResourceDiscovery,
ec2:DescribeIpamResourceDiscoveries,
ec2:CreateTags,
ec2:DeleteTags
```

### Delete
```json
ec2:DeleteIpamResourceDiscovery,
ec2:DescribeIpamResourceDiscoveries,
ec2:DeleteTags
```

