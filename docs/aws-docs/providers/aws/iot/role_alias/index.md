---
title: role_alias
hide_title: false
hide_table_of_contents: false
keywords:
  - role_alias
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>role_alias</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.iot.role_alias</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>RoleAlias</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RoleAliasArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RoleArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CredentialDurationSeconds</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iot.role_alias
WHERE region = 'us-east-1' AND data__Identifier = '<RoleAlias>'
</pre>
