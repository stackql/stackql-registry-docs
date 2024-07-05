---
title: rule_groups_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_groups_list_only
  - networkfirewall
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

Lists <code>rule_groups</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/rule_groups/"><code>rule_groups</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_groups_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::NetworkFirewall::RuleGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkfirewall.rule_groups_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="rule_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_group_arn" /></td><td><code>string</code></td><td>A resource ARN.</td></tr>
<tr><td><CopyableCode code="rule_group_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_group" /></td><td><code>object</code></td><td>Resource type definition for AWS::NetworkFirewall::RuleGroup</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="capacity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
Lists all <code>rule_groups</code> in a region.
```sql
SELECT
region,
rule_group_arn
FROM aws.networkfirewall.rule_groups_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>rule_groups_list_only</code> resource, see <a href="/providers/aws/networkfirewall/rule_groups/#permissions"><code>rule_groups</code></a>


