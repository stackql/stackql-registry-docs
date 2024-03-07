---
title: log_anomaly_detectors
hide_title: false
hide_table_of_contents: false
keywords:
  - log_anomaly_detectors
  - logs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>log_anomaly_detectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_anomaly_detectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>log_anomaly_detectors</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.logs.log_anomaly_detectors</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>anomaly_detector_arn</code></td><td><code>string</code></td><td>ARN of LogAnomalyDetector</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>log_anomaly_detectors</code> resource, the following permissions are required:

### Create
```json
logs:CreateLogAnomalyDetector
```

### List
```json
logs:ListLogAnomalyDetectors
```


## Example
```sql
SELECT
region,
anomaly_detector_arn
FROM awscc.logs.log_anomaly_detectors
WHERE region = 'us-east-1'
```
