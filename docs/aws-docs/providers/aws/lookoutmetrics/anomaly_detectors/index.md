---
title: anomaly_detectors
hide_title: false
hide_table_of_contents: false
keywords:
  - anomaly_detectors
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
Retrieves a list of <code>anomaly_detectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_detectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>anomaly_detectors</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lookoutmetrics.anomaly_detectors</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AnomalyDetectorName</code></td><td><code>string</code></td><td>Name for the Amazon Lookout for Metrics Anomaly Detector</td></tr>
<tr><td><code>AnomalyDetectorDescription</code></td><td><code>string</code></td><td>A description for the AnomalyDetector.</td></tr>
<tr><td><code>AnomalyDetectorConfig</code></td><td><code>object</code></td><td>Configuration options for the AnomalyDetector</td></tr>
<tr><td><code>MetricSetList</code></td><td><code>array</code></td><td>List of metric sets for anomaly detection</td></tr>
<tr><td><code>KmsKeyArn</code></td><td><code>string</code></td><td>KMS key used to encrypt the AnomalyDetector data</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.lookoutmetrics.anomaly_detectors<br/>WHERE region = 'us-east-1'
</pre>
