---
title: run_group
hide_title: false
hide_table_of_contents: false
keywords:
  - run_group
  - omics
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>run_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>run_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>run_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.omics.run_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>max_cpus</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>max_duration</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>max_runs</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
creation_time,
id,
max_cpus,
max_duration,
max_runs,
name,
tags
FROM aws.omics.run_group
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
