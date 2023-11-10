---
title: config_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - config_rule
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
Gets an individual <code>config_rule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>config_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>config_rule</td></tr>
<tr><td><b>Id</b></td><td><code>aws.config.config_rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>config_rule_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>scope</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>compliance_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>config_rule_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>maximum_execution_frequency</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>input_parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
config_rule_id,
description,
scope,
compliance_type,
config_rule_name,
arn,
maximum_execution_frequency,
source,
input_parameters
FROM aws.config.config_rule
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ConfigRuleId&gt;'
```
