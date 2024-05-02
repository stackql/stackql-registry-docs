---
title: dataset
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset
  - databrew
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>dataset</code> resource, use <code>datasets</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataBrew::Dataset.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.databrew.dataset</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Dataset name</td></tr>
<tr><td><code>format</code></td><td><code>string</code></td><td>Dataset format</td></tr>
<tr><td><code>format_options</code></td><td><code>object</code></td><td>Format options for dataset</td></tr>
<tr><td><code>input</code></td><td><code>object</code></td><td>Input</td></tr>
<tr><td><code>path_options</code></td><td><code>object</code></td><td>PathOptions</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
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
format,
format_options,
input,
path_options,
tags
FROM aws.databrew.dataset
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>dataset</code> resource, the following permissions are required:

### Read
```json
databrew:DescribeDataset,
databrew:ListTagsForResource,
iam:ListRoles
```

### Update
```json
databrew:UpdateDataset,
glue:GetConnection,
glue:GetTable
```

### Delete
```json
databrew:DeleteDataset
```

