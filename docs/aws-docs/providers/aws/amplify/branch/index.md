---
title: branch
hide_title: false
hide_table_of_contents: false
keywords:
  - branch
  - amplify
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>branch</code> resource, use <code>branches</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>branch</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Amplify::Branch resource creates a new branch within an app.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.amplify.branch</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>app_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>basic_auth_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>backend</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>branch_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>build_spec</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enable_auto_build</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>enable_performance_mode</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>enable_pull_request_preview</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>environment_variables</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>framework</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>pull_request_environment_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stage</code></td><td><code>string</code></td><td></td></tr>
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
app_id,
arn,
basic_auth_config,
backend,
branch_name,
build_spec,
description,
enable_auto_build,
enable_performance_mode,
enable_pull_request_preview,
environment_variables,
framework,
pull_request_environment_name,
stage,
tags
FROM aws.amplify.branch
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>branch</code> resource, the following permissions are required:

### Delete
```json
amplify:GetBranch,
amplify:DeleteBranch,
codecommit:GetRepository,
codecommit:GetRepositoryTriggers,
sns:Unsubscribe,
iam:PassRole
```

### Read
```json
amplify:GetBranch,
amplify:ListTagsForResource,
codecommit:GetRepository,
codecommit:GetRepositoryTriggers,
s3:GetObject,
s3:GetObjectAcl,
iam:PassRole
```

### Update
```json
amplify:GetBranch,
amplify:UpdateBranch,
amplify:ListTagsForResource,
amplify:TagResource,
amplify:UntagResource,
codecommit:GetRepository,
codecommit:PutRepositoryTriggers,
codecommit:GetRepositoryTriggers,
s3:GetObject,
s3:GetObjectAcl,
s3:PutObject,
s3:PutObjectAcl,
sns:CreateTopic,
sns:Subscribe,
sns:Unsubscribe,
iam:PassRole
```

