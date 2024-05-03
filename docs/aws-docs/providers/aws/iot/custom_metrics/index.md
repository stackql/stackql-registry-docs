---
title: custom_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_metrics
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

Used to retrieve a list of <code>custom_metrics</code> in a region or create a <code>custom_metrics</code> resource, use <code>custom_metric</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A custom metric published by your devices to Device Defender.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.custom_metrics" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="metric_name" /></td><td><code>string</code></td><td>The name of the custom metric. This will be used in the metric report submitted from the device&#x2F;thing. Shouldn't begin with aws: . Cannot be updated once defined.</td></tr>
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
FROM aws.iot.custom_metrics
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>custom_metrics</code> resource, the following permissions are required:

### Create
```json
iot:CreateCustomMetric,
iot:TagResource
```

### List
```json
iot:ListCustomMetrics
```

