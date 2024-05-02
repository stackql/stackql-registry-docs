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
<tr><td><b>Description</b></td><td>Contains the Rules that identify the requests that you want to allow, block, or count. In a RuleGroup, you also specify a default action (ALLOW or BLOCK), and the action for each Rule that you add to a RuleGroup, for example, block requests from specified IP addresses or block requests from specified referrers. You also associate the RuleGroup with a CloudFront distribution to identify the requests that you want AWS WAF to filter. If you add more than one Rule to a RuleGroup, a request needs to match only one of the specifications to be allowed, blocked, or counted.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.wafv2.rule_groups</code></td></tr>
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

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name,
id,
scope
FROM aws.wafv2.rule_groups

```

## Permissions

To operate on the <code>rule_groups</code> resource, the following permissions are required:

### Create
```json
wafv2:CreateRuleGroup,
wafv2:GetRuleGroup,
wafv2:ListTagsForResource
```

### List
```json
wafv2:listRuleGroups
```

