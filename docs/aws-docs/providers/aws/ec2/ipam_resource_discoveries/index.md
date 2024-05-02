---
title: ipam_resource_discoveries
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_resource_discoveries
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
Used to retrieve a list of <code>ipam_resource_discoveries</code> in a region or create a <code>ipam_resource_discoveries</code> resource, use <code>ipam_resource_discovery</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_resource_discoveries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAMResourceDiscovery Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.ipam_resource_discoveries</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ipam_resource_discovery_id</code></td><td><code>string</code></td><td>Id of the IPAM Pool.</td></tr>
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
ipam_resource_discovery_id
FROM aws.ec2.ipam_resource_discoveries
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>ipam_resource_discoveries</code> resource, the following permissions are required:

### Create
```json
ec2:CreateIpamResourceDiscovery,
ec2:DescribeIpamResourceDiscoveries,
ec2:CreateTags
```

### List
```json
ec2:DescribeIpamResourceDiscoveries
```

