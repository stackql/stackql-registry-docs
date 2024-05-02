---
title: lifecycle_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_policy
  - imagebuilder
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>lifecycle_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lifecycle_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::LifecyclePolicy</td></tr>
<tr><td><b>Id</b></td><td><code>aws.imagebuilder.lifecycle_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the lifecycle policy.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the lifecycle policy.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the lifecycle policy.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the lifecycle policy.</td></tr>
<tr><td><code>execution_role</code></td><td><code>string</code></td><td>The execution role of the lifecycle policy.</td></tr>
<tr><td><code>resource_type</code></td><td><code>string</code></td><td>The resource type of the lifecycle policy.</td></tr>
<tr><td><code>policy_details</code></td><td><code>array</code></td><td>The policy details of the lifecycle policy.</td></tr>
<tr><td><code>resource_selection</code></td><td><code>object</code></td><td>The resource selection of the lifecycle policy.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>The tags associated with the lifecycle policy.</td></tr>
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
status,
execution_role,
resource_type,
policy_details,
resource_selection,
tags
FROM aws.imagebuilder.lifecycle_policy
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>lifecycle_policy</code> resource, the following permissions are required:

### Update
```json
iam:PassRole,
imagebuilder:GetLifecyclePolicy,
imagebuilder:UpdateLifecyclePolicy
```

### Read
```json
imagebuilder:GetLifecyclePolicy
```

### Delete
```json
imagebuilder:GetLifecyclePolicy,
imagebuilder:DeleteLifecyclePolicy,
imagebuilder:UnTagResource
```

