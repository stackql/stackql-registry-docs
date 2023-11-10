---
title: dev_endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_endpoint
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
Gets an individual <code>dev_endpoint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dev_endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>dev_endpoint</td></tr>
<tr><td><b>Id</b></td><td><code>aws.glue.dev_endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>extra_jars_s3_path</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>public_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>number_of_nodes</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>arguments</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>public_keys</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>worker_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>endpoint_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>glue_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>extra_python_libs_s3_path</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>security_configuration</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>number_of_workers</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
extra_jars_s3_path,
public_key,
number_of_nodes,
arguments,
subnet_id,
public_keys,
security_group_ids,
role_arn,
worker_type,
endpoint_name,
glue_version,
extra_python_libs_s3_path,
security_configuration,
id,
number_of_workers,
tags
FROM aws.glue.dev_endpoint
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
