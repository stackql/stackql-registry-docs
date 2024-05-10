---
title: anomaly_monitor
hide_title: false
hide_table_of_contents: false
keywords:
  - anomaly_monitor
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


Gets or updates an individual <code>anomaly_monitor</code> resource, use <code>anomaly_monitors</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_monitor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Cost Anomaly Detection leverages advanced Machine Learning technologies to identify anomalous spend and root causes, so you can quickly take action. You can use Cost Anomaly Detection by creating monitor.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ce.anomaly_monitor" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="monitor_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="monitor_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="monitor_name" /></td><td><code>string</code></td><td>The name of the monitor.</td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td>The date when the monitor was created. </td></tr>
<tr><td><CopyableCode code="last_evaluated_date" /></td><td><code>string</code></td><td>The date when the monitor last evaluated for anomalies.</td></tr>
<tr><td><CopyableCode code="last_updated_date" /></td><td><code>string</code></td><td>The date when the monitor was last updated.</td></tr>
<tr><td><CopyableCode code="monitor_dimension" /></td><td><code>string</code></td><td>The dimensions to evaluate</td></tr>
<tr><td><CopyableCode code="monitor_specification" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dimensional_value_count" /></td><td><code>integer</code></td><td>The value for evaluated dimensions.</td></tr>
<tr><td><CopyableCode code="resource_tags" /></td><td><code>array</code></td><td>Tags to assign to monitor.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
monitor_arn,
monitor_type,
monitor_name,
creation_date,
last_evaluated_date,
last_updated_date,
monitor_dimension,
monitor_specification,
dimensional_value_count,
resource_tags
FROM aws.ce.anomaly_monitor
WHERE region = 'us-east-1' AND data__Identifier = '<MonitorArn>';
```


## Permissions

To operate on the <code>anomaly_monitor</code> resource, the following permissions are required:

### Read
```json
ce:GetAnomalyMonitors
```

### Update
```json
ce:UpdateAnomalyMonitor
```

