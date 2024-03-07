---
title: rule_group
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_group
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
Gets an individual <code>rule_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>rule_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.wafv2.rule_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>capacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>scope</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rules</code></td><td><code>array</code></td><td>Collection of Rules.</td></tr>
<tr><td><code>visibility_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>label_namespace</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>custom_response_bodies</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>available_labels</code></td><td><code>array</code></td><td>Collection of Available Labels.</td></tr>
<tr><td><code>consumed_labels</code></td><td><code>array</code></td><td>Collection of Consumed Labels.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>rule_group</code> resource, the following permissions are required:

### Delete
```json
wafv2:DeleteRuleGroup,
wafv2:GetRuleGroup
```

### Read
```json
wafv2:GetRuleGroup,
wafv2:ListTagsForResource
```

### Update
```json
wafv2:UpdateRuleGroup,
wafv2:GetRuleGroup,
wafv2:ListTagsForResource
```


## Example
```sql
SELECT
region,
arn,
capacity,
description,
name,
id,
scope,
rules,
visibility_config,
tags,
label_namespace,
custom_response_bodies,
available_labels,
consumed_labels
FROM awscc.wafv2.rule_group
WHERE data__Identifier = '&lt;Name&gt;'
AND data__Identifier = '&lt;Id&gt;'
AND data__Identifier = '&lt;Scope&gt;'
```
