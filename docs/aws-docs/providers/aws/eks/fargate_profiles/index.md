---
title: fargate_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - fargate_profiles
  - eks
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


Used to retrieve a list of <code>fargate_profiles</code> in a region or to create or delete a <code>fargate_profiles</code> resource, use <code>fargate_profile</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fargate_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::EKS::FargateProfile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.fargate_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>Name of the Cluster</td></tr>
<tr><td><CopyableCode code="fargate_profile_name" /></td><td><code>string</code></td><td>Name of FargateProfile</td></tr>
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
    <td><CopyableCode code="ClusterName, PodExecutionRoleArn, Selectors, region" /></td>
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
cluster_name,
fargate_profile_name
FROM aws.eks.fargate_profiles
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>fargate_profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.eks.fargate_profiles (
 ClusterName,
 PodExecutionRoleArn,
 Selectors,
 region
)
SELECT 
'{{ ClusterName }}',
 '{{ PodExecutionRoleArn }}',
 '{{ Selectors }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.eks.fargate_profiles (
 ClusterName,
 FargateProfileName,
 PodExecutionRoleArn,
 Subnets,
 Selectors,
 Tags,
 region
)
SELECT 
 '{{ ClusterName }}',
 '{{ FargateProfileName }}',
 '{{ PodExecutionRoleArn }}',
 '{{ Subnets }}',
 '{{ Selectors }}',
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
  - name: fargate_profile
    props:
      - name: ClusterName
        value: '{{ ClusterName }}'
      - name: FargateProfileName
        value: '{{ FargateProfileName }}'
      - name: PodExecutionRoleArn
        value: '{{ PodExecutionRoleArn }}'
      - name: Subnets
        value:
          - '{{ Subnets[0] }}'
      - name: Selectors
        value:
          - Namespace: '{{ Namespace }}'
            Labels:
              - Key: '{{ Key }}'
                Value: '{{ Value }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.eks.fargate_profiles
WHERE data__Identifier = '<ClusterName|FargateProfileName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>fargate_profiles</code> resource, the following permissions are required:

### Create
```json
eks:CreateFargateProfile,
eks:DescribeFargateProfile,
iam:GetRole,
iam:PassRole,
iam:CreateServiceLinkedRole,
eks:TagResource
```

### Delete
```json
eks:DeleteFargateProfile,
eks:DescribeFargateProfile
```

### List
```json
eks:ListFargateProfiles
```

