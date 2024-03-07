---
title: sampling_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - sampling_rule
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
Gets an individual <code>sampling_rule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sampling_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>sampling_rule</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.xray.sampling_rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>sampling_rule</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>sampling_rule_record</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>sampling_rule_update</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>rule_ar_n</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rule_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>sampling_rule</code> resource, the following permissions are required:

### Read
<pre>
xray:GetSamplingRules,
xray:ListTagsForResource</pre>

### Update
<pre>
xray:UpdateSamplingRule,
xray:TagResource,
xray:UntagResource,
xray:ListTagsForResource</pre>

### Delete
<pre>
xray:DeleteSamplingRule</pre>


## Example
```sql
SELECT
region,
sampling_rule,
sampling_rule_record,
sampling_rule_update,
rule_ar_n,
rule_name,
tags
FROM awscc.xray.sampling_rule
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;RuleARN&gt;'
```
