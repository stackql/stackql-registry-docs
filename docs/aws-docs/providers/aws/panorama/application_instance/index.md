---
title: application_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - application_instance
  - panorama
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>application_instance</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>application_instance</td></tr>
<tr><td><b>Id</b></td><td><code>aws.panorama.application_instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>manifest_payload</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>manifest_overrides_payload</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>runtime_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_runtime_context_device</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_runtime_context_device_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_instance_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_instance_id_to_replace</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>device_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status_filter</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>health_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_time</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>last_updated_time</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
description,
manifest_payload,
manifest_overrides_payload,
runtime_role_arn,
default_runtime_context_device,
default_runtime_context_device_name,
application_instance_id,
application_instance_id_to_replace,
device_id,
status_filter,
status,
health_status,
status_description,
created_time,
last_updated_time,
arn,
tags
FROM aws.panorama.application_instance
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ApplicationInstanceId&gt;'
```
