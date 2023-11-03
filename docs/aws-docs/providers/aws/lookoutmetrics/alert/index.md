---
title: alert
hide_title: false
hide_table_of_contents: false
keywords:
  - alert
  - lookoutmetrics
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>alert</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alert</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lookoutmetrics.alert</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AlertName</code></td><td><code>string</code></td><td>The name of the alert. If not provided, a name is generated automatically.</td></tr><tr><td><code>Arn</code></td><td><code>undefined</code></td><td>ARN assigned to the alert.</td></tr><tr><td><code>AlertDescription</code></td><td><code>string</code></td><td>A description for the alert.</td></tr><tr><td><code>AnomalyDetectorArn</code></td><td><code>string</code></td><td>The Amazon resource name (ARN) of the Anomaly Detector to alert.</td></tr><tr><td><code>AlertSensitivityThreshold</code></td><td><code>integer</code></td><td>A number between 0 and 100 (inclusive) that tunes the sensitivity of the alert.</td></tr><tr><td><code>Action</code></td><td><code>undefined</code></td><td>The action to be taken by the alert when an anomaly is detected.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.lookoutmetrics.alert
WHERE region = 'us-east-1' AND data__Identifier = '{Arn}'
</pre>
