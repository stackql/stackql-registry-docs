---
title: webhook
hide_title: false
hide_table_of_contents: false
keywords:
  - webhook
  - codepipeline
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>webhook</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webhook</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>webhook</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codepipeline.webhook</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>authentication_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>filters</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>authentication</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>target_pipeline</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>target_action</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>url</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>target_pipeline_version</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>register_with_third_party</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
authentication_configuration,
filters,
authentication,
target_pipeline,
target_action,
id,
url,
name,
target_pipeline_version,
register_with_third_party
FROM aws.codepipeline.webhook
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
