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
<tr><td><b>Description</b></td><td>named_queries</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.athena.named_queries</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>named_query_id</code></td><td><code>string</code></td><td>The unique ID of the query.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
named_query_id
FROM awscc.athena.named_queries
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>named_queries</code> resource, the following permissions are required:

### Create
```json
athena:CreateNamedQuery
```

### List
```json
athena:ListNamedQueries
```

