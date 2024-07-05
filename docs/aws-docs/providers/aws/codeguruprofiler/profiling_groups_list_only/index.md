---
title: profiling_groups_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - profiling_groups_list_only
  - codeguruprofiler
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

Lists <code>profiling_groups</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/profiling_groups/"><code>profiling_groups</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiling_groups_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This resource schema represents the Profiling Group resource in the Amazon CodeGuru Profiler service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codeguruprofiler.profiling_groups_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="profiling_group_name" /></td><td><code>string</code></td><td>The name of the profiling group.</td></tr>
<tr><td><CopyableCode code="compute_platform" /></td><td><code>string</code></td><td>The compute platform of the profiling group.</td></tr>
<tr><td><CopyableCode code="agent_permissions" /></td><td><code>object</code></td><td>The agent permissions attached to this profiling group.</td></tr>
<tr><td><CopyableCode code="anomaly_detection_notification_configuration" /></td><td><code>array</code></td><td>Configuration for Notification Channels for Anomaly Detection feature in CodeGuru Profiler which enables customers to detect anomalies in the application profile for those methods that represent the highest proportion of CPU time or latency</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified profiling group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags associated with a profiling group.</td></tr>
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
Lists all <code>profiling_groups</code> in a region.
```sql
SELECT
region,
profiling_group_name
FROM aws.codeguruprofiler.profiling_groups_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>profiling_groups_list_only</code> resource, see <a href="/providers/aws/codeguruprofiler/profiling_groups/#permissions"><code>profiling_groups</code></a>


