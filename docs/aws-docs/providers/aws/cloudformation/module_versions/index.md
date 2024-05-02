---
title: module_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - module_versions
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
Retrieves a list of <code>module_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>module_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A module that has been registered in the CloudFormation registry.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudformation.module_versions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the module.</td></tr>
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
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.cloudformation.module_versions
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>module_versions</code> resource, the following permissions are required:

### Create
```json
cloudformation:DescribeType,
cloudformation:DescribeTypeRegistration,
cloudformation:ListTypeVersions,
cloudformation:RegisterType,
s3:GetObject,
s3:ListBucket
```

