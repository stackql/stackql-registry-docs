---
title: organization_config_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_config_rule
  - config
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>organization_config_rule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_config_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>organization_config_rule</td></tr>
<tr><td><b>Id</b></td><td><code>aws.config.organization_config_rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>organization_custom_rule_metadata</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>organization_managed_rule_metadata</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>excluded_accounts</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>organization_config_rule_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>organization_custom_policy_rule_metadata</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
organization_custom_rule_metadata,
organization_managed_rule_metadata,
excluded_accounts,
organization_config_rule_name,
id,
organization_custom_policy_rule_metadata
FROM aws.config.organization_config_rule
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
