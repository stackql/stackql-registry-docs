---
title: hours_of_operation
hide_title: false
hide_table_of_contents: false
keywords:
  - hours_of_operation
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>hours_of_operation</code> resource, use <code>hours_of_operations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hours_of_operation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::HoursOfOperation</td></tr>
<tr><td><b>Id</b></td><td><code>aws.connect.hours_of_operation</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the hours of operation.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the hours of operation.</td></tr>
<tr><td><code>time_zone</code></td><td><code>string</code></td><td>The time zone of the hours of operation.</td></tr>
<tr><td><code>config</code></td><td><code>array</code></td><td>Configuration information for the hours of operation: day, start time, and end time.</td></tr>
<tr><td><code>hours_of_operation_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the hours of operation.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>One or more tags.</td></tr>
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
instance_arn,
name,
description,
time_zone,
config,
hours_of_operation_arn,
tags
FROM aws.connect.hours_of_operation
WHERE data__Identifier = '<HoursOfOperationArn>';
```

## Permissions

To operate on the <code>hours_of_operation</code> resource, the following permissions are required:

### Read
```json
connect:DescribeHoursOfOperation
```

### Delete
```json
connect:DeleteHoursOfOperation,
connect:UntagResource
```

### Update
```json
connect:UpdateHoursOfOperation,
connect:TagResource,
connect:UntagResource
```

