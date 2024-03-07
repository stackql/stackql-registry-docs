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
<tr><td><b>Id</b></td><td><code>awscc.config.config_rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>config_rule_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description that you provide for the CC rule.</td></tr>
<tr><td><code>scope</code></td><td><code>object</code></td><td>Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.&lt;br&#x2F;&gt;  The scope can be empty.</td></tr>
<tr><td><code>config_rule_name</code></td><td><code>string</code></td><td>A name for the CC rule. If you don't specify a name, CFN generates a unique physical ID and uses that ID for the rule name. For more information, see &#91;Name Type&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html).</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>compliance</code></td><td><code>object</code></td><td>Indicates whether an AWS resource or CC rule is compliant and provides the number of contributors that affect the compliance.</td></tr>
<tr><td><code>maximum_execution_frequency</code></td><td><code>string</code></td><td>The maximum frequency with which CC runs evaluations for a rule. You can specify a value for ``MaximumExecutionFrequency`` when:&lt;br&#x2F;&gt;  +  You are using an AWS managed rule that is triggered at a periodic frequency.&lt;br&#x2F;&gt;  +  Your custom rule is triggered when CC delivers the configuration snapshot. For more information, see &#91;ConfigSnapshotDeliveryProperties&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;config&#x2F;latest&#x2F;APIReference&#x2F;API_ConfigSnapshotDeliveryProperties.html).&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt;  By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.</td></tr>
<tr><td><code>source</code></td><td><code>object</code></td><td>Provides the rule owner (```` for managed rules, ``CUSTOM_POLICY`` for Custom Policy rules, and ``CUSTOM_LAMBDA`` for Custom Lambda rules), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.</td></tr>
<tr><td><code>input_parameters</code></td><td><code>object</code></td><td>A string, in JSON format, that is passed to the CC rule Lambda function.</td></tr>
<tr><td><code>evaluation_modes</code></td><td><code>array</code></td><td>The modes the CC rule can be evaluated in. The valid values are distinct objects. By default, the value is Detective evaluation mode only.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>config_rule</code> resource, the following permissions are required:

### Read
<pre>
config:DescribeConfigRules,
config:DescribeComplianceByConfigRule</pre>

### Delete
<pre>
config:DeleteConfigRule,
config:DescribeConfigRules</pre>

### Update
<pre>
config:PutConfigRule,
config:DescribeConfigRules</pre>


## Example
```sql
SELECT
region,
config_rule_id,
description,
scope,
config_rule_name,
arn,
compliance,
maximum_execution_frequency,
source,
input_parameters,
evaluation_modes
FROM awscc.config.config_rule
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ConfigRuleName&gt;'
```
