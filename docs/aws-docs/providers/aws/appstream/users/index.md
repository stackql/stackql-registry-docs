---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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
Retrieves a list of <code>users</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.appstream.users</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>UserName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>FirstName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MessageAction</code></td><td><code>string</code></td><td></td></tr><tr><td><code>LastName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AuthenticationType</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.appstream.users
WHERE region = 'us-east-1'
</pre>
