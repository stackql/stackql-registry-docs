---
title: cloud_formation_provisioned_product
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_formation_provisioned_product
  - servicecatalog
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

Gets or operates on an individual <code>cloud_formation_provisioned_product</code> resource, use <code>cloud_formation_provisioned_products</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_formation_provisioned_product</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::ServiceCatalog::CloudFormationProvisionedProduct</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.servicecatalog.cloud_formation_provisioned_product" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="accept_language" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="notification_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="path_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="path_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="product_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="product_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioned_product_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioning_artifact_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioning_artifact_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioning_parameters" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioning_preferences" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioned_product_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="record_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="cloudformation_stack_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="outputs" /></td><td><code>object</code></td><td>List of key-value pair outputs.</td></tr>
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
accept_language,
notification_arns,
path_id,
path_name,
product_id,
product_name,
provisioned_product_name,
provisioning_artifact_id,
provisioning_artifact_name,
provisioning_parameters,
provisioning_preferences,
tags,
provisioned_product_id,
record_id,
cloudformation_stack_arn,
outputs
FROM aws.servicecatalog.cloud_formation_provisioned_product
WHERE data__Identifier = '<ProvisionedProductId>';
```

## Permissions

To operate on the <code>cloud_formation_provisioned_product</code> resource, the following permissions are required:

### Read
```json
*
```

### Update
```json
*
```

### Delete
```json
*
```

