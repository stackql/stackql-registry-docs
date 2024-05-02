---
title: environment
hide_title: false
hide_table_of_contents: false
keywords:
  - environment
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
Gets or operates on an individual <code>environment</code> resource, use <code>environments</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppConfig::Environment</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appconfig.environment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>environment_id</code></td><td><code>string</code></td><td>The environment ID.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the environment.</td></tr>
<tr><td><code>monitors</code></td><td><code>array</code></td><td>Amazon CloudWatch alarms to monitor during the deployment process.</td></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Metadata to assign to the environment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A name for the environment.</td></tr>
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
environment_id,
description,
monitors,
application_id,
tags,
name
FROM aws.appconfig.environment
WHERE data__Identifier = '<ApplicationId>|<EnvironmentId>';
```

## Permissions

To operate on the <code>environment</code> resource, the following permissions are required:

### Read
```json
appconfig:GetEnvironment,
appconfig:ListTagsForResource
```

### Update
```json
appconfig:UpdateEnvironment,
appconfig:TagResource,
appconfig:UntagResource,
iam:PassRole
```

### Delete
```json
appconfig:GetEnvironment,
appconfig:DeleteEnvironment
```

