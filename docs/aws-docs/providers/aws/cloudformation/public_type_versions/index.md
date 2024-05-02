---
title: public_type_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - public_type_versions
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
Retrieves a list of <code>public_type_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_type_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Test and Publish a resource that has been registered in the CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudformation.public_type_versions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>public_type_arn</code></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) assigned to the public extension upon publication</td></tr>
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
public_type_arn
FROM aws.cloudformation.public_type_versions
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>public_type_versions</code> resource, the following permissions are required:

### Create
```json
cloudformation:TestType,
cloudformation:DescribeType,
cloudformation:PublishType,
cloudformation:DescribePublisher,
s3:GetObject,
s3:PutObject
```

### List
```json
cloudformation:ListTypes
```

