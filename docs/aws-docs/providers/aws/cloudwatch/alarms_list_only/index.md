---
title: alarms_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - alarms_list_only
  - cloudwatch
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

Lists <code>alarms</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/alarms/"><code>alarms</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarms_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::CloudWatch::Alarm</code> type specifies an alarm and associates it with the specified metric or metric math expression.<br />When this operation creates an alarm, the alarm state is immediately set to <code>INSUFFICIENT_DATA</code>. The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.<br />When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudwatch.alarms_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="alarm_name" /></td><td><code>string</code></td><td>The name of the alarm. If you don't specify a name, CFN generates a unique physical ID and uses that ID for the alarm name. <br />If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
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
Lists all <code>alarms</code> in a region.
```sql
SELECT
region,
alarm_name
FROM aws.cloudwatch.alarms_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>alarms_list_only</code> resource, see <a href="/providers/aws/cloudwatch/alarms/#permissions"><code>alarms</code></a>

