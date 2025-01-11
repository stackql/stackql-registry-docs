---
title: cloud_watch_alarm_template_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_watch_alarm_template_group_tags
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

Expands all tag keys and values for <code>cloud_watch_alarm_template_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_watch_alarm_template_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaLive::CloudWatchAlarmTemplateGroup Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.cloud_watch_alarm_template_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>A cloudwatch alarm template group's ARN (Amazon Resource Name)</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A resource's optional description.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>A cloudwatch alarm template group's id. AWS provided template groups have ids that start with `aws-`</td></tr>
<tr><td><CopyableCode code="identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A resource's name. Names must be unique within the scope of a resource type in a specific region.</td></tr>
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
Expands tags for all <code>cloud_watch_alarm_template_groups</code> in a region.
```sql
SELECT
region,
arn,
created_at,
description,
id,
identifier,
modified_at,
name,
tag_key,
tag_value
FROM aws.medialive.cloud_watch_alarm_template_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>cloud_watch_alarm_template_group_tags</code> resource, see <a href="/providers/aws/medialive/cloud_watch_alarm_template_groups/#permissions"><code>cloud_watch_alarm_template_groups</code></a>

