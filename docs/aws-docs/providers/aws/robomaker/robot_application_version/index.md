---
title: robot_application_version
hide_title: false
hide_table_of_contents: false
keywords:
  - robot_application_version
  - robomaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>robot_application_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>robot_application_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::RoboMaker::RobotApplicationVersion resource creates an AWS RoboMaker RobotApplicationVersion. This helps you control which code your robot uses.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.robomaker.robot_application_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>application</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>current_revision_id</code></td><td><code>string</code></td><td>The revision ID of robot application.</td></tr>
<tr><td><code>application_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
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
application,
current_revision_id,
application_version,
arn
FROM aws.robomaker.robot_application_version
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>robot_application_version</code> resource, the following permissions are required:

### Delete
```json
robomaker:DeleteRobotApplication,
robomaker:DescribeRobotApplication
```

### Read
```json
robomaker:DescribeRobotApplication
```

