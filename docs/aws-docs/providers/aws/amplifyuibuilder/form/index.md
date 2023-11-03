---
title: form
hide_title: false
hide_table_of_contents: false
keywords:
  - form
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
Gets an individual <code>form</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>form</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.amplifyuibuilder.form</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AppId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Cta</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DataType</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>EnvironmentName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Fields</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>FormActionType</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SchemaVersion</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SectionalElements</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Style</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.amplifyuibuilder.form
WHERE region = 'us-east-1' AND data__Identifier = '{AppId}' AND data__Identifier = '{EnvironmentName}' AND data__Identifier = '{Id}'
```
