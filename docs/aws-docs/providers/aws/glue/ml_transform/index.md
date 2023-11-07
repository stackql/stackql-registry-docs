---
title: ml_transform
hide_title: false
hide_table_of_contents: false
keywords:
  - ml_transform
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
Gets an individual <code>ml_transform</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ml_transform</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>ml_transform</td></tr>
<tr><td><b>Id</b></td><td><code>aws.glue.ml_transform</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>MaxRetries</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>TransformEncryption</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Timeout</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>WorkerType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>GlueVersion</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>TransformParameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>InputRecordTables</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>NumberOfWorkers</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>MaxCapacity</code></td><td><code>number</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.glue.ml_transform<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
