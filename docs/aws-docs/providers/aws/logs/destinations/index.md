---
title: destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - destinations
  - logs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>destinations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Logs::Destination resource specifies a CloudWatch Logs destination. A destination encapsulates a physical resource (such as an Amazon Kinesis data stream) and enables you to subscribe that resource to a stream of log events.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.logs.destinations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>destination_name</code></td><td><code>string</code></td><td>The name of the destination resource</td></tr>
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
destination_name
FROM aws.logs.destinations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>destinations</code> resource, the following permissions are required:

### Create
```json
logs:PutDestination,
logs:PutDestinationPolicy,
logs:DescribeDestinations,
iam:PassRole
```

### List
```json
logs:DescribeDestinations
```

