---
title: pipeline
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline
  - codepipeline
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>pipeline</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>pipeline</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codepipeline.pipeline</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>artifact_stores</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>artifact_store</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>disable_inbound_stage_transitions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>stages</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>restart_execution_on_update</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
artifact_stores,
version,
artifact_store,
disable_inbound_stage_transitions,
stages,
restart_execution_on_update,
id,
role_arn,
tags,
name
FROM aws.codepipeline.pipeline
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
