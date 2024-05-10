---
title: network_insights_access_scope_analysis
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_access_scope_analysis
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


Gets or updates an individual <code>network_insights_access_scope_analysis</code> resource, use <code>network_insights_access_scope_analyses</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_access_scope_analysis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EC2::NetworkInsightsAccessScopeAnalysis</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.network_insights_access_scope_analysis" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="network_insights_access_scope_analysis_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="network_insights_access_scope_analysis_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="network_insights_access_scope_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_message" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="start_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="end_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="findings_found" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="analyzed_eni_count" /></td><td><code>integer</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
network_insights_access_scope_analysis_id,
network_insights_access_scope_analysis_arn,
network_insights_access_scope_id,
status,
status_message,
start_date,
end_date,
findings_found,
analyzed_eni_count,
tags
FROM aws.ec2.network_insights_access_scope_analysis
WHERE region = 'us-east-1' AND data__Identifier = '<NetworkInsightsAccessScopeAnalysisId>';
```


## Permissions

To operate on the <code>network_insights_access_scope_analysis</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeNetworkInsightsAccessScopeAnalyses
```

### Update
```json
ec2:DescribeNetworkInsightsAccessScopeAnalyses,
ec2:CreateTags,
ec2:DeleteTags
```

