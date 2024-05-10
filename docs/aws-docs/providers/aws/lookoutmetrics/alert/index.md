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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>alert</code> resource, use <code>alerts</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alert</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::LookoutMetrics::Alert</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lookoutmetrics.alert" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="alert_name" /></td><td><code>string</code></td><td>The name of the alert. If not provided, a name is generated automatically.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
alert_name,
arn,
alert_description,
anomaly_detector_arn,
alert_sensitivity_threshold,
action
FROM aws.lookoutmetrics.alert
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>alert</code> resource, the following permissions are required:

### Read
```json
lookoutmetrics:DescribeAlert
```

