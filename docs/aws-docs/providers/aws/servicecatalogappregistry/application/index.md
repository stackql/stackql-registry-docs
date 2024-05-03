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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>application</code> resource, use <code>applications</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::ServiceCatalogAppRegistry::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.servicecatalogappregistry.application" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the application. </td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the application. </td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="application_tag_key" /></td><td><code>string</code></td><td>The key of the AWS application tag, which is awsApplication. Applications created before 11&#x2F;13&#x2F;2023 or applications without the AWS application tag resource group return no value.</td></tr>
<tr><td><CopyableCode code="application_tag_value" /></td><td><code>string</code></td><td>The value of the AWS application tag, which is the identifier of an associated resource. Applications created before 11&#x2F;13&#x2F;2023 or applications without the AWS application tag resource group return no value. </td></tr>
<tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>The name of the application. </td></tr>
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

