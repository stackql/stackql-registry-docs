---
title: dataset
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset
  - databrew
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>dataset</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.databrew.dataset</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Dataset name</td></tr><tr><td><code>Format</code></td><td><code>string</code></td><td>Dataset format</td></tr><tr><td><code>FormatOptions</code></td><td><code>undefined</code></td><td>Format options for dataset</td></tr><tr><td><code>Input</code></td><td><code>undefined</code></td><td>Input</td></tr><tr><td><code>PathOptions</code></td><td><code>undefined</code></td><td>PathOptions</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.databrew.dataset
WHERE region = 'us-east-1' AND data__Identifier = '{Name}'
</pre>
