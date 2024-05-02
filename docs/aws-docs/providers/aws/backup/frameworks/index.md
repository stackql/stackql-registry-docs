---
title: frameworks
hide_title: false
hide_table_of_contents: false
keywords:
  - frameworks
  - backup
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>frameworks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>frameworks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains detailed information about a framework. Frameworks contain controls, which evaluate and report on your backup events and resources. Frameworks generate daily compliance results.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.backup.frameworks</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>framework_arn</code></td><td><code>string</code></td><td>An Amazon Resource Name (ARN) that uniquely identifies Framework as a resource</td></tr>
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
framework_arn
FROM aws.backup.frameworks
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>frameworks</code> resource, the following permissions are required:

### Create
```json
backup:CreateFramework,
backup:DescribeFramework,
backup:ListTags,
backup:TagResource,
iam:CreateServiceLinkedRole
```

### List
```json
backup:ListFrameworks
```

