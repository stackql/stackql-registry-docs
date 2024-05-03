---
title: robot
hide_title: false
hide_table_of_contents: false
keywords:
  - robot
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

Gets or operates on an individual <code>robot</code> resource, use <code>robots</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>robot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::RoboMaker::Robot resource creates an AWS RoboMaker Robot.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.robomaker.robot" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="fleet" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the fleet.</td></tr>
<tr><td><CopyableCode code="architecture" /></td><td><code>string</code></td><td>The target architecture of the robot.</td></tr>
<tr><td><CopyableCode code="greengrass_group_id" /></td><td><code>string</code></td><td>The Greengrass group id.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the robot.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
arn,
fleet,
architecture,
greengrass_group_id,
tags,
name
FROM aws.robomaker.robot
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>robot</code> resource, the following permissions are required:

### Read
```json
robomaker:DescribeRobot
```

### Delete
```json
robomaker:DescribeRobot,
robomaker:DeleteRobot,
robomaker:DeregisterRobot
```

### Update
```json
robomaker:TagResource,
robomaker:UntagResource
```

