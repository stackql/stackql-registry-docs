---
title: connection_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_aliases
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
Retrieves a list of <code>connection_aliases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.workspaces.connection_aliases</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Associations</code></td><td><code>array</code></td><td></td></tr><tr><td><code>AliasId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ConnectionString</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ConnectionAliasState</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.workspaces.connection_aliases
WHERE region = 'us-east-1'
```
