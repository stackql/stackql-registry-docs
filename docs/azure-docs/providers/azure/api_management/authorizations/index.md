---
title: authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - authorizations
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

Creates, updates, deletes, gets or lists a <code>authorizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.authorizations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_authorizations', value: 'view', },
        { label: 'authorizations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authorizationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorizationProviderId" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorization_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="oauth2grant_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Authorization details. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the authorization specified by its identifier. |
| <CopyableCode code="list_by_authorization_provider" /> | `SELECT` | <CopyableCode code="authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of authorization providers defined within a authorization provider. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates authorization. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Deletes specific Authorization from the Authorization provider. |
| <CopyableCode code="confirm_consent_code" /> | `EXEC` | <CopyableCode code="authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Confirm valid consent code to suppress Authorizations anti-phishing page. |

## `SELECT` examples

Lists a collection of authorization providers defined within a authorization provider.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_authorizations', value: 'view', },
        { label: 'authorizations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
authorizationId,
authorizationProviderId,
authorization_type,
error,
oauth2grant_type,
parameters,
resourceGroupName,
serviceName,
status,
subscriptionId
FROM azure.api_management.vw_authorizations
WHERE authorizationProviderId = '{{ authorizationProviderId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.authorizations
WHERE authorizationProviderId = '{{ authorizationProviderId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>authorizations</code> resource.

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
INSERT INTO azure.api_management.authorizations (
authorizationId,
authorizationProviderId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ authorizationId }}',
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
        - name: authorizationType
          value: string
        - name: oauth2grantType
          value: string
        - name: parameters
          value: object
        - name: error
          value:
            - name: code
              value: string
            - name: message
              value: string
        - name: status
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>authorizations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.authorizations
WHERE If-Match = '{{ If-Match }}'
AND authorizationId = '{{ authorizationId }}'
AND authorizationProviderId = '{{ authorizationProviderId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
