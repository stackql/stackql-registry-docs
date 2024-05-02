---
title: component_version
hide_title: false
hide_table_of_contents: false
keywords:
  - component_version
  - greengrassv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>component_version</code> resource, use <code>component_versions</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource for Greengrass component version.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.greengrassv2.component_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>component_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>component_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>inline_recipe</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>lambda_function</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
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
arn,
component_name,
component_version,
inline_recipe,
lambda_function,
tags
FROM aws.greengrassv2.component_version
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>component_version</code> resource, the following permissions are required:

### Read
```json
greengrass:DescribeComponent,
greengrass:ListTagsForResource
```

### Update
```json
greengrass:DescribeComponent,
greengrass:ListTagsForResource,
greengrass:TagResource,
greengrass:UntagResource
```

### Delete
```json
greengrass:DeleteComponent
```

