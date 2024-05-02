---
title: aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - aliases
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
Retrieves a list of <code>aliases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::Alias resource creates an alias for an Amazon GameLift (GameLift) fleet destination.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.gamelift.aliases</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>alias_id</code></td><td><code>string</code></td><td>Unique alias ID</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
alias_id
FROM aws.gamelift.aliases
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>aliases</code> resource, the following permissions are required:

### Create
```json
gamelift:CreateAlias
```

### List
```json
gamelift:ListAliases
```

