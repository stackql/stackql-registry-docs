---
title: network_insights_paths
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_paths
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


Used to retrieve a list of <code>network_insights_paths</code> in a region or to create or delete a <code>network_insights_paths</code> resource, use <code>network_insights_path</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_paths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EC2::NetworkInsightsPath</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.network_insights_paths" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="network_insights_path_id" /></td><td><code>string</code></td><td></td></tr>
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
network_insights_path_id
FROM aws.ec2.network_insights_paths
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>network_insights_path</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- network_insights_path.iql (required properties only)
INSERT INTO aws.ec2.network_insights_paths (
 Source,
 Protocol,
 region
)
SELECT 
'{{ Source }}',
 '{{ Protocol }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- network_insights_path.iql (all properties)
INSERT INTO aws.ec2.network_insights_paths (
 SourceIp,
 FilterAtSource,
 FilterAtDestination,
 DestinationIp,
 Source,
 Destination,
 Protocol,
 DestinationPort,
 Tags,
 region
)
SELECT 
 '{{ SourceIp }}',
 '{{ FilterAtSource }}',
 '{{ FilterAtDestination }}',
 '{{ DestinationIp }}',
 '{{ Source }}',
 '{{ Destination }}',
 '{{ Protocol }}',
 '{{ DestinationPort }}',
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
  - name: network_insights_path
    props:
      - name: SourceIp
        value: '{{ SourceIp }}'
      - name: FilterAtSource
        value:
          SourceAddress: null
          SourcePortRange:
            FromPort: '{{ FromPort }}'
            ToPort: '{{ ToPort }}'
          DestinationAddress: null
          DestinationPortRange: null
      - name: FilterAtDestination
        value: null
      - name: DestinationIp
        value: null
      - name: Source
        value: '{{ Source }}'
      - name: Destination
        value: '{{ Destination }}'
      - name: Protocol
        value: '{{ Protocol }}'
      - name: DestinationPort
        value: '{{ DestinationPort }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.network_insights_paths
WHERE data__Identifier = '<NetworkInsightsPathId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>network_insights_paths</code> resource, the following permissions are required:

### Create
```json
ec2:CreateNetworkInsightsPath,
ec2:CreateTags
```

### Delete
```json
ec2:DeleteNetworkInsightsPath,
ec2:DeleteTags
```

### List
```json
ec2:DescribeNetworkInsightsPaths
```

