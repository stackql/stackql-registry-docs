---
title: app
hide_title: false
hide_table_of_contents: false
keywords:
  - app
  - opsworks
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>app</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>app</td></tr>
<tr><td><b>Id</b></td><td><code>aws.opsworks.app</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>app_source</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>data_sources</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domains</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>enable_ssl</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>environment</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>shortname</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ssl_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>stack_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
app_source,
attributes,
data_sources,
description,
domains,
enable_ssl,
environment,
name,
shortname,
ssl_configuration,
stack_id,
type
FROM aws.opsworks.app
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
