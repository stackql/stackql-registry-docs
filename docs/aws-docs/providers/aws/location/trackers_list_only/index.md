---
title: trackers_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - trackers_list_only
  - location
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

Lists <code>trackers</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/trackers/"><code>trackers</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trackers_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Location::Tracker Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.location.trackers_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="create_time" /></td><td><code>string</code></td><td>The datetime value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ss.sssZ)</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="event_bridge_enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_enable_geospatial_queries" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="position_filtering" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pricing_plan" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pricing_plan_data_source" /></td><td><code>string</code></td><td>This shape is deprecated since 2022-02-01: Deprecated. No longer allowed.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="tracker_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tracker_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="update_time" /></td><td><code>string</code></td><td>The datetime value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ss.sssZ)</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>trackers</code> in a region.
```sql
SELECT
region,
tracker_name
FROM aws.location.trackers_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>trackers_list_only</code> resource, see <a href="/providers/aws/location/trackers/#permissions"><code>trackers</code></a>


