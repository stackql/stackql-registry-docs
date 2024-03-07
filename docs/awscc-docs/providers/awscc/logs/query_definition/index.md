---
title: query_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - query_definition
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
Gets an individual <code>query_definition</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>query_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>query_definition</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.logs.query_definition</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A name for the saved query definition</td></tr>
<tr><td><code>query_string</code></td><td><code>string</code></td><td>The query string to use for this definition</td></tr>
<tr><td><code>log_group_names</code></td><td><code>array</code></td><td>Optionally define specific log groups as part of your query definition</td></tr>
<tr><td><code>query_definition_id</code></td><td><code>string</code></td><td>Unique identifier of a query definition</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>query_definition</code> resource, the following permissions are required:

### Read
<pre>
logs:DescribeQueryDefinitions</pre>

### Update
<pre>
logs:PutQueryDefinition</pre>

### Delete
<pre>
logs:DeleteQueryDefinition</pre>


## Example
```sql
SELECT
region,
name,
query_string,
log_group_names,
query_definition_id
FROM awscc.logs.query_definition
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;QueryDefinitionId&gt;'
```
