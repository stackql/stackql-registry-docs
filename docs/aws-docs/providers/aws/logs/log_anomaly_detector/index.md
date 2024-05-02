---
title: log_anomaly_detector
hide_title: false
hide_table_of_contents: false
keywords:
  - log_anomaly_detector
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
Gets or operates on an individual <code>log_anomaly_detector</code> resource, use <code>log_anomaly_detectors</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_anomaly_detector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Logs::LogAnomalyDetector resource specifies a CloudWatch Logs LogAnomalyDetector.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.logs.log_anomaly_detector</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td>Account ID for owner of detector</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.</td></tr>
<tr><td><code>detector_name</code></td><td><code>string</code></td><td>Name of detector</td></tr>
<tr><td><code>log_group_arn_list</code></td><td><code>array</code></td><td>List of Arns for the given log group</td></tr>
<tr><td><code>evaluation_frequency</code></td><td><code>string</code></td><td>How often log group is evaluated</td></tr>
<tr><td><code>filter_pattern</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>anomaly_detector_status</code></td><td><code>string</code></td><td>Current status of detector.</td></tr>
<tr><td><code>anomaly_visibility_time</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>creation_time_stamp</code></td><td><code>number</code></td><td>When detector was created.</td></tr>
<tr><td><code>last_modified_time_stamp</code></td><td><code>number</code></td><td>When detector was lsat modified.</td></tr>
<tr><td><code>anomaly_detector_arn</code></td><td><code>string</code></td><td>ARN of LogAnomalyDetector</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
account_id,
kms_key_id,
detector_name,
log_group_arn_list,
evaluation_frequency,
filter_pattern,
anomaly_detector_status,
anomaly_visibility_time,
creation_time_stamp,
last_modified_time_stamp,
anomaly_detector_arn
FROM aws.logs.log_anomaly_detector
WHERE data__Identifier = '<AnomalyDetectorArn>';
```

## Permissions

To operate on the <code>log_anomaly_detector</code> resource, the following permissions are required:

### Read
```json
logs:GetLogAnomalyDetector
```

### Update
```json
logs:UpdateLogAnomalyDetector
```

### Delete
```json
logs:DeleteLogAnomalyDetector
```

