---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
  - appstream
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
<tr><td><b>Id</b></td><td><code>aws.appstream.user</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>UserName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>FirstName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MessageAction</code></td><td><code>string</code></td><td></td></tr><tr><td><code>LastName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AuthenticationType</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.appstream.user
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
```
