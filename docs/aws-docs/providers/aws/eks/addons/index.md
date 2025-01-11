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

Creates, updates, deletes or gets an <code>addon</code> resource or lists <code>addons</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>addons</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::EKS::Addon</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.addons" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>Name of Cluster</td></tr>
<tr><td><CopyableCode code="addon_name" /></td><td><code>string</code></td><td>Name of Addon</td></tr>
<tr><td><CopyableCode code="addon_version" /></td><td><code>string</code></td><td>Version of Addon</td></tr>
<tr><td><CopyableCode code="preserve_on_delete" /></td><td><code>boolean</code></td><td>PreserveOnDelete parameter value</td></tr>
<tr><td><CopyableCode code="resolve_conflicts" /></td><td><code>string</code></td><td>Resolve parameter value conflicts</td></tr>
<tr><td><CopyableCode code="service_account_role_arn" /></td><td><code>string</code></td><td>IAM role to bind to the add-on's service account</td></tr>
<tr><td><CopyableCode code="pod_identity_associations" /></td><td><code>array</code></td><td>An array of pod identities to apply to this add-on.</td></tr>
<tr><td><CopyableCode code="configuration_values" /></td><td><code>string</code></td><td>The configuration values to use with the add-on</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the add-on</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html"><code>AWS::EKS::Addon</code></a>.

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
Gets all <code>addons</code> in a region.
```sql
SELECT
region,
cluster_name,
addon_name,
addon_version,
preserve_on_delete,
resolve_conflicts,
service_account_role_arn,
pod_identity_associations,
configuration_values,
arn,
tags
FROM aws.eks.addons
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>addon</code>.
```sql
SELECT
region,
cluster_name,
addon_name,
addon_version,
preserve_on_delete,
resolve_conflicts,
service_account_role_arn,
pod_identity_associations,
configuration_values,
arn,
tags
FROM aws.eks.addons
WHERE region = 'us-east-1' AND data__Identifier = '<ClusterName>|<AddonName>';
```

## `INSERT` example

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
 PodIdentityAssociations,
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
 '{{ PodIdentityAssociations }}',
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
      - name: PodIdentityAssociations
        value:
          - ClusterName: '{{ ClusterName }}'
            RoleArn: '{{ RoleArn }}'
            Namespace: '{{ Namespace }}'
            ServiceAccount: '{{ ServiceAccount }}'
            Tags:
              - Key: '{{ Key }}'
                Value: '{{ Value }}'
      - name: ConfigurationValues
        value: '{{ ConfigurationValues }}'
      - name: Tags
        value:
          - null

```
</TabItem>
</Tabs>

## `DELETE` example

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
iam:PassRole,
iam:GetRole,
eks:CreatePodIdentityAssociation
```

### Read
```json
eks:DescribeAddon
```

### Delete
```json
eks:DeleteAddon,
eks:DescribeAddon,
eks:DeletePodIdentityAssociation
```

### List
```json
eks:ListAddons
```

### Update
```json
iam:PassRole,
iam:GetRole,
eks:UpdateAddon,
eks:DescribeAddon,
eks:DescribeUpdate,
eks:ListTagsForResource,
eks:TagResource,
eks:UntagResource,
eks:CreatePodIdentityAssociation,
eks:DeletePodIdentityAssociation
```
