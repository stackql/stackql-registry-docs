---
title: fleet_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - fleet_metrics
  - iot
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

Used to retrieve a list of <code>fleet_metrics</code> in a region or create a <code>fleet_metrics</code> resource, use <code>fleet_metric</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleet_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An aggregated metric of certain devices in your fleet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.fleet_metrics" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="metric_name" /></td><td><code>string</code></td><td>The name of the fleet metric</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
metric_name
FROM aws.iot.fleet_metrics
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>fleet_metrics</code> resource, the following permissions are required:

### Create
```json
iot:CreateFleetMetric,
iot:DescribeFleetMetric,
iot:TagResource
```

### List
```json
iot:ListFleetMetrics
```

