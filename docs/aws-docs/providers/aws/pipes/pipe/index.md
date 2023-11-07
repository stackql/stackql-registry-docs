---
title: pipe
hide_title: false
hide_table_of_contents: false
keywords:
  - pipe
  - pipes
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>pipe</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipe</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.pipes.pipe</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CreationTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CurrentState</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DesiredState</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Enrichment</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EnrichmentParameters</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>LastModifiedTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Source</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SourceParameters</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>StateReason</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Target</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>TargetParameters</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.pipes.pipe
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Name&gt;'
</pre>
