---
title: frauddetector_list
hide_title: false
hide_table_of_contents: false
keywords:
  - frauddetector_list
  - frauddetector
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>frauddetector_list</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>frauddetector_list</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema for a List in Amazon Fraud Detector.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.frauddetector.frauddetector_list</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The list ARN.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the list.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the list.</td></tr>
<tr><td><code>variable_type</code></td><td><code>string</code></td><td>The variable type of the list.</td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td>The time when the list was created.</td></tr>
<tr><td><code>last_updated_time</code></td><td><code>string</code></td><td>The time when the list was last updated.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags associated with this list.</td></tr>
<tr><td><code>elements</code></td><td><code>array</code></td><td>The elements in this list.</td></tr>
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
description,
variable_type,
created_time,
last_updated_time,
tags,
elements
FROM aws.frauddetector.frauddetector_list
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>frauddetector_list</code> resource, the following permissions are required:

### Read
```json
frauddetector:GetListElements,
frauddetector:GetListsMetadata,
frauddetector:ListTagsForResource
```

### Update
```json
frauddetector:GetListElements,
frauddetector:GetListsMetadata,
frauddetector:ListTagsForResource,
frauddetector:UntagResource,
frauddetector:UpdateList,
frauddetector:TagResource
```

### Delete
```json
frauddetector:DeleteList,
frauddetector:GetListsMetadata
```

