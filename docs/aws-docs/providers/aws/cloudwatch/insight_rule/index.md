---
title: insight_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - insight_rule
  - cloudwatch
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>insight_rule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>insight_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>insight_rule</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudwatch.insight_rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>rule_state</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rule_body</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rule_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
rule_state,
id,
arn,
rule_body,
rule_name,
tags
FROM aws.cloudwatch.insight_rule
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
