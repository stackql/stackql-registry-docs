---
title: flywheel
hide_title: false
hide_table_of_contents: false
keywords:
  - flywheel
  - comprehend
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>flywheel</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flywheel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>flywheel</td></tr>
<tr><td><b>Id</b></td><td><code>aws.comprehend.flywheel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ActiveModelArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DataAccessRoleArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DataLakeS3Uri</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DataSecurityConfig</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>FlywheelName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ModelType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>TaskConfig</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.comprehend.flywheel<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Arn&gt;'
</pre>
