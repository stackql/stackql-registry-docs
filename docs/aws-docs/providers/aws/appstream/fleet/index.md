---
title: fleet
hide_title: false
hide_table_of_contents: false
keywords:
  - fleet
  - appstream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>fleet</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleet</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>fleet</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appstream.fleet</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>compute_capacity</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>platform</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpc_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>fleet_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enable_default_internet_access</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>domain_join_info</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>session_script_s3_location</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>image_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>max_user_duration_in_seconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>idle_disconnect_timeout_in_seconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>usb_device_filter_strings</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>disconnect_timeout_in_seconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stream_view</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>iam_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instance_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>max_concurrent_sessions</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>image_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
compute_capacity,
platform,
vpc_config,
fleet_type,
enable_default_internet_access,
domain_join_info,
session_script_s3_location,
name,
image_name,
max_user_duration_in_seconds,
idle_disconnect_timeout_in_seconds,
usb_device_filter_strings,
disconnect_timeout_in_seconds,
display_name,
stream_view,
iam_role_arn,
id,
instance_type,
max_concurrent_sessions,
tags,
image_arn
FROM aws.appstream.fleet
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
