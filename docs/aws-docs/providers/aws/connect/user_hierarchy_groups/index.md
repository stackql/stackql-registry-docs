---
title: user_hierarchy_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - user_hierarchy_groups
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
Retrieves a list of <code>user_hierarchy_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_hierarchy_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.connect.user_hierarchy_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>InstanceArn</code></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr><tr><td><code>UserHierarchyGroupArn</code></td><td><code>undefined</code></td><td>The Amazon Resource Name (ARN) for the user hierarchy group.</td></tr><tr><td><code>ParentGroupArn</code></td><td><code>undefined</code></td><td>The Amazon Resource Name (ARN) for the parent user hierarchy group.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the user hierarchy group.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.connect.user_hierarchy_groups
WHERE region = 'us-east-1'
```
