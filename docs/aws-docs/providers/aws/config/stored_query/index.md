---
title: stored_query
hide_title: false
hide_table_of_contents: false
keywords:
  - stored_query
  - config
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>stored_query</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stored_query</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.config.stored_query</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>QueryArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>QueryId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>QueryName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>QueryDescription</code></td><td><code>string</code></td><td></td></tr><tr><td><code>QueryExpression</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags for the stored query.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.config.stored_query
WHERE region = 'us-east-1' AND data__Identifier = '{QueryName}'
</pre>
