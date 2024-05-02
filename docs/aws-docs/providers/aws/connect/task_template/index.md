---
title: task_template
hide_title: false
hide_table_of_contents: false
keywords:
  - task_template
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>task_template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::TaskTemplate.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.connect.task_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The identifier (arn) of the task template.</td></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The identifier (arn) of the instance.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the task template.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the task template.</td></tr>
<tr><td><code>contact_flow_arn</code></td><td><code>string</code></td><td>The identifier of the contact flow.</td></tr>
<tr><td><code>constraints</code></td><td><code>object</code></td><td>The constraints for the task template</td></tr>
<tr><td><code>defaults</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>fields</code></td><td><code>array</code></td><td>The list of task template's fields</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>client_token</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>One or more tags.</td></tr>
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
instance_arn,
name,
description,
contact_flow_arn,
constraints,
defaults,
fields,
status,
client_token,
tags
FROM aws.connect.task_template
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>task_template</code> resource, the following permissions are required:

### Read
```json
connect:GetTaskTemplate
```

### Update
```json
connect:UpdateTaskTemplate,
connect:TagResource,
connect:UntagResource
```

### Delete
```json
connect:DeleteTaskTemplate,
connect:UntagResource,
connect:GetTaskTemplate
```

