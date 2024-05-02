---
title: anomaly_detector
hide_title: false
hide_table_of_contents: false
keywords:
  - anomaly_detector
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
Gets an individual <code>anomaly_detector</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_detector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An Amazon Lookout for Metrics Detector</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lookoutmetrics.anomaly_detector</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>anomaly_detector_name</code></td><td><code>string</code></td><td>Name for the Amazon Lookout for Metrics Anomaly Detector</td></tr>
<tr><td><code>anomaly_detector_description</code></td><td><code>string</code></td><td>A description for the AnomalyDetector.</td></tr>
<tr><td><code>anomaly_detector_config</code></td><td><code>object</code></td><td>Configuration options for the AnomalyDetector</td></tr>
<tr><td><code>metric_set_list</code></td><td><code>array</code></td><td>List of metric sets for anomaly detection</td></tr>
<tr><td><code>kms_key_arn</code></td><td><code>string</code></td><td>KMS key used to encrypt the AnomalyDetector data</td></tr>
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
arn,
anomaly_detector_name,
anomaly_detector_description,
anomaly_detector_config,
metric_set_list,
kms_key_arn
FROM aws.lookoutmetrics.anomaly_detector
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>anomaly_detector</code> resource, the following permissions are required:

### Read
```json
lookoutmetrics:DescribeAnomalyDetector,
lookoutmetrics:DescribeMetricSet,
lookoutmetrics:ListMetricSets
```

### Update
```json
lookoutmetrics:UpdateAnomalyDetector,
lookoutmetrics:UpdateMetricSet
```

### Delete
```json
lookoutmetrics:DescribeAnomalyDetector,
lookoutmetrics:DeleteAnomalyDetector
```

