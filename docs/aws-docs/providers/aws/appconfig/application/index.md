---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
  - appconfig
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>application</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppConfig::Application</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appconfig.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the application.</td></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td>The application Id</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Metadata to assign to the application. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A name for the application.</td></tr>
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
description,
application_id,
tags,
name
FROM aws.appconfig.application
WHERE data__Identifier = '<ApplicationId>';
```

## Permissions

To operate on the <code>application</code> resource, the following permissions are required:

### Read
```json
appconfig:GetApplication,
appconfig:ListTagsForResource
```

### Update
```json
appconfig:UpdateApplication,
appconfig:TagResource,
appconfig:UntagResource
```

### Delete
```json
appconfig:GetApplication,
appconfig:DeleteApplication
```

