---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - memorydb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>users</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>users</td></tr>
<tr><td><b>Id</b></td><td><code>aws.memorydb.users</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td>Indicates the user status. Can be "active", "modifying" or "deleting".</td></tr>
<tr><td><code>UserName</code></td><td><code>string</code></td><td>The name of the user.</td></tr>
<tr><td><code>AccessString</code></td><td><code>string</code></td><td>Access permissions string used for this user account.</td></tr>
<tr><td><code>AuthenticationMode</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the user account.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this user.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.memorydb.users
WHERE region = 'us-east-1'
</pre>
