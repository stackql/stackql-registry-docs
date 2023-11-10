---
title: image_builder
hide_title: false
hide_table_of_contents: false
keywords:
  - image_builder
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
Gets an individual <code>image_builder</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_builder</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>image_builder</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appstream.image_builder</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpc_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>enable_default_internet_access</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>domain_join_info</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>appstream_agent_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>image_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>iam_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instance_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>streaming_url</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>image_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>access_endpoints</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
vpc_config,
enable_default_internet_access,
domain_join_info,
appstream_agent_version,
name,
image_name,
display_name,
iam_role_arn,
instance_type,
tags,
streaming_url,
image_arn,
access_endpoints
FROM aws.appstream.image_builder
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Name&gt;'
```
