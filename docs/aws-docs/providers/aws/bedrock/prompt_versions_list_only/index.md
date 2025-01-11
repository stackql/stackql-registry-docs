---
title: prompt_versions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - prompt_versions_list_only
  - bedrock
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

Lists <code>prompt_versions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/prompt_versions/"><code>prompt_versions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prompt_versions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::PromptVersion Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.prompt_versions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN of a prompt version resource</td></tr>
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
Lists all <code>prompt_versions</code> in a region.
```sql
SELECT
region,
arn
FROM aws.bedrock.prompt_versions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>prompt_versions_list_only</code> resource, see <a href="/providers/aws/bedrock/prompt_versions/#permissions"><code>prompt_versions</code></a>

