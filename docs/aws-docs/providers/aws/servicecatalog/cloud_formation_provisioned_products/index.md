---
title: cloud_formation_provisioned_products
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_formation_provisioned_products
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

Used to retrieve a list of <code>cloud_formation_provisioned_products</code> in a region or create a <code>cloud_formation_provisioned_products</code> resource, use <code>cloud_formation_provisioned_product</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_formation_provisioned_products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::ServiceCatalog::CloudFormationProvisionedProduct</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.servicecatalog.cloud_formation_provisioned_products" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="provisioned_product_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
provisioned_product_id
FROM aws.servicecatalog.cloud_formation_provisioned_products
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>cloud_formation_provisioned_products</code> resource, the following permissions are required:

### Create
```json
*
```

