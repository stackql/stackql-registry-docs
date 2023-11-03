---
title: rule_groups_namespace
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_groups_namespace
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
Gets an individual <code>rule_groups_namespace</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_groups_namespace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.aps.rule_groups_namespace</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Workspace</code></td><td><code>string</code></td><td>Required to identify a specific APS Workspace associated with this RuleGroupsNamespace.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The RuleGroupsNamespace name.</td></tr><tr><td><code>Data</code></td><td><code>string</code></td><td>The RuleGroupsNamespace data.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>The RuleGroupsNamespace ARN.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.aps.rule_groups_namespace
WHERE region = 'us-east-1' AND data__Identifier = '{Arn}'
```
