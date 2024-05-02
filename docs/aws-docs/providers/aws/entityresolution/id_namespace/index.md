---
title: id_namespace
hide_title: false
hide_table_of_contents: false
keywords:
  - id_namespace
  - entityresolution
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>id_namespace</code> resource, use <code>id_namespaces</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>id_namespace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>IdNamespace defined in AWS Entity Resolution service</td></tr>
<tr><td><b>Id</b></td><td><code>aws.entityresolution.id_namespace</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id_namespace_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>input_source_config</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id_mapping_workflow_properties</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id_namespace_arn</code></td><td><code>string</code></td><td>The arn associated with the IdNamespace</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The date and time when the IdNamespace was created</td></tr>
<tr><td><code>updated_at</code></td><td><code>string</code></td><td>The date and time when the IdNamespace was updated</td></tr>
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
id_namespace_name,
description,
input_source_config,
id_mapping_workflow_properties,
type,
role_arn,
id_namespace_arn,
created_at,
updated_at,
tags
FROM aws.entityresolution.id_namespace
WHERE data__Identifier = '<IdNamespaceName>';
```

## Permissions

To operate on the <code>id_namespace</code> resource, the following permissions are required:

### Read
```json
entityresolution:GetIdNamespace,
entityresolution:ListTagsForResource
```

### Update
```json
entityresolution:UpdateIdNamespace,
entityresolution:ListTagsForResource,
entityresolution:TagResource,
entityresolution:UntagResource,
iam:PassRole
```

### Delete
```json
entityresolution:DeleteIdNamespace,
entityresolution:GetIdNamespace,
entityresolution:UntagResource
```

