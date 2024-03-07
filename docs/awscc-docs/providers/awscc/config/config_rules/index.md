---
title: config_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - config_rules
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
Retrieves a list of <code>config_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>config_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>config_rules</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.config.config_rules</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>config_rule_name</code></td><td><code>string</code></td><td>A name for the CC rule. If you don't specify a name, CFN generates a unique physical ID and uses that ID for the rule name. For more information, see &#91;Name Type&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html).</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>config_rules</code> resource, the following permissions are required:

### Create
```json
config:PutConfigRule,
config:DescribeConfigRules
```

### List
```json
config:DescribeConfigRules
```


## Example
```sql
SELECT
region,
config_rule_name
FROM awscc.config.config_rules
WHERE region = 'us-east-1'
```
