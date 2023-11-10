---
title: branch
hide_title: false
hide_table_of_contents: false
keywords:
  - branch
  - amplify
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>branch</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>branch</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>branch</td></tr>
<tr><td><b>Id</b></td><td><code>aws.amplify.branch</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>app_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>basic_auth_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>branch_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>build_spec</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enable_auto_build</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>enable_performance_mode</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>enable_pull_request_preview</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>environment_variables</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>framework</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>pull_request_environment_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stage</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
app_id,
arn,
basic_auth_config,
branch_name,
build_spec,
description,
enable_auto_build,
enable_performance_mode,
enable_pull_request_preview,
environment_variables,
framework,
pull_request_environment_name,
stage,
tags
FROM aws.amplify.branch
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
