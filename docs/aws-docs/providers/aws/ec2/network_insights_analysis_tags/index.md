---
title: network_insights_analysis_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_analysis_tags
  - ec2
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

Expands all tag keys and values for <code>network_insights_analyses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_analysis_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EC2::NetworkInsightsAnalysis</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.network_insights_analysis_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="return_path_components" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="network_insights_analysis_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="network_insights_path_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="network_path_found" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="suggested_accounts" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="filter_in_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="network_insights_analysis_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_message" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="start_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="alternate_path_hints" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="explanations" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="forward_path_components" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="additional_accounts" /></td><td><code>array</code></td><td></td></tr>
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
Expands tags for all <code>network_insights_analyses</code> in a region.
```sql
SELECT
region,
status,
return_path_components,
network_insights_analysis_id,
network_insights_path_id,
network_path_found,
suggested_accounts,
filter_in_arns,
network_insights_analysis_arn,
status_message,
start_date,
alternate_path_hints,
explanations,
forward_path_components,
additional_accounts,
tag_key,
tag_value
FROM aws.ec2.network_insights_analysis_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>network_insights_analysis_tags</code> resource, see <a href="/providers/aws/ec2/network_insights_analyses/#permissions"><code>network_insights_analyses</code></a>


