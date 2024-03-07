---
title: data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources
  - datazone
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>data_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>data_sources</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datazone.data_sources</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain_id</code></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain where the data source is created.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The unique identifier of the data source.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>data_sources</code> resource, the following permissions are required:

### Create
<pre>
datazone:CreateDataSource,
iam:PassRole,
datazone:GetDataSource,
datazone:DeleteDataSource</pre>

### List
<pre>
datazone:ListDataSources</pre>


## Example
```sql
SELECT
region,
domain_id,
id
FROM awscc.datazone.data_sources
WHERE region = 'us-east-1'
```
