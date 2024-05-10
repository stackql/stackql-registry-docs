---
title: identity_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_providers
  - workspacesweb
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


Used to retrieve a list of <code>identity_providers</code> in a region or to create or delete a <code>identity_providers</code> resource, use <code>identity_provider</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::IdentityProvider Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.identity_providers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="identity_provider_arn" /></td><td><code>string</code></td><td></td></tr>
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
identity_provider_arn
FROM aws.workspacesweb.identity_providers
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>identity_provider</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- identity_provider.iql (required properties only)
INSERT INTO aws.workspacesweb.identity_providers (
 IdentityProviderDetails,
 IdentityProviderName,
 IdentityProviderType,
 region
)
SELECT 
'{{ IdentityProviderDetails }}',
 '{{ IdentityProviderName }}',
 '{{ IdentityProviderType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- identity_provider.iql (all properties)
INSERT INTO aws.workspacesweb.identity_providers (
 IdentityProviderDetails,
 IdentityProviderName,
 IdentityProviderType,
 PortalArn,
 region
)
SELECT 
 '{{ IdentityProviderDetails }}',
 '{{ IdentityProviderName }}',
 '{{ IdentityProviderType }}',
 '{{ PortalArn }}',
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
  - name: identity_provider
    props:
      - name: IdentityProviderDetails
        value: {}
      - name: IdentityProviderName
        value: '{{ IdentityProviderName }}'
      - name: IdentityProviderType
        value: '{{ IdentityProviderType }}'
      - name: PortalArn
        value: '{{ PortalArn }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.workspacesweb.identity_providers
WHERE data__Identifier = '<IdentityProviderArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>identity_providers</code> resource, the following permissions are required:

### Create
```json
workspaces-web:CreateIdentityProvider,
workspaces-web:GetIdentityProvider,
workspaces-web:ListTagsForResource,
workspaces-web:TagResource
```

### Delete
```json
workspaces-web:GetIdentityProvider,
workspaces-web:DeleteIdentityProvider
```

### List
```json
workspaces-web:ListIdentityProviders
```

