---
title: custom_plugin
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_plugin
  - kafkaconnect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>custom_plugin</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_plugin</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kafkaconnect.custom_plugin</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the custom plugin.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A summary description of the custom plugin.</td></tr>
<tr><td><code>custom_plugin_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the custom plugin to use.</td></tr>
<tr><td><code>content_type</code></td><td><code>string</code></td><td>The type of the plugin file.</td></tr>
<tr><td><code>file_description</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>location</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>revision</code></td><td><code>integer</code></td><td>The revision of the custom plugin.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
custom_plugin_arn,
content_type,
file_description,
location,
revision,
tags
FROM aws.kafkaconnect.custom_plugin
WHERE data__Identifier = '<CustomPluginArn>';
```

## Permissions

To operate on the <code>custom_plugin</code> resource, the following permissions are required:

### Read
```json
kafkaconnect:DescribeCustomPlugin,
kafkaconnect:ListTagsForResource
```

### Update
```json
kafkaconnect:DescribeCustomPlugin,
kafkaconnect:ListTagsForResource,
kafkaconnect:TagResource,
kafkaconnect:UntagResource
```

### Delete
```json
kafkaconnect:DeleteCustomPlugin,
kafkaconnect:DescribeCustomPlugin
```

