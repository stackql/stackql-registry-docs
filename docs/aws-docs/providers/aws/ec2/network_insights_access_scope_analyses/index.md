---
title: network_insights_access_scope_analyses
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_access_scope_analyses
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

Creates, updates, deletes or gets a <code>network_insights_access_scope_analysis</code> resource or lists <code>network_insights_access_scope_analyses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_access_scope_analyses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EC2::NetworkInsightsAccessScopeAnalysis</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.network_insights_access_scope_analyses" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="network_insights_access_scope_analysis_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="NetworkInsightsAccessScopeId, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>network_insights_access_scope_analyses</code> in a region.
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
FROM aws.ec2.network_insights_access_scope_analyses
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>network_insights_access_scope_analysis</code>.
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
FROM aws.ec2.network_insights_access_scope_analyses
WHERE region = 'us-east-1' AND data__Identifier = '<NetworkInsightsAccessScopeAnalysisId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_insights_access_scope_analysis</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.network_insights_access_scope_analyses (
 NetworkInsightsAccessScopeId,
 region
)
SELECT 
'{{ NetworkInsightsAccessScopeId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.network_insights_access_scope_analyses (
 NetworkInsightsAccessScopeId,
 Tags,
 region
)
SELECT 
 '{{ NetworkInsightsAccessScopeId }}',
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
  - name: network_insights_access_scope_analysis
    props:
      - name: NetworkInsightsAccessScopeId
        value: '{{ NetworkInsightsAccessScopeId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.network_insights_access_scope_analyses
WHERE data__Identifier = '<NetworkInsightsAccessScopeAnalysisId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>network_insights_access_scope_analyses</code> resource, the following permissions are required:

### Create
```json
ec2:CreateTags,
ec2:StartNetworkInsightsAccessScopeAnalysis,
ec2:GetTransitGatewayRouteTablePropagations,
ec2:Describe*,
elasticloadbalancing:Describe*,
directconnect:Describe*,
tiros:CreateQuery,
tiros:GetQueryAnswer,
tiros:GetQueryExplanation
```

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

### Delete
```json
ec2:DeleteNetworkInsightsAccessScopeAnalysis,
ec2:DeleteTags
```

### List
```json
ec2:DescribeNetworkInsightsAccessScopeAnalyses
```

