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
Gets an individual <code>data_catalog</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_catalog</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>data_catalog</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.athena.data_catalog</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the data catalog to create. The catalog name must be unique for the AWS account and can use a maximum of 128 alphanumeric, underscore, at sign, or hyphen characters. </td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the data catalog to be created. </td></tr>
<tr><td><code>parameters</code></td><td><code>object</code></td><td>Specifies the Lambda function or functions to use for creating the data catalog. This is a mapping whose values depend on the catalog type. </td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of comma separated tags to add to the data catalog that is created. </td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of data catalog to create: LAMBDA for a federated catalog, GLUE for AWS Glue Catalog, or HIVE for an external hive metastore. </td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>data_catalog</code> resource, the following permissions are required:

### Read
<pre>
athena:GetDataCatalog,
athena:ListTagsForResource</pre>

### Update
<pre>
athena:UpdateDataCatalog,
athena:TagResource,
athena:GetDataCatalog,
athena:UntagResource,
athena:ListTagsForResource</pre>

### Delete
<pre>
athena:DeleteDataCatalog</pre>


## Example
```sql
SELECT
region,
name,
description,
parameters,
tags,
type
FROM awscc.athena.data_catalog
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Name&gt;'
```
