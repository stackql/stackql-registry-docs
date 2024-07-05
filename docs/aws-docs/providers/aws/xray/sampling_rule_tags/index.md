---
title: sampling_rule_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - sampling_rule_tags
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

Expands all tag keys and values for <code>sampling_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sampling_rule_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This schema provides construct and validation rules for AWS-XRay SamplingRule resource parameters.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.xray.sampling_rule_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="sampling_rule" /></td><td><code>object</code></td><td>This schema provides construct and validation rules for AWS-XRay SamplingRule resource parameters.</td></tr>
<tr><td><CopyableCode code="sampling_rule_record" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="sampling_rule_update" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_arn" /></td><td><code>string</code></td><td>The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.</td></tr>
<tr><td><CopyableCode code="rule_name" /></td><td><code>string</code></td><td>The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>sampling_rules</code> in a region.
```sql
SELECT
region,
sampling_rule,
sampling_rule_record,
sampling_rule_update,
rule_arn,
rule_name,
tag_key,
tag_value
FROM aws.xray.sampling_rule_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>sampling_rule_tags</code> resource, see <a href="/providers/aws/xray/sampling_rules/#permissions"><code>sampling_rules</code></a>


