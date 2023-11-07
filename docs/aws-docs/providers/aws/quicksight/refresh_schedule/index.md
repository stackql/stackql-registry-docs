---
title: refresh_schedule
hide_title: false
hide_table_of_contents: false
keywords:
  - refresh_schedule
  - quicksight
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>refresh_schedule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>refresh_schedule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.quicksight.refresh_schedule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) of the data source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>AwsAccountId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DataSetId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Schedule</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.quicksight.refresh_schedule
WHERE region = 'us-east-1' AND data__Identifier = '&lt;AwsAccountId&gt;' AND data__Identifier = '&lt;DataSetId&gt;' AND data__Identifier = '&lt;Schedule/ScheduleId&gt;'
</pre>
