---
title: model
hide_title: false
hide_table_of_contents: false
keywords:
  - model
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>model</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>model</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.model</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>execution_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enable_network_isolation</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>primary_container</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>model_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpc_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>containers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>inference_execution_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
execution_role_arn,
enable_network_isolation,
primary_container,
model_name,
vpc_config,
containers,
inference_execution_config,
id,
tags
FROM aws.sagemaker.model
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
