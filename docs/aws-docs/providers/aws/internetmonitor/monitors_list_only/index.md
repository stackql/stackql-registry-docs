---
title: monitors_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_list_only
  - internetmonitor
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

Lists <code>monitors</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/monitors/"><code>monitors</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitors_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a monitor, which defines the monitoring boundaries for measurements that Internet Monitor publishes information about for an application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.internetmonitor.monitors_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The date value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ssZ)</td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td>The date value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ssZ)</td></tr>
<tr><td><CopyableCode code="monitor_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="monitor_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="linked_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="include_linked_accounts" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="processing_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="processing_status_info" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resources" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resources_to_add" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resources_to_remove" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="max_city_networks_to_monitor" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="traffic_percentage_to_monitor" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="internet_measurements_log_delivery" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="health_events_config" /></td><td><code>object</code></td><td></td></tr>
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
Lists all <code>monitors</code> in a region.
```sql
SELECT
region,
monitor_name
FROM aws.internetmonitor.monitors_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>monitors_list_only</code> resource, see <a href="/providers/aws/internetmonitor/monitors/#permissions"><code>monitors</code></a>

