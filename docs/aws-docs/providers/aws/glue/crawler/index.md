---
title: crawler
hide_title: false
hide_table_of_contents: false
keywords:
  - crawler
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
Gets an individual <code>crawler</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crawler</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>crawler</td></tr>
<tr><td><b>Id</b></td><td><code>aws.glue.crawler</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>classifiers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schema_change_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>configuration</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>recrawl_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>database_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>targets</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>crawler_security_configuration</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schedule</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>table_prefix</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
classifiers,
description,
schema_change_policy,
configuration,
recrawl_policy,
database_name,
targets,
crawler_security_configuration,
name,
role,
schedule,
id,
table_prefix,
tags
FROM aws.glue.crawler
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
