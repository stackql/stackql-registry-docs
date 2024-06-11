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

Creates, updates, deletes or gets a <code>pod_identity_association</code> resource or lists <code>pod_identity_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pod_identity_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An object representing an Amazon EKS PodIdentityAssociation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.pod_identity_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>The cluster that the pod identity association is created for.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The IAM role ARN that the pod identity association is created for.</td></tr>
<tr><td><CopyableCode code="namespace" /></td><td><code>string</code></td><td>The Kubernetes namespace that the pod identity association is created for.</td></tr>
<tr><td><CopyableCode code="service_account" /></td><td><code>string</code></td><td>The Kubernetes service account that the pod identity association is created for.</td></tr>
<tr><td><CopyableCode code="association_arn" /></td><td><code>string</code></td><td>The ARN of the pod identity association.</td></tr>
<tr><td><CopyableCode code="association_id" /></td><td><code>string</code></td><td>The ID of the pod identity association.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>pod_identity_associations</code> in a region.
```sql
SELECT
region,
association_arn
FROM aws.eks.pod_identity_associations
WHERE region = 'us-east-1';
```
Gets all properties from a <code>pod_identity_association</code>.
```sql
SELECT
region,
cluster_name,
role_arn,
namespace,
service_account,
association_arn,
association_id,
tags
FROM aws.eks.pod_identity_associations
WHERE region = 'us-east-1' AND data__Identifier = '<AssociationArn>';
```


## `INSERT` example

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

## `DELETE` example

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

### Read
```json
eks:DescribePodIdentityAssociation
```

### Update
```json
eks:DescribePodIdentityAssociation,
eks:UpdatePodIdentityAssociation,
eks:TagResource,
eks:UntagResource,
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

