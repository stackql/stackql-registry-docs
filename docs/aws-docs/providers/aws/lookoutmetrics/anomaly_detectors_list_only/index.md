---
title: anomaly_detectors_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - anomaly_detectors_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>anomaly_detectors</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/anomaly_detectors/"><code>anomaly_detectors</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_detectors_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An Amazon Lookout for Metrics Detector</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lookoutmetrics.anomaly_detectors_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="anomaly_detector_name" /></td><td><code>string</code></td><td>Name for the Amazon Lookout for Metrics Anomaly Detector</td></tr>
<tr><td><CopyableCode code="anomaly_detector_description" /></td><td><code>string</code></td><td>A description for the AnomalyDetector.</td></tr>
<tr><td><CopyableCode code="anomaly_detector_config" /></td><td><code>object</code></td><td>Configuration options for the AnomalyDetector</td></tr>
<tr><td><CopyableCode code="metric_set_list" /></td><td><code>array</code></td><td>List of metric sets for anomaly detection</td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td>KMS key used to encrypt the AnomalyDetector data</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>anomaly_detectors</code> in a region.
```sql
SELECT
region,
arn
FROM aws.lookoutmetrics.anomaly_detectors_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>anomaly_detectors_list_only</code> resource, see <a href="/providers/aws/lookoutmetrics/anomaly_detectors/#permissions"><code>anomaly_detectors</code></a>


