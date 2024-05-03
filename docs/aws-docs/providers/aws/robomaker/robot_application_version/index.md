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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>robot_application_version</code> resource, use <code>robot_application_versions</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>robot_application_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::RoboMaker::RobotApplicationVersion resource creates an AWS RoboMaker RobotApplicationVersion. This helps you control which code your robot uses.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.robomaker.robot_application_version" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="application" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="current_revision_id" /></td><td><code>string</code></td><td>The revision ID of robot application.</td></tr>
<tr><td><CopyableCode code="application_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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

