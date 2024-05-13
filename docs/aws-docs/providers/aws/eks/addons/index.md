---
title: addons
hide_title: false
hide_table_of_contents: false
keywords:
  - addons
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


Used to retrieve a list of <code>addons</code> in a region or to create or delete a <code>addons</code> resource, use <code>addon</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>addons</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::EKS::Addon</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.addons" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>Name of Cluster</td></tr>
<tr><td><CopyableCode code="addon_name" /></td><td><code>string</code></td><td>Name of Addon</td></tr>
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
    <td><CopyableCode code="ClusterName, AddonName, region" /></td>
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
addon_name
FROM aws.eks.addons
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>addon</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.eks.addons (
 ClusterName,
 AddonName,
 region
)
SELECT 
'{{ ClusterName }}',
 '{{ AddonName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.eks.addons (
 ClusterName,
 AddonName,
 AddonVersion,
 PreserveOnDelete,
 ResolveConflicts,
 ServiceAccountRoleArn,
 ConfigurationValues,
 Tags,
 region
)
SELECT 
 '{{ ClusterName }}',
 '{{ AddonName }}',
 '{{ AddonVersion }}',
 '{{ PreserveOnDelete }}',
 '{{ ResolveConflicts }}',
 '{{ ServiceAccountRoleArn }}',
 '{{ ConfigurationValues }}',
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
  - name: addon
    props:
      - name: ClusterName
        value: '{{ ClusterName }}'
      - name: AddonName
        value: '{{ AddonName }}'
      - name: AddonVersion
        value: '{{ AddonVersion }}'
      - name: PreserveOnDelete
        value: '{{ PreserveOnDelete }}'
      - name: ResolveConflicts
        value: '{{ ResolveConflicts }}'
      - name: ServiceAccountRoleArn
        value: '{{ ServiceAccountRoleArn }}'
      - name: ConfigurationValues
        value: '{{ ConfigurationValues }}'
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
DELETE FROM aws.eks.addons
WHERE data__Identifier = '<ClusterName|AddonName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>addons</code> resource, the following permissions are required:

### Create
```json
eks:CreateAddon,
eks:DescribeAddon,
eks:TagResource,
iam:PassRole
```

### Delete
```json
eks:DeleteAddon,
eks:DescribeAddon
```

### List
```json
eks:ListAddons
```

