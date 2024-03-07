---
title: anomaly_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - anomaly_monitors
  - ce
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>anomaly_monitors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>anomaly_monitors</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ce.anomaly_monitors</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>monitor_arn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>anomaly_monitors</code> resource, the following permissions are required:

### Create
<pre>
ce:CreateAnomalyMonitor,
ce:TagResource</pre>

### List
<pre>
ce:GetAnomalyMonitors</pre>


## Example
```sql
SELECT
region,
monitor_arn
FROM awscc.ce.anomaly_monitors
WHERE region = 'us-east-1'
```
