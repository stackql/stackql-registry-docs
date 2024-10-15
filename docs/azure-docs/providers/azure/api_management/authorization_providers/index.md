---
title: authorization_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_providers
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

Creates, updates, deletes, gets or lists a <code>authorization_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorization_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.authorization_providers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_authorization_providers', value: 'view', },
        { label: 'authorization_providers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authorizationProviderId" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity_provider" /> | `text` | field from the `properties` object |
| <CopyableCode code="oauth2" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Authorization Provider details. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the authorization provider specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of authorization providers defined within a service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates authorization provider. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Deletes specific authorization provider from the API Management service instance. |

## `SELECT` examples

Lists a collection of authorization providers defined within a service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_authorization_providers', value: 'view', },
        { label: 'authorization_providers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
authorizationProviderId,
display_name,
identity_provider,
oauth2,
resourceGroupName,
serviceName,
subscriptionId
FROM azure.api_management.vw_authorization_providers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.authorization_providers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>authorization_providers</code> resource.

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
INSERT INTO azure.api_management.authorization_providers (
authorizationProviderId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ authorizationProviderId }}',
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
        - name: displayName
          value: string
        - name: identityProvider
          value: string
        - name: oauth2
          value:
            - name: redirectUrl
              value: string
            - name: grantTypes
              value:
                - name: authorizationCode
                  value: object
                - name: clientCredentials
                  value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>authorization_providers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.authorization_providers
WHERE If-Match = '{{ If-Match }}'
AND authorizationProviderId = '{{ authorizationProviderId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
