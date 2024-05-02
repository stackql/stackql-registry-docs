---
title: in_app_template
hide_title: false
hide_table_of_contents: false
keywords:
  - in_app_template
  - pinpoint
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>in_app_template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>in_app_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Pinpoint::InAppTemplate</td></tr>
<tr><td><b>Id</b></td><td><code>aws.pinpoint.in_app_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>content</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>custom_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>layout</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>template_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>template_name</code></td><td><code>string</code></td><td></td></tr>
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
content,
custom_config,
layout,
tags,
template_description,
template_name
FROM aws.pinpoint.in_app_template
WHERE data__Identifier = '<TemplateName>';
```

## Permissions

To operate on the <code>in_app_template</code> resource, the following permissions are required:

### Delete
```json
mobiletargeting:DeleteInAppTemplate,
mobiletargeting:GetInAppTemplate
```

### Read
```json
mobiletargeting:GetInAppTemplate,
mobiletargeting:ListTemplates
```

### Update
```json
mobiletargeting:UpdateInAppTemplate,
mobiletargeting:GetInAppTemplate
```

