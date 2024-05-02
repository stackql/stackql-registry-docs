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
Gets or operates on an individual <code>named_query</code> resource, use <code>named_queries</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>named_query</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Athena::NamedQuery</td></tr>
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

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
WHERE data__Identifier = '<NamedQueryId>';
```

## Permissions

To operate on the <code>named_query</code> resource, the following permissions are required:

### Read
```json
athena:GetNamedQuery
```

### Delete
```json
athena:DeleteNamedQuery
```

