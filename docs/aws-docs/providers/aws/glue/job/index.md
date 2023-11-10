---
title: job
hide_title: false
hide_table_of_contents: false
keywords:
  - job
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
Gets an individual <code>job</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>job</td></tr>
<tr><td><b>Id</b></td><td><code>aws.glue.job</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>connections</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>max_retries</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>timeout</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>allocated_capacity</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_arguments</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>notification_property</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>worker_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>execution_class</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>log_uri</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>command</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>glue_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>execution_property</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>security_configuration</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>number_of_workers</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>max_capacity</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>non_overridable_arguments</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
connections,
max_retries,
description,
timeout,
allocated_capacity,
name,
role,
default_arguments,
notification_property,
worker_type,
execution_class,
log_uri,
command,
glue_version,
execution_property,
security_configuration,
id,
number_of_workers,
tags,
max_capacity,
non_overridable_arguments
FROM aws.glue.job
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
