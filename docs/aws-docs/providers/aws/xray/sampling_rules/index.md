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


Used to retrieve a list of <code>sampling_rules</code> in a region or to create or delete a <code>sampling_rules</code> resource, use <code>sampling_rule</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sampling_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This schema provides construct and validation rules for AWS-XRay SamplingRule resource parameters.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.xray.sampling_rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="rule_arn" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
rule_arn
FROM aws.xray.sampling_rules
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "SamplingRule": {
  "SamplingRule": null,
  "SamplingRuleRecord": {
   "CreatedAt": "{{ CreatedAt }}",
   "ModifiedAt": "{{ ModifiedAt }}",
   "SamplingRule": null
  },
  "SamplingRuleUpdate": {
   "Attributes": {},
   "FixedRate": null,
   "Host": "{{ Host }}",
   "HTTPMethod": "{{ HTTPMethod }}",
   "Priority": "{{ Priority }}",
   "ReservoirSize": "{{ ReservoirSize }}",
   "ResourceARN": "{{ ResourceARN }}",
   "RuleARN": "{{ RuleARN }}",
   "RuleName": "{{ RuleName }}",
   "ServiceName": "{{ ServiceName }}",
   "ServiceType": "{{ ServiceType }}",
   "URLPath": "{{ URLPath }}"
  },
  "RuleName": null,
  "Tags": [
   {
    "Key": "{{ Key }}",
    "Value": "{{ Value }}"
   }
  ]
 },
 "SamplingRuleRecord": null,
 "SamplingRuleUpdate": null,
 "RuleName": null,
 "Tags": null
}
>>>
--required properties only
INSERT INTO aws.xray.sampling_rules (
 SamplingRule,
 SamplingRuleRecord,
 SamplingRuleUpdate,
 RuleName,
 Tags,
 region
)
SELECT 
{{ .SamplingRule }},
 {{ .SamplingRuleRecord }},
 {{ .SamplingRuleUpdate }},
 {{ .RuleName }},
 {{ .Tags }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "SamplingRule": {
  "SamplingRule": null,
  "SamplingRuleRecord": {
   "CreatedAt": "{{ CreatedAt }}",
   "ModifiedAt": "{{ ModifiedAt }}",
   "SamplingRule": null
  },
  "SamplingRuleUpdate": {
   "Attributes": {},
   "FixedRate": null,
   "Host": "{{ Host }}",
   "HTTPMethod": "{{ HTTPMethod }}",
   "Priority": "{{ Priority }}",
   "ReservoirSize": "{{ ReservoirSize }}",
   "ResourceARN": "{{ ResourceARN }}",
   "RuleARN": "{{ RuleARN }}",
   "RuleName": "{{ RuleName }}",
   "ServiceName": "{{ ServiceName }}",
   "ServiceType": "{{ ServiceType }}",
   "URLPath": "{{ URLPath }}"
  },
  "RuleName": null,
  "Tags": [
   {
    "Key": "{{ Key }}",
    "Value": "{{ Value }}"
   }
  ]
 },
 "SamplingRuleRecord": null,
 "SamplingRuleUpdate": null,
 "RuleName": null,
 "Tags": null
}
>>>
--all properties
INSERT INTO aws.xray.sampling_rules (
 SamplingRule,
 SamplingRuleRecord,
 SamplingRuleUpdate,
 RuleName,
 Tags,
 region
)
SELECT 
 {{ .SamplingRule }},
 {{ .SamplingRuleRecord }},
 {{ .SamplingRuleUpdate }},
 {{ .RuleName }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
xray:DeleteSamplingRule
```

### List
```json
xray:GetSamplingRules,
xray:ListTagsForResource
```

