---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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
Retrieves a list of <code>jobs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.glue.jobs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Connections</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>MaxRetries</code></td><td><code>number</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Timeout</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>AllocatedCapacity</code></td><td><code>number</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Role</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DefaultArguments</code></td><td><code>object</code></td><td></td></tr><tr><td><code>NotificationProperty</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>WorkerType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ExecutionClass</code></td><td><code>string</code></td><td></td></tr><tr><td><code>LogUri</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Command</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>GlueVersion</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ExecutionProperty</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>SecurityConfiguration</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>NumberOfWorkers</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr><tr><td><code>MaxCapacity</code></td><td><code>number</code></td><td></td></tr><tr><td><code>NonOverridableArguments</code></td><td><code>object</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.glue.jobs
WHERE region = 'us-east-1'
```
