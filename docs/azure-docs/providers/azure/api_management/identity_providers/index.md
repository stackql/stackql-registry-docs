---
title: identity_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_providers
  - api_management
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>identity_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.identity_providers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_identity_providers', value: 'view', },
        { label: 'identity_providers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allowed_tenants" /> | `text` | field from the `properties` object |
| <CopyableCode code="authority" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_library" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_secret" /> | `text` | field from the `properties` object |
| <CopyableCode code="identityProviderName" /> | `text` | field from the `properties` object |
| <CopyableCode code="password_reset_policy_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="profile_editing_policy_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="signin_policy_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="signin_tenant" /> | `text` | field from the `properties` object |
| <CopyableCode code="signup_policy_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The external Identity Providers like Facebook, Google, Microsoft, Twitter or Azure Active Directory which can be used to enable access to the API Management service developer portal for all users. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="identityProviderName, resourceGroupName, serviceName, subscriptionId" /> | Gets the configuration details of the identity Provider configured in specified service instance. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of Identity Provider configured in the specified service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="identityProviderName, resourceGroupName, serviceName, subscriptionId" /> | Creates or Updates the IdentityProvider configuration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, identityProviderName, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified identity provider configuration. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, identityProviderName, resourceGroupName, serviceName, subscriptionId" /> | Updates an existing IdentityProvider configuration. |

## `SELECT` examples

Lists a collection of Identity Provider configured in the specified service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_identity_providers', value: 'view', },
        { label: 'identity_providers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
allowed_tenants,
authority,
client_id,
client_library,
client_secret,
identityProviderName,
password_reset_policy_name,
profile_editing_policy_name,
resourceGroupName,
serviceName,
signin_policy_name,
signin_tenant,
signup_policy_name,
subscriptionId,
type
FROM azure.api_management.vw_identity_providers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.identity_providers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>identity_providers</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.api_management.identity_providers (
identityProviderName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ identityProviderName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: clientId
          value: string
        - name: clientSecret
          value: string
        - name: type
          value: string
        - name: signinTenant
          value: string
        - name: allowedTenants
          value:
            - string
        - name: authority
          value: string
        - name: signupPolicyName
          value: string
        - name: signinPolicyName
          value: string
        - name: profileEditingPolicyName
          value: string
        - name: passwordResetPolicyName
          value: string
        - name: clientLibrary
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>identity_providers</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.identity_providers
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND identityProviderName = '{{ identityProviderName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>identity_providers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.identity_providers
WHERE If-Match = '{{ If-Match }}'
AND identityProviderName = '{{ identityProviderName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
