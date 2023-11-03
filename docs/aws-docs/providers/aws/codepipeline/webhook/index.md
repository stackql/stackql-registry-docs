---
title: webhook
hide_title: false
hide_table_of_contents: false
keywords:
  - webhook
  - codepipeline
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>webhook</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webhook</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codepipeline.webhook</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AuthenticationConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Filters</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Authentication</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TargetPipeline</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TargetAction</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Url</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TargetPipelineVersion</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>RegisterWithThirdParty</code></td><td><code>boolean</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.codepipeline.webhook
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
</pre>
