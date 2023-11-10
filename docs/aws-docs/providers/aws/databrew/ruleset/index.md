---
title: ruleset
hide_title: false
hide_table_of_contents: false
keywords:
  - ruleset
  - databrew
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>ruleset</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ruleset</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>ruleset</td></tr>
<tr><td><b>Id</b></td><td><code>aws.databrew.ruleset</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the Ruleset</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of the Ruleset</td></tr>
<tr><td><code>target_arn</code></td><td><code>string</code></td><td>Arn of the target resource (dataset) to apply the ruleset to</td></tr>
<tr><td><code>rules</code></td><td><code>array</code></td><td>List of the data quality rules in the ruleset</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
description,
target_arn,
rules,
tags
FROM aws.databrew.ruleset
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Name&gt;'
```
