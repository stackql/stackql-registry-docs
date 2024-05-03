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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>sampling_rule</code> resource, use <code>sampling_rules</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sampling_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This schema provides construct and validation rules for AWS-XRay SamplingRule resource parameters.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.xray.sampling_rule" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="sampling_rule" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="sampling_rule_record" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="sampling_rule_update" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
sampling_rule,
sampling_rule_record,
sampling_rule_update,
rule_arn,
rule_name,
tags
FROM aws.xray.sampling_rule
WHERE data__Identifier = '<RuleARN>';
```

## Permissions

To operate on the <code>sampling_rule</code> resource, the following permissions are required:

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

