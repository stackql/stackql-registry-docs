---
title: network_insights_analyses
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_analyses
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

Creates, updates, deletes or gets a <code>network_insights_analysis</code> resource or lists <code>network_insights_analyses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_analyses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EC2::NetworkInsightsAnalysis</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.network_insights_analyses" /></td></tr>
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
    <td><CopyableCode code="NetworkInsightsPathId, region" /></td>
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
Gets all <code>network_insights_analyses</code> in a region.
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
tags
FROM aws.ec2.network_insights_analyses
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>network_insights_analysis</code>.
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
tags
FROM aws.ec2.network_insights_analyses
WHERE region = 'us-east-1' AND data__Identifier = '<NetworkInsightsAnalysisId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_insights_analysis</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.network_insights_analyses (
 NetworkInsightsPathId,
 region
)
SELECT 
'{{ NetworkInsightsPathId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.network_insights_analyses (
 NetworkInsightsPathId,
 FilterInArns,
 AdditionalAccounts,
 Tags,
 region
)
SELECT 
 '{{ NetworkInsightsPathId }}',
 '{{ FilterInArns }}',
 '{{ AdditionalAccounts }}',
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
  - name: network_insights_analysis
    props:
      - name: NetworkInsightsPathId
        value: '{{ NetworkInsightsPathId }}'
      - name: FilterInArns
        value:
          - '{{ FilterInArns[0] }}'
      - name: AdditionalAccounts
        value:
          - '{{ AdditionalAccounts[0] }}'
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
DELETE FROM aws.ec2.network_insights_analyses
WHERE data__Identifier = '<NetworkInsightsAnalysisId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>network_insights_analyses</code> resource, the following permissions are required:

### Read
```json
ec2:Describe*
```

### Create
```json
ec2:CreateTags,
ec2:StartNetworkInsightsAnalysis,
ec2:GetTransitGatewayRouteTablePropagations,
ec2:SearchTransitGatewayRoutes,
ec2:Describe*,
ec2:GetManagedPrefixListEntries,
elasticloadbalancing:Describe*,
directconnect:Describe*,
tiros:CreateQuery,
tiros:GetQueryAnswer,
tiros:GetQueryExplanation
```

### Update
```json
ec2:CreateTags,
ec2:Describe*,
ec2:DeleteTags
```

### List
```json
ec2:Describe*
```

### Delete
```json
ec2:DeleteNetworkInsightsAnalysis,
ec2:DeleteTags
```

