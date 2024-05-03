---
title: function
hide_title: false
hide_table_of_contents: false
keywords:
  - function
  - cloudfront
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>function</code> resource, use <code>functions</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>function</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CloudFront::Function</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.function" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="auto_publish" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="function_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="function_code" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="function_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="function_metadata" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stage" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
auto_publish,
function_arn,
function_code,
function_config,
function_metadata,
name,
stage
FROM aws.cloudfront.function
WHERE data__Identifier = '<FunctionARN>';
```

## Permissions

To operate on the <code>function</code> resource, the following permissions are required:

### Delete
```json
cloudfront:DeleteFunction,
cloudfront:DescribeFunction
```

### Read
```json
cloudfront:DescribeFunction,
cloudfront:GetFunction
```

### Update
```json
cloudfront:UpdateFunction,
cloudfront:PublishFunction,
cloudfront:DescribeFunction
```

