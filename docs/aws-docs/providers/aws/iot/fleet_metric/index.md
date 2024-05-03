---
title: fleet_metric
hide_title: false
hide_table_of_contents: false
keywords:
  - fleet_metric
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

Gets or operates on an individual <code>fleet_metric</code> resource, use <code>fleet_metrics</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleet_metric</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An aggregated metric of certain devices in your fleet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.fleet_metric" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="metric_name" /></td><td><code>string</code></td><td>The name of the fleet metric</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of a fleet metric</td></tr>
<tr><td><CopyableCode code="query_string" /></td><td><code>string</code></td><td>The Fleet Indexing query used by a fleet metric</td></tr>
<tr><td><CopyableCode code="period" /></td><td><code>integer</code></td><td>The period of metric emission in seconds</td></tr>
<tr><td><CopyableCode code="aggregation_field" /></td><td><code>string</code></td><td>The aggregation field to perform aggregation and metric emission</td></tr>
<tr><td><CopyableCode code="query_version" /></td><td><code>string</code></td><td>The version of a Fleet Indexing query used by a fleet metric</td></tr>
<tr><td><CopyableCode code="index_name" /></td><td><code>string</code></td><td>The index name of a fleet metric</td></tr>
<tr><td><CopyableCode code="unit" /></td><td><code>string</code></td><td>The unit of data points emitted by a fleet metric</td></tr>
<tr><td><CopyableCode code="aggregation_type" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="metric_arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of a fleet metric metric</td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td>The creation date of a fleet metric</td></tr>
<tr><td><CopyableCode code="last_modified_date" /></td><td><code>string</code></td><td>The last modified date of a fleet metric</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>number</code></td><td>The version of a fleet metric</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
metric_name,
description,
query_string,
period,
aggregation_field,
query_version,
index_name,
unit,
aggregation_type,
metric_arn,
creation_date,
last_modified_date,
version,
tags
FROM aws.iot.fleet_metric
WHERE data__Identifier = '<MetricName>';
```

## Permissions

To operate on the <code>fleet_metric</code> resource, the following permissions are required:

### Read
```json
iot:DescribeFleetMetric,
iot:ListTagsForResource
```

### Update
```json
iot:UpdateFleetMetric,
iot:DescribeFleetMetric,
iot:ListTagsForResource,
iot:UntagResource,
iot:TagResource
```

### Delete
```json
iot:DeleteFleetMetric,
iot:DescribeFleetMetric
```

