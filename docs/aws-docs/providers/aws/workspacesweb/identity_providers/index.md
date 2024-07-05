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

Creates, updates, deletes or gets an <code>identity_provider</code> resource or lists <code>identity_providers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::IdentityProvider Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.identity_providers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="identity_provider_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_provider_details" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_provider_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_provider_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="portal_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="IdentityProviderDetails, IdentityProviderName, IdentityProviderType, region" /></td>
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
Gets all <code>identity_providers</code> in a region.
```sql
SELECT
region,
identity_provider_arn,
identity_provider_details,
identity_provider_name,
identity_provider_type,
portal_arn
FROM aws.workspacesweb.identity_providers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>identity_provider</code>.
```sql
SELECT
region,
identity_provider_arn,
identity_provider_details,
identity_provider_name,
identity_provider_type,
portal_arn
FROM aws.workspacesweb.identity_providers
WHERE region = 'us-east-1' AND data__Identifier = '<IdentityProviderArn>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
workspaces-web:GetIdentityProvider,
workspaces-web:ListIdentityProviders,
workspaces-web:ListTagsForResource
```

### Update
```json
workspaces-web:UpdateIdentityProvider,
workspaces-web:TagResource,
workspaces-web:UntagResource,
workspaces-web:GetIdentityProvider,
workspaces-web:ListIdentityProviders,
workspaces-web:ListTagsForResource
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

