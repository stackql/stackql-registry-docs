---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
  - appintegrations
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>application</code> resource, use <code>applications</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS:AppIntegrations::Application</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appintegrations.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the application.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The id of the application.</td></tr>
<tr><td><code>namespace</code></td><td><code>string</code></td><td>The namespace of the application.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The application description.</td></tr>
<tr><td><code>application_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the application.</td></tr>
<tr><td><code>application_source_config</code></td><td><code>object</code></td><td>Application source config</td></tr>
<tr><td><code>permissions</code></td><td><code>array</code></td><td>The configuration of events or requests that the application has access to.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags (keys and values) associated with the application.</td></tr>
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
id,
namespace,
description,
application_arn,
application_source_config,
permissions,
tags
FROM aws.appintegrations.application
WHERE data__Identifier = '<ApplicationArn>';
```

## Permissions

To operate on the <code>application</code> resource, the following permissions are required:

### Read
```json
app-integrations:GetApplication
```

### Update
```json
app-integrations:GetApplication,
app-integrations:UpdateApplication,
app-integrations:TagResource,
app-integrations:UntagResource
```

### Delete
```json
app-integrations:DeleteApplication
```

