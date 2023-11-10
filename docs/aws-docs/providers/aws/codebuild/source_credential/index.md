---
title: source_credential
hide_title: false
hide_table_of_contents: false
keywords:
  - source_credential
  - codebuild
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>source_credential</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_credential</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>source_credential</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codebuild.source_credential</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>server_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>token</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>auth_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>username</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
server_type,
token,
auth_type,
id,
username
FROM aws.codebuild.source_credential
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
