---
title: user_hierarchy_group
hide_title: false
hide_table_of_contents: false
keywords:
  - user_hierarchy_group
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
Gets an individual <code>user_hierarchy_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_hierarchy_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user_hierarchy_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.connect.user_hierarchy_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><code>user_hierarchy_group_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the user hierarchy group.</td></tr>
<tr><td><code>parent_group_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the parent user hierarchy group.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the user hierarchy group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
instance_arn,
user_hierarchy_group_arn,
parent_group_arn,
name
FROM aws.connect.user_hierarchy_group
WHERE region = 'us-east-1'
AND data__Identifier = '<UserHierarchyGroupArn>'
```
