---
title: sampling_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - sampling_rules
  - xray
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>sampling_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sampling_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>sampling_rules</td></tr>
<tr><td><b>Id</b></td><td><code>aws.xray.sampling_rules</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>rule_ar_n</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
rule_ar_n
FROM aws.xray.sampling_rules
WHERE region = 'us-east-1'
```
