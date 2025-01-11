---
title: service_level_objective_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - service_level_objective_tags
  - applicationsignals
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

Expands all tag keys and values for <code>service_level_objectives</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_level_objective_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ApplicationSignals::ServiceLevelObjective</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.applicationsignals.service_level_objective_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of this SLO.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of this SLO.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>An optional description for this SLO. Default is 'No description'</td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>integer</code></td><td>Epoch time in seconds of the time that this SLO was created</td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>integer</code></td><td>Epoch time in seconds of the time that this SLO was most recently updated</td></tr>
<tr><td><CopyableCode code="sli" /></td><td><code>object</code></td><td>This structure contains information about the performance metric that an SLO monitors.</td></tr>
<tr><td><CopyableCode code="request_based_sli" /></td><td><code>object</code></td><td>This structure contains information about the performance metric that a request-based SLO monitors.</td></tr>
<tr><td><CopyableCode code="evaluation_type" /></td><td><code>string</code></td><td>Displays whether this is a period-based SLO or a request-based SLO.</td></tr>
<tr><td><CopyableCode code="goal" /></td><td><code>object</code></td><td>A structure that contains the attributes that determine the goal of the SLO. This includes the time period for evaluation and the attainment threshold.</td></tr>
<tr><td><CopyableCode code="burn_rate_configurations" /></td><td><code>array</code></td><td>Each object in this array defines the length of the look-back window used to calculate one burn rate metric for this SLO. The burn rate measures how fast the service is consuming the error budget, relative to the attainment goal of the SLO.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>service_level_objectives</code> in a region.
```sql
SELECT
region,
arn,
name,
description,
created_time,
last_updated_time,
sli,
request_based_sli,
evaluation_type,
goal,
burn_rate_configurations,
tag_key,
tag_value
FROM aws.applicationsignals.service_level_objective_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>service_level_objective_tags</code> resource, see <a href="/providers/aws/applicationsignals/service_level_objectives/#permissions"><code>service_level_objectives</code></a>

