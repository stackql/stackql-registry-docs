---
title: alerts_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts_list_only
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

Lists <code>alerts</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/alerts/"><code>alerts</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::LookoutMetrics::Alert</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lookoutmetrics.alerts_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="alert_name" /></td><td><code>string</code></td><td>The name of the alert. If not provided, a name is generated automatically.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN assigned to the alert.</td></tr>
<tr><td><CopyableCode code="alert_description" /></td><td><code>string</code></td><td>A description for the alert.</td></tr>
<tr><td><CopyableCode code="anomaly_detector_arn" /></td><td><code>string</code></td><td>The Amazon resource name (ARN) of the Anomaly Detector to alert.</td></tr>
<tr><td><CopyableCode code="alert_sensitivity_threshold" /></td><td><code>integer</code></td><td>A number between 0 and 100 (inclusive) that tunes the sensitivity of the alert.</td></tr>
<tr><td><CopyableCode code="action" /></td><td><code>object</code></td><td>The action to be taken by the alert when an anomaly is detected.</td></tr>
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
Lists all <code>alerts</code> in a region.
```sql
SELECT
region,
arn
FROM aws.lookoutmetrics.alerts_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>alerts_list_only</code> resource, see <a href="/providers/aws/lookoutmetrics/alerts/#permissions"><code>alerts</code></a>


