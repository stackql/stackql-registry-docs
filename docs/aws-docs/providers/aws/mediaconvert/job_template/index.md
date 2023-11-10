---
title: job_template
hide_title: false
hide_table_of_contents: false
keywords:
  - job_template
  - mediaconvert
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>job_template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>job_template</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediaconvert.job_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>category</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>acceleration_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>priority</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>status_update_interval</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>settings_json</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>queue</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>hop_destinations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
category,
description,
acceleration_settings,
priority,
status_update_interval,
settings_json,
id,
arn,
queue,
hop_destinations,
tags,
name
FROM aws.mediaconvert.job_template
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
