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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>sampling_rule</code> resource or lists <code>sampling_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sampling_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This schema provides construct and validation rules for AWS-XRay SamplingRule resource parameters.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.xray.sampling_rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="sampling_rule" /></td><td><code>This schema provides construct and validation rules for AWS-XRay SamplingRule resource parameters.</code></td><td></td></tr>
<tr><td><CopyableCode code="sampling_rule_record" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="sampling_rule_update" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_arn" /></td><td><code>The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_name" /></td><td><code>The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>An array of key-value pairs to apply to this resource.</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>sampling_rules</code> in a region.
```sql
SELECT
region,
rule_arn
FROM aws.xray.sampling_rules
WHERE region = 'us-east-1';
```
Gets all properties from a <code>sampling_rule</code>.
```sql
SELECT
region,
sampling_rule,
sampling_rule_record,
sampling_rule_update,
rule_arn,
rule_name,
tags
FROM aws.xray.sampling_rules
WHERE region = 'us-east-1' AND data__Identifier = '<RuleARN>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sampling_rule</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.xray.sampling_rules (
 SamplingRule,
 SamplingRuleRecord,
 SamplingRuleUpdate,
 RuleName,
 Tags,
 region
)
SELECT 
'{{ SamplingRule }}',
 '{{ SamplingRuleRecord }}',
 '{{ SamplingRuleUpdate }}',
 '{{ RuleName }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.xray.sampling_rules (
 SamplingRule,
 SamplingRuleRecord,
 SamplingRuleUpdate,
 RuleName,
 Tags,
 region
)
SELECT 
 '{{ SamplingRule }}',
 '{{ SamplingRuleRecord }}',
 '{{ SamplingRuleUpdate }}',
 '{{ RuleName }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: sampling_rule
    props:
      - name: SamplingRule
        value:
          SamplingRule: null
          SamplingRuleRecord:
            CreatedAt: '{{ CreatedAt }}'
            ModifiedAt: '{{ ModifiedAt }}'
            SamplingRule: null
          SamplingRuleUpdate:
            Attributes: {}
            FixedRate: null
            Host: '{{ Host }}'
            HTTPMethod: '{{ HTTPMethod }}'
            Priority: '{{ Priority }}'
            ReservoirSize: '{{ ReservoirSize }}'
            ResourceARN: '{{ ResourceARN }}'
            RuleARN: '{{ RuleARN }}'
            RuleName: '{{ RuleName }}'
            ServiceName: '{{ ServiceName }}'
            ServiceType: '{{ ServiceType }}'
            URLPath: '{{ URLPath }}'
          RuleName: null
          Tags:
            - Key: '{{ Key }}'
              Value: '{{ Value }}'
      - name: SamplingRuleRecord
        value: null
      - name: SamplingRuleUpdate
        value: null
      - name: RuleName
        value: null
      - name: Tags
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.xray.sampling_rules
WHERE data__Identifier = '<RuleARN>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>sampling_rules</code> resource, the following permissions are required:

### Create
```json
xray:CreateSamplingRule,
xray:TagResource
```

### Read
```json
xray:GetSamplingRules,
xray:ListTagsForResource
```

### Update
```json
xray:UpdateSamplingRule,
xray:TagResource,
xray:UntagResource,
xray:ListTagsForResource
```

### Delete
```json
xray:DeleteSamplingRule
```

### List
```json
xray:GetSamplingRules,
xray:ListTagsForResource
```

