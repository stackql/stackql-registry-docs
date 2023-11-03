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
<tr><td><b>Id</b></td><td><code>aws.batch.job_definition</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Parameters</code></td><td><code>object</code></td><td></td></tr><tr><td><code>Timeout</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>JobDefinitionName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PropagateTags</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>PlatformCapabilities</code></td><td><code>array</code></td><td></td></tr><tr><td><code>EksProperties</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Type</code></td><td><code>string</code></td><td></td></tr><tr><td><code>NodeProperties</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>SchedulingPriority</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>ContainerProperties</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RetryStrategy</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.batch.job_definition
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
```
