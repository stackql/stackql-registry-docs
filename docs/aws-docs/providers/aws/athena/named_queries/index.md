---
title: named_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - named_queries
  - athena
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>named_queries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>named_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.athena.named_queries</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The query name.</td></tr><tr><td><code>Database</code></td><td><code>string</code></td><td>The database to which the query belongs.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>The query description.</td></tr><tr><td><code>QueryString</code></td><td><code>string</code></td><td>The contents of the query with all query statements.</td></tr><tr><td><code>WorkGroup</code></td><td><code>string</code></td><td>The name of the workgroup that contains the named query.</td></tr><tr><td><code>NamedQueryId</code></td><td><code>string</code></td><td>The unique ID of the query.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.athena.named_queries
WHERE region = 'us-east-1'
</pre>
