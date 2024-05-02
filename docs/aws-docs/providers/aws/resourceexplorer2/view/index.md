---
title: view
hide_title: false
hide_table_of_contents: false
keywords:
  - view
  - resourceexplorer2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>view</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>view</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ResourceExplorer2::View Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.resourceexplorer2.view</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>filters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>included_properties</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>scope</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>view_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>view_name</code></td><td><code>string</code></td><td></td></tr>
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
filters,
included_properties,
scope,
tags,
view_arn,
view_name
FROM aws.resourceexplorer2.view
WHERE data__Identifier = '<ViewArn>';
```

## Permissions

To operate on the <code>view</code> resource, the following permissions are required:

### Read
```json
resource-explorer-2:GetView
```

### Update
```json
resource-explorer-2:UpdateView,
resource-explorer-2:TagResource,
resource-explorer-2:UntagResource,
resource-explorer-2:ListTagsForResource
```

### Delete
```json
resource-explorer-2:DeleteView,
resource-explorer-2:GetView,
resource-explorer-2:UntagResource
```

