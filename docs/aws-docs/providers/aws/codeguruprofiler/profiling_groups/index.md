---
title: profiling_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - profiling_groups
  - codeguruprofiler
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>profiling_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiling_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>profiling_groups</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codeguruprofiler.profiling_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ProfilingGroupName</code></td><td><code>string</code></td><td>The name of the profiling group.</td></tr>
<tr><td><code>ComputePlatform</code></td><td><code>string</code></td><td>The compute platform of the profiling group.</td></tr>
<tr><td><code>AgentPermissions</code></td><td><code>object</code></td><td>The agent permissions attached to this profiling group.</td></tr>
<tr><td><code>AnomalyDetectionNotificationConfiguration</code></td><td><code>array</code></td><td>Configuration for Notification Channels for Anomaly Detection feature in CodeGuru Profiler which enables customers to detect anomalies in the application profile for those methods that represent the highest proportion of CPU time or latency</td></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td>The Amazon Resource Name (ARN) of the specified profiling group.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags associated with a profiling group.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.codeguruprofiler.profiling_groups<br/>WHERE region = 'us-east-1'
</pre>
