---
title: dashboard_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboard_tags
  - cloudtrail
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

Expands all tag keys and values for <code>dashboards</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboard_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The Amazon CloudTrail dashboard resource allows customers to manage managed dashboards and create custom dashboards. You can manually refresh custom and managed dashboards. For custom dashboards, you can also set up an automatic refresh schedule and modify dashboard widgets.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudtrail.dashboard_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="widgets" /></td><td><code>array</code></td><td>List of widgets on the dashboard</td></tr>
<tr><td><CopyableCode code="created_timestamp" /></td><td><code>string</code></td><td>The timestamp of the dashboard creation.</td></tr>
<tr><td><CopyableCode code="dashboard_arn" /></td><td><code>string</code></td><td>The ARN of the dashboard.</td></tr>
<tr><td><CopyableCode code="refresh_schedule" /></td><td><code>object</code></td><td>Configures the automatic refresh schedule for the dashboard. Includes the frequency unit (DAYS or HOURS) and value, as well as the status (ENABLED or DISABLED) of the refresh schedule.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the dashboard.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the dashboard. Values are CREATING, CREATED, UPDATING, UPDATED and DELETING.</td></tr>
<tr><td><CopyableCode code="termination_protection_enabled" /></td><td><code>boolean</code></td><td>Indicates whether the dashboard is protected from termination.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the dashboard. Values are CUSTOM and MANAGED.</td></tr>
<tr><td><CopyableCode code="updated_timestamp" /></td><td><code>string</code></td><td>The timestamp showing when the dashboard was updated, if applicable. UpdatedTimestamp is always either the same or newer than the time shown in CreatedTimestamp.</td></tr>
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
Expands tags for all <code>dashboards</code> in a region.
```sql
SELECT
region,
widgets,
created_timestamp,
dashboard_arn,
refresh_schedule,
name,
status,
termination_protection_enabled,
type,
updated_timestamp,
tag_key,
tag_value
FROM aws.cloudtrail.dashboard_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>dashboard_tags</code> resource, see <a href="/providers/aws/cloudtrail/dashboards/#permissions"><code>dashboards</code></a>

