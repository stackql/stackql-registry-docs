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


Used to retrieve a list of <code>identity_provider_configs</code> in a region or to create or delete a <code>identity_provider_configs</code> resource, use <code>identity_provider_config</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_provider_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An object representing an Amazon EKS IdentityProviderConfig.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.identity_provider_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="identity_provider_config_name" /></td><td><code>string</code></td><td>The name of the OIDC provider configuration.</td></tr>
<tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>The name of the identity provider configuration.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the identity provider configuration.</td></tr>
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
identity_provider_config_name,
cluster_name,
type
FROM aws.eks.identity_provider_configs
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "ClusterName": "{{ ClusterName }}",
 "Type": "{{ Type }}"
}
>>>
--required properties only
INSERT INTO aws.eks.identity_provider_configs (
 ClusterName,
 Type,
 region
)
SELECT 
{{ .ClusterName }},
 {{ .Type }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ClusterName": "{{ ClusterName }}",
 "Type": "{{ Type }}",
 "IdentityProviderConfigName": "{{ IdentityProviderConfigName }}",
 "Oidc": {
  "ClientId": "{{ ClientId }}",
  "GroupsClaim": "{{ GroupsClaim }}",
  "GroupsPrefix": "{{ GroupsPrefix }}",
  "IssuerUrl": "{{ IssuerUrl }}",
  "RequiredClaims": [
   {
    "Key": "{{ Key }}",
    "Value": "{{ Value }}"
   }
  ],
  "UsernameClaim": "{{ UsernameClaim }}",
  "UsernamePrefix": "{{ UsernamePrefix }}"
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.eks.identity_provider_configs (
 ClusterName,
 Type,
 IdentityProviderConfigName,
 Oidc,
 Tags,
 region
)
SELECT 
 {{ .ClusterName }},
 {{ .Type }},
 {{ .IdentityProviderConfigName }},
 {{ .Oidc }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
eks:DisassociateIdentityProviderConfig,
eks:DescribeIdentityProviderConfig
```

### List
```json
eks:ListIdentityProviderConfigs
```

