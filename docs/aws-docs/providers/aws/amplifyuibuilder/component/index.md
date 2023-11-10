---
title: component
hide_title: false
hide_table_of_contents: false
keywords:
  - component
  - amplifyuibuilder
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>component</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>component</td></tr>
<tr><td><b>Id</b></td><td><code>aws.amplifyuibuilder.component</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>app_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>binding_properties</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>children</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>collection_properties</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>component_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>environment_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>events</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>overrides</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>properties</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>schema_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>variants</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
app_id,
binding_properties,
children,
collection_properties,
component_type,
environment_name,
events,
id,
name,
overrides,
properties,
schema_version,
source_id,
tags,
variants
FROM aws.amplifyuibuilder.component
WHERE region = 'us-east-1'
AND data__Identifier = '<AppId>'
AND data__Identifier = '<EnvironmentName>'
AND data__Identifier = '<Id>'
```
