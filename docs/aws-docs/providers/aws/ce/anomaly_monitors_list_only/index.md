---
title: anomaly_monitors_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - anomaly_monitors_list_only
  - ce
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

Lists <code>anomaly_monitors</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/anomaly_monitors/"><code>anomaly_monitors</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_monitors_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Cost Anomaly Detection leverages advanced Machine Learning technologies to identify anomalous spend and root causes, so you can quickly take action. You can use Cost Anomaly Detection by creating monitor.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ce.anomaly_monitors_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="monitor_arn" /></td><td><code>string</code></td><td>Subscription ARN</td></tr>
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
Lists all <code>anomaly_monitors</code> in a region.
```sql
SELECT
region,
monitor_arn
FROM aws.ce.anomaly_monitors_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>anomaly_monitors_list_only</code> resource, see <a href="/providers/aws/ce/anomaly_monitors/#permissions"><code>anomaly_monitors</code></a>

