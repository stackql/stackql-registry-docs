---
title: data_catalog
hide_title: false
hide_table_of_contents: false
keywords:
  - data_catalog
  - athena
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>data_catalog</code> resource, use <code>data_catalogs</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_catalog</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Athena::DataCatalog</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.athena.data_catalog" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the data catalog to create. The catalog name must be unique for the AWS account and can use a maximum of 128 alphanumeric, underscore, at sign, or hyphen characters. </td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the data catalog to be created. </td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>Specifies the Lambda function or functions to use for creating the data catalog. This is a mapping whose values depend on the catalog type. </td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of comma separated tags to add to the data catalog that is created. </td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of data catalog to create: LAMBDA for a federated catalog, GLUE for AWS Glue Catalog, or HIVE for an external hive metastore. </td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name,
description,
parameters,
tags,
type
FROM aws.athena.data_catalog
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## Permissions

To operate on the <code>data_catalog</code> resource, the following permissions are required:

### Read
```json
athena:GetDataCatalog,
athena:ListTagsForResource
```

### Update
```json
athena:UpdateDataCatalog,
athena:TagResource,
athena:GetDataCatalog,
athena:UntagResource,
athena:ListTagsForResource
```

