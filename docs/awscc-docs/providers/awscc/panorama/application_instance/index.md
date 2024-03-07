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
<tr><td><b>Id</b></td><td><code>awscc.panorama.application_instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>default_runtime_context_device_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_runtime_context_device</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_instance_id_to_replace</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_time</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>health_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>manifest_overrides_payload</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>last_updated_time</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>runtime_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_instance_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>manifest_payload</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>application_instance</code> resource, the following permissions are required:

### Read
```json
panorama:DescribeApplicationInstance,
panorama:DescribeApplicationInstanceDetails,
panorama:ListTagsForResource,
s3:ListObjects,
s3:GetObject,
s3:GetObjectVersion
```

### Update
```json
panorama:ListTagsForResource,
panorama:TagResource,
panorama:UntagResource,
panorama:DescribeApplicationInstance,
panorama:DescribeApplicationInstanceDetails,
s3:ListObjects,
s3:GetObject,
s3:GetObjectVersion
```

### Delete
```json
panorama:RemoveApplicationInstance,
panorama:DescribeApplicationInstance,
panorama:DescribeApplicationInstanceDetails,
s3:DeleteObject,
s3:DeleteObjectVersion,
s3:DeleteObjectVersionTagging,
s3:ListObjects,
s3:GetObject,
s3:GetObjectVersion
```


## Example
```sql
SELECT
region,
default_runtime_context_device_name,
status,
default_runtime_context_device,
description,
application_instance_id_to_replace,
created_time,
health_status,
manifest_overrides_payload,
last_updated_time,
runtime_role_arn,
name,
application_instance_id,
status_description,
manifest_payload,
arn,
tags
FROM awscc.panorama.application_instance
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ApplicationInstanceId&gt;'
```
