---
title: data_catalog_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - data_catalog_tags
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

Expands all tag keys and values for <code>data_catalogs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_catalog_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Athena::DataCatalog</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.athena.data_catalog_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the data catalog to create. The catalog name must be unique for the AWS account and can use a maximum of 128 alphanumeric, underscore, at sign, or hyphen characters.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the data catalog to be created.</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>Specifies the Lambda function or functions to use for creating the data catalog. This is a mapping whose values depend on the catalog type.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of data catalog to create: LAMBDA for a federated catalog, GLUE for AWS Glue Catalog, or HIVE for an external hive metastore.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>data_catalogs</code> in a region.
```sql
SELECT
region,
name,
description,
parameters,
type,
tag_key,
tag_value
FROM aws.athena.data_catalog_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>data_catalog_tags</code> resource, see <a href="/providers/aws/athena/data_catalogs/#permissions"><code>data_catalogs</code></a>

