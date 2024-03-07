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
<tr><td><b>Description</b></td><td>alert</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lookoutmetrics.alert</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>alert_name</code></td><td><code>string</code></td><td>The name of the alert. If not provided, a name is generated automatically.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>ARN assigned to the alert.</td></tr>
<tr><td><code>alert_description</code></td><td><code>string</code></td><td>A description for the alert.</td></tr>
<tr><td><code>anomaly_detector_arn</code></td><td><code>string</code></td><td>The Amazon resource name (ARN) of the Anomaly Detector to alert.</td></tr>
<tr><td><code>alert_sensitivity_threshold</code></td><td><code>integer</code></td><td>A number between 0 and 100 (inclusive) that tunes the sensitivity of the alert.</td></tr>
<tr><td><code>action</code></td><td><code>object</code></td><td>The action to be taken by the alert when an anomaly is detected.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>alert</code> resource, the following permissions are required:

### Read
```json
lookoutmetrics:DescribeAlert
```

### Delete
```json
lookoutmetrics:DeleteAlert
```


## Example
```sql
SELECT
region,
alert_name,
arn,
alert_description,
anomaly_detector_arn,
alert_sensitivity_threshold,
action
FROM awscc.lookoutmetrics.alert
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
