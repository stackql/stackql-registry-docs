---
title: stage
hide_title: false
hide_table_of_contents: false
keywords:
  - stage
  - ivs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>stage</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Definition for type AWS::IVS::Stage.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ivs.stage</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Stage ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Stage name</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>active_session_id</code></td><td><code>string</code></td><td>ID of the active session within the stage.</td></tr>
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
name,
tags,
active_session_id
FROM aws.ivs.stage
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>stage</code> resource, the following permissions are required:

### Read
```json
ivs:GetStage,
ivs:ListTagsForResource
```

### Update
```json
ivs:GetStage,
ivs:UpdateStage,
ivs:TagResource,
ivs:UnTagResource,
ivs:ListTagsForResource
```

### Delete
```json
ivs:DeleteStage,
ivs:UnTagResource
```

