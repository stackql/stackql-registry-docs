---
title: ml_transform
hide_title: false
hide_table_of_contents: false
keywords:
  - ml_transform
  - glue
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>ml_transform</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ml_transform</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>ml_transform</td></tr>
<tr><td><b>Id</b></td><td><code>aws.glue.ml_transform</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>max_retries</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>transform_encryption</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>timeout</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>worker_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>glue_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>transform_parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>input_record_tables</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>number_of_workers</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>max_capacity</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
max_retries,
description,
transform_encryption,
timeout,
name,
role,
worker_type,
glue_version,
transform_parameters,
id,
input_record_tables,
number_of_workers,
tags,
max_capacity
FROM aws.glue.ml_transform
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
