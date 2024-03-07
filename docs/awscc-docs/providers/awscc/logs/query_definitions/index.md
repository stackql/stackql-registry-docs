---
title: query_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - query_definitions
  - logs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>query_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>query_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>query_definitions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.logs.query_definitions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>query_definition_id</code></td><td><code>string</code></td><td>Unique identifier of a query definition</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>query_definitions</code> resource, the following permissions are required:

### Create
<pre>
logs:PutQueryDefinition</pre>

### List
<pre>
logs:DescribeQueryDefinitions</pre>


## Example
```sql
SELECT
region,
query_definition_id
FROM awscc.logs.query_definitions
WHERE region = 'us-east-1'
```
