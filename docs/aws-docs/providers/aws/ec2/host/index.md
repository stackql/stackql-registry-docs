---
title: host
hide_title: false
hide_table_of_contents: false
keywords:
  - host
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
Gets an individual <code>host</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>host</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::Host</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.host</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>host_id</code></td><td><code>string</code></td><td>ID of the host created.</td></tr>
<tr><td><code>auto_placement</code></td><td><code>string</code></td><td>Indicates whether the host accepts any untargeted instance launches that match its instance type configuration, or if it only accepts Host tenancy instance launches that specify its unique host ID.</td></tr>
<tr><td><code>availability_zone</code></td><td><code>string</code></td><td>The Availability Zone in which to allocate the Dedicated Host.</td></tr>
<tr><td><code>host_recovery</code></td><td><code>string</code></td><td>Indicates whether to enable or disable host recovery for the Dedicated Host. Host recovery is disabled by default.</td></tr>
<tr><td><code>instance_type</code></td><td><code>string</code></td><td>Specifies the instance type to be supported by the Dedicated Hosts. If you specify an instance type, the Dedicated Hosts support instances of the specified instance type only.</td></tr>
<tr><td><code>instance_family</code></td><td><code>string</code></td><td>Specifies the instance family to be supported by the Dedicated Hosts. If you specify an instance family, the Dedicated Hosts support multiple instance types within that instance family.</td></tr>
<tr><td><code>outpost_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon Web Services Outpost on which to allocate the Dedicated Host.</td></tr>
<tr><td><code>host_maintenance</code></td><td><code>string</code></td><td>Automatically allocates a new dedicated host and moves your instances on to it if a degradation is detected on your current host.</td></tr>
<tr><td><code>asset_id</code></td><td><code>string</code></td><td>The ID of the Outpost hardware asset.</td></tr>
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
host_id,
auto_placement,
availability_zone,
host_recovery,
instance_type,
instance_family,
outpost_arn,
host_maintenance,
asset_id
FROM aws.ec2.host
WHERE data__Identifier = '<HostId>';
```

## Permissions

To operate on the <code>host</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeHosts
```

### Update
```json
ec2:ModifyHosts,
ec2:DescribeHosts
```

### Delete
```json
ec2:ReleaseHosts,
ec2:DescribeHosts
```

