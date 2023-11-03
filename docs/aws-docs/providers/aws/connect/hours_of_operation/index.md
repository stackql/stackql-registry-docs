---
title: hours_of_operation
hide_title: false
hide_table_of_contents: false
keywords:
  - hours_of_operation
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>hours_of_operation</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hours_of_operation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.connect.hours_of_operation</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>InstanceArn</code></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the hours of operation.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the hours of operation.</td></tr><tr><td><code>TimeZone</code></td><td><code>string</code></td><td>The time zone of the hours of operation.</td></tr><tr><td><code>Config</code></td><td><code>array</code></td><td>Configuration information for the hours of operation: day, start time, and end time.</td></tr><tr><td><code>HoursOfOperationArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the hours of operation.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>One or more tags.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.connect.hours_of_operation
WHERE region = 'us-east-1' AND data__Identifier = '<HoursOfOperationArn>'
</pre>
