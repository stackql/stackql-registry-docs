---
title: event_bridge_rule_template_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - event_bridge_rule_template_tags
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

Expands all tag keys and values for <code>event_bridge_rule_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_bridge_rule_template_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaLive::EventBridgeRuleTemplate Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.event_bridge_rule_template_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>An eventbridge rule template's ARN (Amazon Resource Name)</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Placeholder documentation for __timestampIso8601</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A resource's optional description.</td></tr>
<tr><td><CopyableCode code="event_targets" /></td><td><code>array</code></td><td>Placeholder documentation for __listOfEventBridgeRuleTemplateTarget</td></tr>
<tr><td><CopyableCode code="event_type" /></td><td><code>string</code></td><td>The type of event to match with the rule.</td></tr>
<tr><td><CopyableCode code="group_id" /></td><td><code>string</code></td><td>An eventbridge rule template group's id. AWS provided template groups have ids that start with `aws-`</td></tr>
<tr><td><CopyableCode code="group_identifier" /></td><td><code>string</code></td><td>An eventbridge rule template group's identifier. Can be either be its id or current name.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>An eventbridge rule template's id. AWS provided templates have ids that start with `aws-`</td></tr>
<tr><td><CopyableCode code="identifier" /></td><td><code>string</code></td><td>Placeholder documentation for __string</td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td>Placeholder documentation for __timestampIso8601</td></tr>
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
Expands tags for all <code>event_bridge_rule_templates</code> in a region.
```sql
SELECT
region,
arn,
created_at,
description,
event_targets,
event_type,
group_id,
group_identifier,
id,
identifier,
modified_at,
name,
tag_key,
tag_value
FROM aws.medialive.event_bridge_rule_template_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>event_bridge_rule_template_tags</code> resource, see <a href="/providers/aws/medialive/event_bridge_rule_templates/#permissions"><code>event_bridge_rule_templates</code></a>

