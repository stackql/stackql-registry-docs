---
title: data_catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - data_catalogs
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
Retrieves a list of <code>data_catalogs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.athena.data_catalogs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the data catalog to create. The catalog name must be unique for the AWS account and can use a maximum of 128 alphanumeric, underscore, at sign, or hyphen characters. </td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>A description of the data catalog to be created. </td></tr><tr><td><code>Parameters</code></td><td><code>object</code></td><td>Specifies the Lambda function or functions to use for creating the data catalog. This is a mapping whose values depend on the catalog type. </td></tr><tr><td><code>Tags</code></td><td><code>undefined</code></td><td>A list of comma separated tags to add to the data catalog that is created. </td></tr><tr><td><code>Type</code></td><td><code>string</code></td><td>The type of data catalog to create: LAMBDA for a federated catalog, GLUE for AWS Glue Catalog, or HIVE for an external hive metastore. </td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.athena.data_catalogs
WHERE region = 'us-east-1'
</pre>
