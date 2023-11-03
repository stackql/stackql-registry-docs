---
title: rulesets
hide_title: false
hide_table_of_contents: false
keywords:
  - rulesets
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
Retrieves a list of <code>rulesets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rulesets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.databrew.rulesets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Name of the Ruleset</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>Description of the Ruleset</td></tr><tr><td><code>TargetArn</code></td><td><code>string</code></td><td>Arn of the target resource (dataset) to apply the ruleset to</td></tr><tr><td><code>Rules</code></td><td><code>array</code></td><td>List of the data quality rules in the ruleset</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.databrew.rulesets
WHERE region = 'us-east-1'
```
