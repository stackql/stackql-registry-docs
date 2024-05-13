---
title: pod_identity_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - pod_identity_associations
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


Used to retrieve a list of <code>pod_identity_associations</code> in a region or to create or delete a <code>pod_identity_associations</code> resource, use <code>pod_identity_association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pod_identity_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An object representing an Amazon EKS PodIdentityAssociation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.pod_identity_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="association_arn" /></td><td><code>string</code></td><td>The ARN of the pod identity association.</td></tr>
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
    <td><CopyableCode code="ClusterName, RoleArn, Namespace, ServiceAccount, region" /></td>
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
association_arn
FROM aws.eks.pod_identity_associations
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>pod_identity_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.eks.pod_identity_associations (
 ClusterName,
 RoleArn,
 Namespace,
 ServiceAccount,
 region
)
SELECT 
'{{ ClusterName }}',
 '{{ RoleArn }}',
 '{{ Namespace }}',
 '{{ ServiceAccount }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.eks.pod_identity_associations (
 ClusterName,
 RoleArn,
 Namespace,
 ServiceAccount,
 Tags,
 region
)
SELECT 
 '{{ ClusterName }}',
 '{{ RoleArn }}',
 '{{ Namespace }}',
 '{{ ServiceAccount }}',
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
  - name: pod_identity_association
    props:
      - name: ClusterName
        value: '{{ ClusterName }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Namespace
        value: '{{ Namespace }}'
      - name: ServiceAccount
        value: '{{ ServiceAccount }}'
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
DELETE FROM aws.eks.pod_identity_associations
WHERE data__Identifier = '<AssociationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>pod_identity_associations</code> resource, the following permissions are required:

### Create
```json
eks:CreatePodIdentityAssociation,
eks:DescribePodIdentityAssociation,
eks:TagResource,
iam:PassRole,
iam:GetRole
```

### Delete
```json
eks:DeletePodIdentityAssociation,
eks:DescribePodIdentityAssociation
```

### List
```json
eks:ListPodIdentityAssociations
```

