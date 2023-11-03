---
title: launch
hide_title: false
hide_table_of_contents: false
keywords:
  - launch
  - evidently
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>launch</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.evidently.launch</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Project</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RandomizationSalt</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ScheduledSplitsConfig</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Groups</code></td><td><code>array</code></td><td></td></tr><tr><td><code>MetricMonitors</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr><tr><td><code>ExecutionStatus</code></td><td><code>undefined</code></td><td>Start or Stop Launch Launch. Default is not started.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.evidently.launch
WHERE region = 'us-east-1' AND data__Identifier = '{Arn}'
</pre>
