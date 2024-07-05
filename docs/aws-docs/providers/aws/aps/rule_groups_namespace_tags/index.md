---
title: rule_groups_namespace_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_groups_namespace_tags
  - aps
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

Expands all tag keys and values for <code>rule_groups_namespaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_groups_namespace_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>RuleGroupsNamespace schema for cloudformation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.aps.rule_groups_namespace_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="workspace" /></td><td><code>string</code></td><td>Required to identify a specific APS Workspace associated with this RuleGroupsNamespace.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The RuleGroupsNamespace name.</td></tr>
<tr><td><CopyableCode code="data" /></td><td><code>string</code></td><td>The RuleGroupsNamespace data.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The RuleGroupsNamespace ARN.</td></tr>
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
Expands tags for all <code>rule_groups_namespaces</code> in a region.
```sql
SELECT
region,
workspace,
name,
data,
arn,
tag_key,
tag_value
FROM aws.aps.rule_groups_namespace_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>rule_groups_namespace_tags</code> resource, see <a href="/providers/aws/aps/rule_groups_namespaces/#permissions"><code>rule_groups_namespaces</code></a>


