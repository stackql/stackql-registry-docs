---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
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
Gets an individual <code>application</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::ServiceCatalogAppRegistry::Application</td></tr>
<tr><td><b>Id</b></td><td><code>aws.servicecatalogappregistry.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the application. </td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the application. </td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>application_tag_key</code></td><td><code>string</code></td><td>The key of the AWS application tag, which is awsApplication. Applications created before 11&#x2F;13&#x2F;2023 or applications without the AWS application tag resource group return no value.</td></tr>
<tr><td><code>application_tag_value</code></td><td><code>string</code></td><td>The value of the AWS application tag, which is the identifier of an associated resource. Applications created before 11&#x2F;13&#x2F;2023 or applications without the AWS application tag resource group return no value. </td></tr>
<tr><td><code>application_name</code></td><td><code>string</code></td><td>The name of the application. </td></tr>
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
tags,
application_tag_key,
application_tag_value,
application_name
FROM aws.servicecatalogappregistry.application
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>application</code> resource, the following permissions are required:

### Read
```json
servicecatalog:GetApplication
```

### Update
```json
servicecatalog:GetApplication,
servicecatalog:ListTagsForResource,
servicecatalog:TagResource,
servicecatalog:UntagResource,
servicecatalog:UpdateApplication,
iam:CreateServiceLinkedRole
```

### Delete
```json
servicecatalog:DeleteApplication
```

