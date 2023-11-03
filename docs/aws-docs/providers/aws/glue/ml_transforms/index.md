---
title: ml_transforms
hide_title: false
hide_table_of_contents: false
keywords:
  - ml_transforms
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
Retrieves a list of <code>ml_transforms</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ml_transforms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.glue.ml_transforms</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>MaxRetries</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TransformEncryption</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Timeout</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Role</code></td><td><code>string</code></td><td></td></tr><tr><td><code>WorkerType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>GlueVersion</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TransformParameters</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>InputRecordTables</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>NumberOfWorkers</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr><tr><td><code>MaxCapacity</code></td><td><code>number</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.glue.ml_transforms
WHERE region = 'us-east-1'
</pre>
