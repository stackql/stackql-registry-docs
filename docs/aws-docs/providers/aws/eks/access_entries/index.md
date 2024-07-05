---
title: access_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - access_entries
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

Creates, updates, deletes or gets an <code>access_entry</code> resource or lists <code>access_entries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An object representing an Amazon EKS AccessEntry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.access_entries" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>The cluster that the access entry is created for.</td></tr>
<tr><td><CopyableCode code="principal_arn" /></td><td><code>string</code></td><td>The principal ARN that the access entry is created for.</td></tr>
<tr><td><CopyableCode code="username" /></td><td><code>string</code></td><td>The Kubernetes user that the access entry is associated with.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="access_entry_arn" /></td><td><code>string</code></td><td>The ARN of the access entry.</td></tr>
<tr><td><CopyableCode code="kubernetes_groups" /></td><td><code>array</code></td><td>The Kubernetes groups that the access entry is associated with.</td></tr>
<tr><td><CopyableCode code="access_policies" /></td><td><code>array</code></td><td>An array of access policies that are associated with the access entry.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The node type to associate with the access entry.</td></tr>
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
    <td><CopyableCode code="PrincipalArn, ClusterName, region" /></td>
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
Gets all <code>access_entries</code> in a region.
```sql
SELECT
region,
cluster_name,
principal_arn,
username,
tags,
access_entry_arn,
kubernetes_groups,
access_policies,
type
FROM aws.eks.access_entries
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>access_entry</code>.
```sql
SELECT
region,
cluster_name,
principal_arn,
username,
tags,
access_entry_arn,
kubernetes_groups,
access_policies,
type
FROM aws.eks.access_entries
WHERE region = 'us-east-1' AND data__Identifier = '<PrincipalArn>|<ClusterName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_entry</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.eks.access_entries (
 ClusterName,
 PrincipalArn,
 region
)
SELECT 
'{{ ClusterName }}',
 '{{ PrincipalArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.eks.access_entries (
 ClusterName,
 PrincipalArn,
 Username,
 Tags,
 KubernetesGroups,
 AccessPolicies,
 Type,
 region
)
SELECT 
 '{{ ClusterName }}',
 '{{ PrincipalArn }}',
 '{{ Username }}',
 '{{ Tags }}',
 '{{ KubernetesGroups }}',
 '{{ AccessPolicies }}',
 '{{ Type }}',
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
  - name: access_entry
    props:
      - name: ClusterName
        value: '{{ ClusterName }}'
      - name: PrincipalArn
        value: '{{ PrincipalArn }}'
      - name: Username
        value: '{{ Username }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: KubernetesGroups
        value:
          - '{{ KubernetesGroups[0] }}'
      - name: AccessPolicies
        value:
          - PolicyArn: '{{ PolicyArn }}'
            AccessScope:
              Type: '{{ Type }}'
              Namespaces:
                - '{{ Namespaces[0] }}'
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.eks.access_entries
WHERE data__Identifier = '<PrincipalArn|ClusterName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>access_entries</code> resource, the following permissions are required:

### Create
```json
eks:CreateAccessEntry,
eks:DescribeAccessEntry,
eks:AssociateAccessPolicy,
eks:TagResource,
eks:ListAssociatedAccessPolicies
```

### Read
```json
eks:DescribeAccessEntry,
eks:ListAssociatedAccessPolicies
```

### Update
```json
eks:DescribeAccessEntry,
eks:ListAssociatedAccessPolicies,
eks:UpdateAccessEntry,
eks:AssociateAccessPolicy,
eks:DisassociateAccessPolicy,
eks:TagResource,
eks:UntagResource
```

### Delete
```json
eks:DeleteAccessEntry,
eks:DescribeAccessEntry
```

### List
```json
eks:ListAccessEntries
```

