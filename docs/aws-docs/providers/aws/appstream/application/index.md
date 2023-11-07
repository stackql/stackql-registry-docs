---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
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
Gets an individual <code>application</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>application</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appstream.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DisplayName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LaunchPath</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LaunchParameters</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>WorkingDirectory</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>InstanceFamilies</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>IconS3Location</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AppBlockArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Platforms</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>AttributesToDelete</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>CreatedTime</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.appstream.application<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Arn&gt;'
</pre>
