---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
  - transfer
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>user</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.transfer.user</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Policy</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Role</code></td><td><code>string</code></td><td></td></tr><tr><td><code>HomeDirectory</code></td><td><code>string</code></td><td></td></tr><tr><td><code>HomeDirectoryType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ServerId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>UserName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>HomeDirectoryMappings</code></td><td><code>array</code></td><td></td></tr><tr><td><code>PosixProfile</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>SshPublicKeys</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.transfer.user
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
```
