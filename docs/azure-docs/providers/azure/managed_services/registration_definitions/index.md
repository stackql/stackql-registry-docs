---
title: registration_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - registration_definitions
  - managed_services
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

Creates, updates, deletes, gets or lists a <code>registration_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registration_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_services.registration_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registration_definitions', value: 'view', },
        { label: 'registration_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The fully qualified path of the registration definition. |
| <CopyableCode code="name" /> | `text` | The name of the registration definition. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorizations" /> | `text` | field from the `properties` object |
| <CopyableCode code="eligible_authorizations" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_by_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_by_tenant_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="managee_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="managee_tenant_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan" /> | `text` | Plan for the resource. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registrationDefinitionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_definition_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the Azure resource (Microsoft.ManagedServices/registrationDefinitions). |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified path of the registration definition. |
| <CopyableCode code="name" /> | `string` | The name of the registration definition. |
| <CopyableCode code="plan" /> | `object` | Plan for the resource. |
| <CopyableCode code="properties" /> | `object` | The properties of a registration definition. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the Azure resource (Microsoft.ManagedServices/registrationDefinitions). |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registrationDefinitionId, scope" /> | Gets the registration definition details. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Gets a list of the registration definitions. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="registrationDefinitionId, scope" /> | Creates or updates a registration definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="registrationDefinitionId, scope" /> | Deletes the registration definition. |

## `SELECT` examples

Gets a list of the registration definitions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registration_definitions', value: 'view', },
        { label: 'registration_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
authorizations,
eligible_authorizations,
managed_by_tenant_id,
managed_by_tenant_name,
managee_tenant_id,
managee_tenant_name,
plan,
provisioning_state,
registrationDefinitionId,
registration_definition_name,
scope,
system_data,
type
FROM azure.managed_services.vw_registration_definitions
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
plan,
properties,
systemData,
type
FROM azure.managed_services.registration_definitions
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>registration_definitions</code> resource.

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
INSERT INTO azure.managed_services.registration_definitions (
registrationDefinitionId,
scope,
properties,
plan
)
SELECT 
'{{ registrationDefinitionId }}',
'{{ scope }}',
'{{ properties }}',
'{{ plan }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: description
          value: string
        - name: authorizations
          value:
            - - name: principalId
                value: string
              - name: principalIdDisplayName
                value: string
              - name: roleDefinitionId
                value: string
              - name: delegatedRoleDefinitionIds
                value:
                  - string
        - name: eligibleAuthorizations
          value:
            - - name: principalId
                value: string
              - name: principalIdDisplayName
                value: string
              - name: roleDefinitionId
                value: string
              - name: justInTimeAccessPolicy
                value:
                  - name: multiFactorAuthProvider
                    value: string
                  - name: maximumActivationDuration
                    value: string
                  - name: managedByTenantApprovers
                    value:
                      - - name: principalId
                          value: string
                        - name: principalIdDisplayName
                          value: string
        - name: registrationDefinitionName
          value: string
        - name: managedByTenantId
          value: string
        - name: provisioningState
          value: string
        - name: manageeTenantId
          value: string
        - name: manageeTenantName
          value: string
        - name: managedByTenantName
          value: string
    - name: plan
      value:
        - name: name
          value: string
        - name: publisher
          value: string
        - name: product
          value: string
        - name: promotionCode
          value: string
        - name: version
          value: string
    - name: id
      value: string
    - name: type
      value: string
    - name: name
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>registration_definitions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_services.registration_definitions
WHERE registrationDefinitionId = '{{ registrationDefinitionId }}'
AND scope = '{{ scope }}';
```
