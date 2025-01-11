---
title: cloud_watch_alarm_template_groups_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_watch_alarm_template_groups_list_only
  - medialive
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

Lists <code>cloud_watch_alarm_template_groups</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/cloud_watch_alarm_template_groups/"><code>cloud_watch_alarm_template_groups</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_watch_alarm_template_groups_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaLive::CloudWatchAlarmTemplateGroup Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.cloud_watch_alarm_template_groups_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>A cloudwatch alarm template group's id. AWS provided template groups have ids that start with `aws-`</td></tr>
<tr><td><CopyableCode code="identifier" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>cloud_watch_alarm_template_groups</code> in a region.
```sql
SELECT
region,
identifier
FROM aws.medialive.cloud_watch_alarm_template_groups_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>cloud_watch_alarm_template_groups_list_only</code> resource, see <a href="/providers/aws/medialive/cloud_watch_alarm_template_groups/#permissions"><code>cloud_watch_alarm_template_groups</code></a>

