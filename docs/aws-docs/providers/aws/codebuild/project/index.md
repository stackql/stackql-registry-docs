---
title: project
hide_title: false
hide_table_of_contents: false
keywords:
  - project
  - codebuild
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>project</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>project</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codebuild.project</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_access_role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpc_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>secondary_sources</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>encryption_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>secondary_artifacts</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>source</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>logs_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>service_role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>queued_timeout_in_minutes</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>secondary_source_versions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>source_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>triggers</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>artifacts</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>badge_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>file_system_locations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>environment</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>concurrent_build_limit</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>visibility</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>build_batch_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>timeout_in_minutes</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>cache</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
resource_access_role,
vpc_config,
secondary_sources,
encryption_key,
secondary_artifacts,
source,
name,
logs_config,
service_role,
queued_timeout_in_minutes,
secondary_source_versions,
tags,
source_version,
triggers,
artifacts,
badge_enabled,
file_system_locations,
environment,
concurrent_build_limit,
visibility,
id,
arn,
build_batch_config,
timeout_in_minutes,
cache
FROM aws.codebuild.project
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
