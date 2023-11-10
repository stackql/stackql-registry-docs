---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
  - kinesisanalytics
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>application</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>application</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kinesisanalytics.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>inputs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>application_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_code</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
application_name,
inputs,
application_description,
application_code
FROM aws.kinesisanalytics.application
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
