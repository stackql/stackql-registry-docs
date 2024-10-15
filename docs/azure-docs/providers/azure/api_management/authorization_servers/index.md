---
title: authorization_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_servers
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

Creates, updates, deletes, gets or lists a <code>authorization_servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorization_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.authorization_servers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_authorization_servers', value: 'view', },
        { label: 'authorization_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorization_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorization_methods" /> | `text` | field from the `properties` object |
| <CopyableCode code="authsid" /> | `text` | field from the `properties` object |
| <CopyableCode code="bearer_token_sending_methods" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_authentication_method" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_registration_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_secret" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="grant_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_owner_password" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_owner_username" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="support_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="token_body_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="token_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_in_api_documentation" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_in_test_console" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | External OAuth authorization server settings Properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authsid, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the authorization server specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of authorization servers defined within a service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authsid, resourceGroupName, serviceName, subscriptionId" /> | Creates new authorization server or updates an existing authorization server. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, authsid, resourceGroupName, serviceName, subscriptionId" /> | Deletes specific authorization server instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, authsid, resourceGroupName, serviceName, subscriptionId" /> | Updates the details of the authorization server specified by its identifier. |

## `SELECT` examples

Lists a collection of authorization servers defined within a service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_authorization_servers', value: 'view', },
        { label: 'authorization_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
authorization_endpoint,
authorization_methods,
authsid,
bearer_token_sending_methods,
client_authentication_method,
client_id,
client_registration_endpoint,
client_secret,
default_scope,
display_name,
grant_types,
resourceGroupName,
resource_owner_password,
resource_owner_username,
serviceName,
subscriptionId,
support_state,
token_body_parameters,
token_endpoint,
use_in_api_documentation,
use_in_test_console
FROM azure.api_management.vw_authorization_servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.authorization_servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>authorization_servers</code> resource.

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
INSERT INTO azure.api_management.authorization_servers (
authsid,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ authsid }}',
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
        - name: useInTestConsole
          value: boolean
        - name: useInApiDocumentation
          value: boolean
        - name: clientRegistrationEndpoint
          value: string
        - name: authorizationEndpoint
          value: string
        - name: grantTypes
          value:
            - string
        - name: clientId
          value: string
        - name: clientSecret
          value: string
        - name: description
          value: string
        - name: authorizationMethods
          value:
            - string
        - name: clientAuthenticationMethod
          value:
            - string
        - name: tokenBodyParameters
          value:
            - - name: name
                value: string
              - name: value
                value: string
        - name: tokenEndpoint
          value: string
        - name: supportState
          value: boolean
        - name: defaultScope
          value: string
        - name: bearerTokenSendingMethods
          value:
            - string
        - name: resourceOwnerUsername
          value: string
        - name: resourceOwnerPassword
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>authorization_servers</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.authorization_servers
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND authsid = '{{ authsid }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>authorization_servers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.authorization_servers
WHERE If-Match = '{{ If-Match }}'
AND authsid = '{{ authsid }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
