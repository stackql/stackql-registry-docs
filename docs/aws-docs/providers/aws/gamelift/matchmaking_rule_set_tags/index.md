---
title: matchmaking_rule_set_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - matchmaking_rule_set_tags
  - gamelift
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

Expands all tag keys and values for <code>matchmaking_rule_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>matchmaking_rule_set_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::MatchmakingRuleSet resource creates an Amazon GameLift (GameLift) matchmaking rule set.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.matchmaking_rule_set_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A unique identifier for the matchmaking rule set.</td></tr>
<tr><td><CopyableCode code="rule_set_body" /></td><td><code>string</code></td><td>A collection of matchmaking rules, formatted as a JSON string.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift matchmaking rule set resource and uniquely identifies it.</td></tr>
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
Expands tags for all <code>matchmaking_rule_sets</code> in a region.
```sql
SELECT
region,
name,
rule_set_body,
creation_time,
arn,
tag_key,
tag_value
FROM aws.gamelift.matchmaking_rule_set_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>matchmaking_rule_set_tags</code> resource, see <a href="/providers/aws/gamelift/matchmaking_rule_sets/#permissions"><code>matchmaking_rule_sets</code></a>

