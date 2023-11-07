---
title: reference_store
hide_title: false
hide_table_of_contents: false
keywords:
  - reference_store
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
Gets an individual <code>reference_store</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reference_store</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>reference_store</td></tr>
<tr><td><b>Id</b></td><td><code>aws.omics.reference_store</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The store's ARN.</td></tr>
<tr><td><code>CreationTime</code></td><td><code>string</code></td><td>When the store was created.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>A description for the store.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>A name for the store.</td></tr>
<tr><td><code>ReferenceStoreId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SseConfig</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.omics.reference_store<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;ReferenceStoreId&gt;'
</pre>
