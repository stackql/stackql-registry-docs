---
title: knowledge_bases
hide_title: false
hide_table_of_contents: false
keywords:
  - knowledge_bases
  - wisdom
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>knowledge_bases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>knowledge_bases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>knowledge_bases</td></tr>
<tr><td><b>Id</b></td><td><code>aws.wisdom.knowledge_bases</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>KnowledgeBaseArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>KnowledgeBaseId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>KnowledgeBaseType</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RenderingConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ServerSideEncryptionConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>SourceConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.wisdom.knowledge_bases
WHERE region = 'us-east-1'
</pre>
