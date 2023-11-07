---
title: variant_store
hide_title: false
hide_table_of_contents: false
keywords:
  - variant_store
  - omics
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>variant_store</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>variant_store</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.omics.variant_store</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CreationTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Reference</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>SseConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Status</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>StatusMessage</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StoreArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StoreSizeBytes</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>UpdateTime</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.omics.variant_store
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Name&gt;'
</pre>
