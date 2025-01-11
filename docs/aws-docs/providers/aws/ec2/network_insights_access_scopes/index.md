---
title: network_insights_access_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_access_scopes
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

Creates, updates, deletes or gets a <code>network_insights_access_scope</code> resource or lists <code>network_insights_access_scopes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_access_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EC2::NetworkInsightsAccessScope</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.network_insights_access_scopes" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="network_insights_access_scope_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="network_insights_access_scope_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="match_paths" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="exclude_paths" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsaccessscope.html"><code>AWS::EC2::NetworkInsightsAccessScope</code></a>.

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
Gets all <code>network_insights_access_scopes</code> in a region.
```sql
SELECT
region,
network_insights_access_scope_id,
network_insights_access_scope_arn,
created_date,
updated_date,
tags,
match_paths,
exclude_paths
FROM aws.ec2.network_insights_access_scopes
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>network_insights_access_scope</code>.
```sql
SELECT
region,
network_insights_access_scope_id,
network_insights_access_scope_arn,
created_date,
updated_date,
tags,
match_paths,
exclude_paths
FROM aws.ec2.network_insights_access_scopes
WHERE region = 'us-east-1' AND data__Identifier = '<NetworkInsightsAccessScopeId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_insights_access_scope</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.network_insights_access_scopes (
 Tags,
 MatchPaths,
 ExcludePaths,
 region
)
SELECT 
'{{ Tags }}',
 '{{ MatchPaths }}',
 '{{ ExcludePaths }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.network_insights_access_scopes (
 Tags,
 MatchPaths,
 ExcludePaths,
 region
)
SELECT 
 '{{ Tags }}',
 '{{ MatchPaths }}',
 '{{ ExcludePaths }}',
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
  - name: network_insights_access_scope
    props:
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: MatchPaths
        value:
          - Source:
              PacketHeaderStatement:
                SourceAddresses:
                  - '{{ SourceAddresses[0] }}'
                DestinationAddresses:
                  - '{{ DestinationAddresses[0] }}'
                SourcePorts:
                  - '{{ SourcePorts[0] }}'
                DestinationPorts:
                  - '{{ DestinationPorts[0] }}'
                SourcePrefixLists:
                  - '{{ SourcePrefixLists[0] }}'
                DestinationPrefixLists:
                  - '{{ DestinationPrefixLists[0] }}'
                Protocols:
                  - '{{ Protocols[0] }}'
              ResourceStatement:
                Resources:
                  - '{{ Resources[0] }}'
                ResourceTypes:
                  - '{{ ResourceTypes[0] }}'
            Destination: null
            ThroughResources:
              - ResourceStatement: null
      - name: ExcludePaths
        value:
          - null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.network_insights_access_scopes
WHERE data__Identifier = '<NetworkInsightsAccessScopeId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>network_insights_access_scopes</code> resource, the following permissions are required:

### Create
```json
ec2:CreateNetworkInsightsAccessScope,
ec2:CreateTags,
tiros:CreateQuery
```

### Read
```json
ec2:DescribeNetworkInsightsAccessScopes,
ec2:GetNetworkInsightsAccessScopeContent
```

### Update
```json
ec2:DescribeNetworkInsightsAccessScopes,
ec2:GetNetworkInsightsAccessScopeContent,
ec2:CreateTags,
ec2:DeleteTags
```

### Delete
```json
ec2:DeleteNetworkInsightsAccessScope,
ec2:DeleteTags
```

### List
```json
ec2:DescribeNetworkInsightsAccessScopes
```
