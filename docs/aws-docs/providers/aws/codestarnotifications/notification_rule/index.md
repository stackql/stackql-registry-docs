---
title: notification_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_rule
  - codestarnotifications
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>notification_rule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>notification_rule</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codestarnotifications.notification_rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>EventTypeId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CreatedBy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>TargetAddress</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EventTypeIds</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DetailType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Resource</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Targets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.codestarnotifications.notification_rule<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Arn&gt;'
</pre>
