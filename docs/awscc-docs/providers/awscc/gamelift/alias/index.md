---
title: alias
hide_title: false
hide_table_of_contents: false
keywords:
  - alias
  - gamelift
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>alias</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>alias</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.gamelift.alias</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A human-readable description of the alias.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A descriptive label that is associated with an alias. Alias names do not need to be unique.</td></tr>
<tr><td><code>routing_strategy</code></td><td><code>object</code></td><td>A routing configuration that specifies where traffic is directed for this alias, such as to a fleet or to a message.</td></tr>
<tr><td><code>alias_id</code></td><td><code>string</code></td><td>Unique alias ID</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
name,
routing_strategy,
alias_id
FROM awscc.gamelift.alias
WHERE data__Identifier = '<AliasId>';
```

## Permissions

To operate on the <code>alias</code> resource, the following permissions are required:

### Read
```json
gamelift:DescribeAlias
```

### Update
```json
gamelift:UpdateAlias
```

### Delete
```json
gamelift:DeleteAlias
```

