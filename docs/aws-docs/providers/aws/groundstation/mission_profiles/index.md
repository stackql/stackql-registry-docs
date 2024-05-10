---
title: mission_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - mission_profiles
  - groundstation
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


Used to retrieve a list of <code>mission_profiles</code> in a region or to create or delete a <code>mission_profiles</code> resource, use <code>mission_profile</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mission_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Ground Station Mission Profile resource type for CloudFormation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.groundstation.mission_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
id,
arn
FROM aws.groundstation.mission_profiles
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>mission_profile</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- mission_profile.iql (required properties only)
INSERT INTO aws.groundstation.mission_profiles (
 Name,
 MinimumViableContactDurationSeconds,
 DataflowEdges,
 TrackingConfigArn,
 region
)
SELECT 
'{{ Name }}',
 '{{ MinimumViableContactDurationSeconds }}',
 '{{ DataflowEdges }}',
 '{{ TrackingConfigArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- mission_profile.iql (all properties)
INSERT INTO aws.groundstation.mission_profiles (
 Name,
 ContactPrePassDurationSeconds,
 ContactPostPassDurationSeconds,
 MinimumViableContactDurationSeconds,
 StreamsKmsKey,
 StreamsKmsRole,
 DataflowEdges,
 TrackingConfigArn,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ ContactPrePassDurationSeconds }}',
 '{{ ContactPostPassDurationSeconds }}',
 '{{ MinimumViableContactDurationSeconds }}',
 '{{ StreamsKmsKey }}',
 '{{ StreamsKmsRole }}',
 '{{ DataflowEdges }}',
 '{{ TrackingConfigArn }}',
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
  - name: mission_profile
    props:
      - name: Name
        value: '{{ Name }}'
      - name: ContactPrePassDurationSeconds
        value: '{{ ContactPrePassDurationSeconds }}'
      - name: ContactPostPassDurationSeconds
        value: '{{ ContactPostPassDurationSeconds }}'
      - name: MinimumViableContactDurationSeconds
        value: '{{ MinimumViableContactDurationSeconds }}'
      - name: StreamsKmsKey
        value:
          KmsKeyArn: '{{ KmsKeyArn }}'
          KmsAliasArn: '{{ KmsAliasArn }}'
      - name: StreamsKmsRole
        value: '{{ StreamsKmsRole }}'
      - name: DataflowEdges
        value:
          - Source: '{{ Source }}'
            Destination: '{{ Destination }}'
      - name: TrackingConfigArn
        value: '{{ TrackingConfigArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.groundstation.mission_profiles
WHERE data__Identifier = '<Id|Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>mission_profiles</code> resource, the following permissions are required:

### Create
```json
groundstation:CreateMissionProfile,
groundstation:GetMissionProfile,
groundstation:TagResource,
iam:PassRole,
kms:DescribeKey,
kms:CreateGrant
```

### Delete
```json
groundstation:DeleteMissionProfile,
groundstation:GetMissionProfile
```

### List
```json
groundstation:ListMissionProfiles
```

