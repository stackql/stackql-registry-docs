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
Gets an individual <code>robot</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>robot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>robot</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.robomaker.robot</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>fleet</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the fleet.</td></tr>
<tr><td><code>architecture</code></td><td><code>string</code></td><td>The target architecture of the robot.</td></tr>
<tr><td><code>greengrass_group_id</code></td><td><code>string</code></td><td>The Greengrass group id.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name for the robot.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>robot</code> resource, the following permissions are required:

### Read
<pre>
robomaker:DescribeRobot</pre>

### Delete
<pre>
robomaker:DescribeRobot,
robomaker:DeleteRobot,
robomaker:DeregisterRobot</pre>

### Update
<pre>
robomaker:TagResource,
robomaker:UntagResource</pre>


## Example
```sql
SELECT
region,
arn,
fleet,
architecture,
greengrass_group_id,
tags,
name
FROM awscc.robomaker.robot
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
