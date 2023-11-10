---
title: step
hide_title: false
hide_table_of_contents: false
keywords:
  - step
  - emr
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>step</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>step</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>step</td></tr>
<tr><td><b>Id</b></td><td><code>aws.emr.step</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>action_on_failure</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>hadoop_jar_step</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>job_flow_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
action_on_failure,
hadoop_jar_step,
job_flow_id,
name
FROM aws.emr.step
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
