---
title: identity_provider_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_provider_configs
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

Creates, updates, deletes or gets an <code>identity_provider_config</code> resource or lists <code>identity_provider_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_provider_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An object representing an Amazon EKS IdentityProviderConfig.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.identity_provider_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>The name of the identity provider configuration.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the identity provider configuration.</td></tr>
<tr><td><CopyableCode code="identity_provider_config_name" /></td><td><code>string</code></td><td>The name of the OIDC provider configuration.</td></tr>
<tr><td><CopyableCode code="oidc" /></td><td><code>object</code></td><td>An object representing an OpenID Connect (OIDC) configuration.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="identity_provider_config_arn" /></td><td><code>string</code></td><td>The ARN of the configuration.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-identityproviderconfig.html"><code>AWS::EKS::IdentityProviderConfig</code></a>.

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
    <td><CopyableCode code="Type, ClusterName, region" /></td>
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
Gets all <code>identity_provider_configs</code> in a region.
```sql
SELECT
region,
cluster_name,
type,
identity_provider_config_name,
oidc,
tags,
identity_provider_config_arn
FROM aws.eks.identity_provider_configs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>identity_provider_config</code>.
```sql
SELECT
region,
cluster_name,
type,
identity_provider_config_name,
oidc,
tags,
identity_provider_config_arn
FROM aws.eks.identity_provider_configs
WHERE region = 'us-east-1' AND data__Identifier = '<IdentityProviderConfigName>|<ClusterName>|<Type>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>identity_provider_config</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.eks.identity_provider_configs (
 ClusterName,
 Type,
 region
)
SELECT 
'{{ ClusterName }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.eks.identity_provider_configs (
 ClusterName,
 Type,
 IdentityProviderConfigName,
 Oidc,
 Tags,
 region
)
SELECT 
 '{{ ClusterName }}',
 '{{ Type }}',
 '{{ IdentityProviderConfigName }}',
 '{{ Oidc }}',
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
  - name: identity_provider_config
    props:
      - name: ClusterName
        value: '{{ ClusterName }}'
      - name: Type
        value: '{{ Type }}'
      - name: IdentityProviderConfigName
        value: '{{ IdentityProviderConfigName }}'
      - name: Oidc
        value:
          ClientId: '{{ ClientId }}'
          GroupsClaim: '{{ GroupsClaim }}'
          GroupsPrefix: '{{ GroupsPrefix }}'
          IssuerUrl: '{{ IssuerUrl }}'
          RequiredClaims:
            - Key: '{{ Key }}'
              Value: '{{ Value }}'
          UsernameClaim: '{{ UsernameClaim }}'
          UsernamePrefix: '{{ UsernamePrefix }}'
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
DELETE FROM aws.eks.identity_provider_configs
WHERE data__Identifier = '<IdentityProviderConfigName|ClusterName|Type>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>identity_provider_configs</code> resource, the following permissions are required:

### Create
```json
eks:DescribeUpdate,
eks:AssociateIdentityProviderConfig,
eks:DescribeIdentityProviderConfig,
eks:TagResource
```

### Read
```json
eks:DescribeIdentityProviderConfig
```

### Update
```json
eks:DescribeIdentityProviderConfig,
eks:TagResource,
eks:UntagResource
```

### Delete
```json
eks:DisassociateIdentityProviderConfig,
eks:DescribeIdentityProviderConfig
```

### List
```json
eks:ListIdentityProviderConfigs
```
