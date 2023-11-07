---
title: email_channel
hide_title: false
hide_table_of_contents: false
keywords:
  - email_channel
  - pinpoint
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>email_channel</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>email_channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>email_channel</td></tr>
<tr><td><b>Id</b></td><td><code>aws.pinpoint.email_channel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ConfigurationSet</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>FromAddress</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>ApplicationId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Identity</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.pinpoint.email_channel<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
