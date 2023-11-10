---
title: acl
hide_title: false
hide_table_of_contents: false
keywords:
  - acl
  - memorydb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>acl</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>acl</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>acl</td></tr>
<tr><td><b>Id</b></td><td><code>aws.memorydb.acl</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>Indicates acl status. Can be "creating", "active", "modifying", "deleting".</td></tr>
<tr><td><code>a_cl_name</code></td><td><code>string</code></td><td>The name of the acl.</td></tr>
<tr><td><code>user_names</code></td><td><code>array</code></td><td>List of users associated to this acl.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the acl.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this cluster.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
status,
a_cl_name,
user_names,
arn,
tags
FROM aws.memorydb.acl
WHERE region = 'us-east-1'
AND data__Identifier = '<ACLName>'
```
