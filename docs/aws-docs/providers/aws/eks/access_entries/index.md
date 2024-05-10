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


Used to retrieve a list of <code>access_entries</code> in a region or to create or delete a <code>access_entries</code> resource, use <code>access_entry</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An object representing an Amazon EKS AccessEntry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.access_entries" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="principal_arn" /></td><td><code>string</code></td><td>The principal ARN that the access entry is created for.</td></tr>
<tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>The cluster that the access entry is created for.</td></tr>
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
principal_arn,
cluster_name
FROM aws.eks.access_entries
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>access_entry</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- access_entry.iql (required properties only)
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
-- access_entry.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
eks:DeleteAccessEntry,
eks:DescribeAccessEntry
```

### List
```json
eks:ListAccessEntries
```

