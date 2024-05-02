---
title: theme
hide_title: false
hide_table_of_contents: false
keywords:
  - theme
  - amplifyuibuilder
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>theme</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>theme</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::AmplifyUIBuilder::Theme Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.amplifyuibuilder.theme</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>app_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>environment_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>modified_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>overrides</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>values</code></td><td><code>array</code></td><td></td></tr>
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
app_id,
created_at,
environment_name,
id,
modified_at,
name,
overrides,
tags,
values
FROM aws.amplifyuibuilder.theme
WHERE data__Identifier = '<AppId>|<EnvironmentName>|<Id>';
```

## Permissions

To operate on the <code>theme</code> resource, the following permissions are required:

### Read
```json
amplify:GetApp,
amplifyuibuilder:GetTheme
```

### Update
```json
amplify:GetApp,
amplifyuibuilder:GetTheme,
amplifyuibuilder:TagResource,
amplifyuibuilder:UntagResource,
amplifyuibuilder:UpdateTheme
```

### Delete
```json
amplify:GetApp,
amplifyuibuilder:DeleteTheme,
amplifyuibuilder:UntagResource
```

