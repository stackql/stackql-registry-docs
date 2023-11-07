---
title: key_group
hide_title: false
hide_table_of_contents: false
keywords:
  - key_group
  - cloudfront
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>key_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>key_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudfront.key_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>KeyGroupConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>LastModifiedTime</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.cloudfront.key_group<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
