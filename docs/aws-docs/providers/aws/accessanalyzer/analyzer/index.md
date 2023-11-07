---
title: analyzer
hide_title: false
hide_table_of_contents: false
keywords:
  - analyzer
  - accessanalyzer
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>analyzer</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analyzer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>analyzer</td></tr>
<tr><td><b>Id</b></td><td><code>aws.accessanalyzer.analyzer</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AnalyzerName</code></td><td><code>string</code></td><td>Analyzer name</td></tr>
<tr><td><code>ArchiveRules</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the analyzer</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td>The type of the analyzer, must be ACCOUNT or ORGANIZATION</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.accessanalyzer.analyzer<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Arn&gt;'
</pre>
