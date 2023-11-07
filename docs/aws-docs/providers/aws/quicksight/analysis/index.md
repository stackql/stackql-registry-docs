---
title: analysis
hide_title: false
hide_table_of_contents: false
keywords:
  - analysis
  - quicksight
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>analysis</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analysis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>analysis</td></tr>
<tr><td><b>Id</b></td><td><code>aws.quicksight.analysis</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AnalysisId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AwsAccountId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CreatedTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DataSetArns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Definition</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Errors</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>LastUpdatedTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Parameters</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Permissions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Sheets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>SourceEntity</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Status</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ThemeArn</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.quicksight.analysis
WHERE region = 'us-east-1' AND data__Identifier = '&lt;AnalysisId&gt;' AND data__Identifier = '&lt;AwsAccountId&gt;'
</pre>
