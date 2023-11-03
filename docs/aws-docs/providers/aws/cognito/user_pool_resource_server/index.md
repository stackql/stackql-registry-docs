---
title: user_pool_resource_server
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_resource_server
  - cognito
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>user_pool_resource_server</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_resource_server</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.cognito.user_pool_resource_server</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>UserPoolId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Identifier</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Scopes</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.cognito.user_pool_resource_server
WHERE region = 'us-east-1' AND data__Identifier = '<Id>'
</pre>
