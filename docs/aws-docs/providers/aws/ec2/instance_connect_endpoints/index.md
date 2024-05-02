---
title: instance_connect_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_connect_endpoints
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
Retrieves a list of <code>instance_connect_endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_connect_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::InstanceConnectEndpoint</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.instance_connect_endpoints</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The id of the instance connect endpoint</td></tr>
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
id
FROM aws.ec2.instance_connect_endpoints
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>instance_connect_endpoints</code> resource, the following permissions are required:

### Create
```json
ec2:CreateInstanceConnectEndpoint,
ec2:DescribeInstanceConnectEndpoints,
ec2:CreateTags,
ec2:CreateNetworkInterface,
iam:CreateServiceLinkedRole
```

### List
```json
ec2:DescribeInstanceConnectEndpoints
```

