---
title: module_default_version
hide_title: false
hide_table_of_contents: false
keywords:
  - module_default_version
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
Gets or operates on an individual <code>module_default_version</code> resource, use <code>module_default_versions</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>module_default_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A module that has been registered in the CloudFormation registry as the default version</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudformation.module_default_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the module version to set as the default version.</td></tr>
<tr><td><code>module_name</code></td><td><code>string</code></td><td>The name of a module existing in the registry.</td></tr>
<tr><td><code>version_id</code></td><td><code>string</code></td><td>The ID of an existing version of the named module to set as the default.</td></tr>
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
module_name,
version_id
FROM aws.cloudformation.module_default_version
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>module_default_version</code> resource, the following permissions are required:

### Read
```json
cloudformation:DescribeType
```

