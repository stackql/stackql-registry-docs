---
title: experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - experiments
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
Retrieves a list of <code>experiments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.evidently.experiments</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Project</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RunningStatus</code></td><td><code>undefined</code></td><td>Start Experiment. Default is False</td></tr>
<tr><td><code>RandomizationSalt</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Treatments</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>MetricGoals</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>SamplingRate</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>OnlineAbConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Segment</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RemoveSegment</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.evidently.experiments
WHERE region = 'us-east-1'
</pre>
