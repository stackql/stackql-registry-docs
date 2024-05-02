---
title: resource_default_version
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_default_version
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
Gets an individual <code>resource_default_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_default_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The default version of a resource that has been registered in the CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudformation.resource_default_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>version_id</code></td><td><code>string</code></td><td>The ID of an existing version of the resource to set as the default.</td></tr>
<tr><td><code>type_name</code></td><td><code>string</code></td><td>The name of the type being registered.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type. This is used to uniquely identify a ResourceDefaultVersion</td></tr>
<tr><td><code>type_version_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type version.</td></tr>
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
version_id,
type_name,
arn,
type_version_arn
FROM aws.cloudformation.resource_default_version
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>resource_default_version</code> resource, the following permissions are required:

### Read
```json
cloudformation:DescribeType
```

### Update
```json
cloudformation:SetTypeDefaultVersion
```

### Delete
```json

```

