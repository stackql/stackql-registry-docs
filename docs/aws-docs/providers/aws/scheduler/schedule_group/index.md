---
title: schedule_group
hide_title: false
hide_table_of_contents: false
keywords:
  - schedule_group
  - scheduler
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>schedule_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schedule_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>schedule_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.scheduler.schedule_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the schedule group.</td></tr>
<tr><td><code>CreationDate</code></td><td><code>string</code></td><td>The time at which the schedule group was created.</td></tr>
<tr><td><code>LastModificationDate</code></td><td><code>string</code></td><td>The time at which the schedule group was last modified.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>State</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>The list of tags to associate with the schedule group.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.scheduler.schedule_group<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Name&gt;'
</pre>
