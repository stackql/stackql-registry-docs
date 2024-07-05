---
title: scheduled_actions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_actions_list_only
  - redshift
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

Lists <code>scheduled_actions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/scheduled_actions/"><code>scheduled_actions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_actions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The `AWS::Redshift::ScheduledAction` resource creates an Amazon Redshift Scheduled Action.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.scheduled_actions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="scheduled_action_description" /></td><td><code>string</code></td><td>The description of the scheduled action.</td></tr>
<tr><td><CopyableCode code="scheduled_action_name" /></td><td><code>string</code></td><td>The name of the scheduled action. The name must be unique within an account.</td></tr>
<tr><td><CopyableCode code="end_time" /></td><td><code>string</code></td><td>The end time in UTC of the scheduled action. After this time, the scheduled action does not trigger.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the scheduled action.</td></tr>
<tr><td><CopyableCode code="schedule" /></td><td><code>string</code></td><td>The schedule in `at( )` or `cron( )` format.</td></tr>
<tr><td><CopyableCode code="iam_role" /></td><td><code>string</code></td><td>The IAM role to assume to run the target action.</td></tr>
<tr><td><CopyableCode code="start_time" /></td><td><code>string</code></td><td>The start time in UTC of the scheduled action. Before this time, the scheduled action does not trigger.</td></tr>
<tr><td><CopyableCode code="enable" /></td><td><code>boolean</code></td><td>If true, the schedule is enabled. If false, the scheduled action does not trigger.</td></tr>
<tr><td><CopyableCode code="target_action" /></td><td><code>object</code></td><td>A JSON format string of the Amazon Redshift API operation with input parameters.</td></tr>
<tr><td><CopyableCode code="next_invocations" /></td><td><code>array</code></td><td>List of times when the scheduled action will run.</td></tr>
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
Lists all <code>scheduled_actions</code> in a region.
```sql
SELECT
region,
scheduled_action_name
FROM aws.redshift.scheduled_actions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>scheduled_actions_list_only</code> resource, see <a href="/providers/aws/redshift/scheduled_actions/#permissions"><code>scheduled_actions</code></a>


