---
title: account_alias
hide_title: false
hide_table_of_contents: false
keywords:
  - account_alias
  - supportapp
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>account_alias</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>account_alias</td></tr>
<tr><td><b>Id</b></td><td><code>aws.supportapp.account_alias</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>account_alias</code></td><td><code>string</code></td><td>An account alias associated with a customer's account.</td></tr>
<tr><td><code>account_alias_resource_id</code></td><td><code>string</code></td><td>Unique identifier representing an alias tied to an account</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
account_alias,
account_alias_resource_id
FROM aws.supportapp.account_alias
WHERE region = 'us-east-1'
AND data__Identifier = '<AccountAliasResourceId>'
```
