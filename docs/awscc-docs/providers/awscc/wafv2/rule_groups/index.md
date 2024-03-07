---
title: rule_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_groups
  - wafv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>rule_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>rule_groups</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.wafv2.rule_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>scope</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>rule_groups</code> resource, the following permissions are required:

### Create
<pre>
wafv2:CreateRuleGroup,
wafv2:GetRuleGroup,
wafv2:ListTagsForResource</pre>

### List
<pre>
wafv2:listRuleGroups</pre>


## Example
```sql
SELECT
region,
name,
id,
scope
FROM awscc.wafv2.rule_groups

```
