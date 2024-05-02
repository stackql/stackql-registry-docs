---
title: attribute_group
hide_title: false
hide_table_of_contents: false
keywords:
  - attribute_group
  - servicecatalogappregistry
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>attribute_group</code> resource, use <code>attribute_groups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attribute_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::ServiceCatalogAppRegistry::AttributeGroup.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.servicecatalogappregistry.attribute_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the attribute group. </td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the attribute group. </td></tr>
<tr><td><code>attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
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
id,
arn,
name,
description,
attributes,
tags
FROM aws.servicecatalogappregistry.attribute_group
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>attribute_group</code> resource, the following permissions are required:

### Read
```json
servicecatalog:GetAttributeGroup
```

### Update
```json
servicecatalog:GetAttributeGroup,
servicecatalog:UpdateAttributeGroup,
servicecatalog:ListTagsForResource,
servicecatalog:TagResource,
servicecatalog:UntagResource
```

### Delete
```json
servicecatalog:DeleteAttributeGroup
```

