---
title: connection_alias
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_alias
  - workspaces
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>connection_alias</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection_alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>connection_alias</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.workspaces.connection_alias</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>associations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>alias_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>connection_string</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>connection_alias_state</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>connection_alias</code> resource, the following permissions are required:

### Read
<pre>
workspaces:DescribeConnectionAliases</pre>

### Delete
<pre>
workspaces:DeleteConnectionAlias</pre>


## Example
```sql
SELECT
region,
associations,
alias_id,
connection_string,
connection_alias_state,
tags
FROM awscc.workspaces.connection_alias
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AliasId&gt;'
```
