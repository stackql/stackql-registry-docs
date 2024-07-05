---
title: log_anomaly_detectors_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - log_anomaly_detectors_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>log_anomaly_detectors</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/log_anomaly_detectors/"><code>log_anomaly_detectors</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_anomaly_detectors_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Logs::LogAnomalyDetector resource specifies a CloudWatch Logs LogAnomalyDetector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.log_anomaly_detectors_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>Account ID for owner of detector</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.</td></tr>
<tr><td><CopyableCode code="detector_name" /></td><td><code>string</code></td><td>Name of detector</td></tr>
<tr><td><CopyableCode code="log_group_arn_list" /></td><td><code>array</code></td><td>List of Arns for the given log group</td></tr>
<tr><td><CopyableCode code="evaluation_frequency" /></td><td><code>string</code></td><td>How often log group is evaluated</td></tr>
<tr><td><CopyableCode code="filter_pattern" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="anomaly_detector_status" /></td><td><code>string</code></td><td>Current status of detector.</td></tr>
<tr><td><CopyableCode code="anomaly_visibility_time" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time_stamp" /></td><td><code>number</code></td><td>When detector was created.</td></tr>
<tr><td><CopyableCode code="last_modified_time_stamp" /></td><td><code>number</code></td><td>When detector was lsat modified.</td></tr>
<tr><td><CopyableCode code="anomaly_detector_arn" /></td><td><code>string</code></td><td>ARN of LogAnomalyDetector</td></tr>
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
Lists all <code>log_anomaly_detectors</code> in a region.
```sql
SELECT
region,
anomaly_detector_arn
FROM aws.logs.log_anomaly_detectors_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>log_anomaly_detectors_list_only</code> resource, see <a href="/providers/aws/logs/log_anomaly_detectors/#permissions"><code>log_anomaly_detectors</code></a>


