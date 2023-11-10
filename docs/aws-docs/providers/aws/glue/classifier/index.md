---
title: classifier
hide_title: false
hide_table_of_contents: false
keywords:
  - classifier
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
Gets an individual <code>classifier</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>classifier</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>classifier</td></tr>
<tr><td><b>Id</b></td><td><code>aws.glue.classifier</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>x_ml_classifier</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>json_classifier</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>csv_classifier</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>grok_classifier</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
x_ml_classifier,
json_classifier,
csv_classifier,
grok_classifier
FROM aws.glue.classifier
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
