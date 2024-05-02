---
title: locationf_sx_lustres
hide_title: false
hide_table_of_contents: false
keywords:
  - locationf_sx_lustres
  - datasync
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Used to retrieve a list of <code>locationf_sx_lustres</code> in a region or create a <code>locationf_sx_lustres</code> resource, use <code>locationf_sx_lustre</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locationf_sx_lustres</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationFSxLustre.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.datasync.locationf_sx_lustres</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>location_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon FSx for Lustre file system location that is created.</td></tr>
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
location_arn
FROM aws.datasync.locationf_sx_lustres
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>locationf_sx_lustres</code> resource, the following permissions are required:

### Create
```json
datasync:CreateLocationFsxLustre,
datasync:DescribeLocationFsxLustre,
datasync:ListTagsForResource,
datasync:TagResource,
fsx:DescribeFileSystems,
ec2:DescribeNetworkInterfaces,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups
```

### List
```json
datasync:ListLocations
```

