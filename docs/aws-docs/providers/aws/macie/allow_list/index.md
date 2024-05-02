---
title: allow_list
hide_title: false
hide_table_of_contents: false
keywords:
  - allow_list
  - macie
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>allow_list</code> resource, use <code>allow_lists</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>allow_list</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Macie AllowList resource schema</td></tr>
<tr><td><b>Id</b></td><td><code>aws.macie.allow_list</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of AllowList.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of AllowList.</td></tr>
<tr><td><code>criteria</code></td><td><code>object</code></td><td>AllowList criteria.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>AllowList ID.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>AllowList ARN.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>AllowList status.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
name,
description,
criteria,
id,
arn,
status,
tags
FROM aws.macie.allow_list
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>allow_list</code> resource, the following permissions are required:

### Read
```json
macie2:GetAllowList
```

### Update
```json
macie2:UpdateAllowList,
macie2:GetAllowList,
macie2:TagResource,
macie2:UntagResource
```

### Delete
```json
macie2:DeleteAllowList
```

