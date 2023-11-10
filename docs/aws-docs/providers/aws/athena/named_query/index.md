---
title: named_query
hide_title: false
hide_table_of_contents: false
keywords:
  - named_query
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
Gets an individual <code>named_query</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>named_query</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>named_query</td></tr>
<tr><td><b>Id</b></td><td><code>aws.athena.named_query</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The query name.</td></tr>
<tr><td><code>database</code></td><td><code>string</code></td><td>The database to which the query belongs.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The query description.</td></tr>
<tr><td><code>query_string</code></td><td><code>string</code></td><td>The contents of the query with all query statements.</td></tr>
<tr><td><code>work_group</code></td><td><code>string</code></td><td>The name of the workgroup that contains the named query.</td></tr>
<tr><td><code>named_query_id</code></td><td><code>string</code></td><td>The unique ID of the query.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
database,
description,
query_string,
work_group,
named_query_id
FROM aws.athena.named_query
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;NamedQueryId&gt;'
```
