---
title: job_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - job_definition
  - batch
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>job_definition</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>job_definition</td></tr>
<tr><td><b>Id</b></td><td><code>aws.batch.job_definition</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>timeout</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>job_definition_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>propagate_tags</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>platform_capabilities</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>eks_properties</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>node_properties</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>scheduling_priority</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>container_properties</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>retry_strategy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
parameters,
timeout,
job_definition_name,
propagate_tags,
platform_capabilities,
eks_properties,
type,
node_properties,
scheduling_priority,
container_properties,
id,
retry_strategy,
tags
FROM aws.batch.job_definition
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
