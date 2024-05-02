---
title: hook_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - hook_versions
  - cloudformation
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>hook_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hook_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Publishes new or first hook version to AWS CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudformation.hook_versions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type, here the HookVersion. This is used to uniquely identify a HookVersion resource</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.cloudformation.hook_versions
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>hook_versions</code> resource, the following permissions are required:

### Create
```json
cloudformation:DescribeType,
cloudformation:DescribeTypeRegistration,
cloudformation:RegisterType,
iam:PassRole,
s3:GetObject,
s3:ListBucket,
kms:Decrypt
```

### List
```json
cloudformation:ListTypes,
cloudformation:ListTypeVersions
```

