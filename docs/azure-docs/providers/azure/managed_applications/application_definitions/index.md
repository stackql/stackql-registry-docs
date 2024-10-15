---
title: application_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - application_definitions
  - managed_applications
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

Creates, updates, deletes, gets or lists a <code>application_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_applications.application_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_definitions', value: 'view', },
        { label: 'application_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicationDefinitionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="artifacts" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorizations" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_ui_definition" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="lock_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="locking_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="main_template" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="management_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="notification_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_file_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | SKU for the resource. |
| <CopyableCode code="storage_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="managedBy" /> | `string` | ID of the resource that manages this resource. |
| <CopyableCode code="properties" /> | `object` | The managed application definition properties. |
| <CopyableCode code="sku" /> | `object` | SKU for the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationDefinitionName, resourceGroupName, subscriptionId" /> | Gets the managed application definition. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the managed application definitions in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the application definitions within a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationDefinitionName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a managed application definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationDefinitionName, resourceGroupName, subscriptionId" /> | Deletes the managed application definition. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="applicationDefinitionName, resourceGroupName, subscriptionId" /> | Updates the managed application definition. |

## `SELECT` examples

Lists all the application definitions within a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_definitions', value: 'view', },
        { label: 'application_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
applicationDefinitionName,
artifacts,
authorizations,
create_ui_definition,
deployment_policy,
display_name,
is_enabled,
lock_level,
locking_policy,
main_template,
managed_by,
management_policy,
notification_policy,
package_file_uri,
policies,
resourceGroupName,
sku,
storage_account_id,
subscriptionId
FROM azure.managed_applications.vw_application_definitions
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
managedBy,
properties,
sku
FROM azure.managed_applications.application_definitions
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application_definitions</code> resource.

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
INSERT INTO azure.managed_applications.application_definitions (
applicationDefinitionName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
managedBy,
sku
)
SELECT 
'{{ applicationDefinitionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ managedBy }}',
'{{ sku }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: lockLevel
          value: []
        - name: displayName
          value: string
        - name: isEnabled
          value: boolean
        - name: authorizations
          value:
            - - name: principalId
                value: string
              - name: roleDefinitionId
                value: string
        - name: artifacts
          value:
            - - name: name
                value: []
              - name: uri
                value: string
              - name: type
                value: []
        - name: description
          value: string
        - name: packageFileUri
          value: string
        - name: storageAccountId
          value: string
        - name: mainTemplate
          value: object
        - name: createUiDefinition
          value: object
        - name: notificationPolicy
          value:
            - name: notificationEndpoints
              value:
                - - name: uri
                    value: string
        - name: lockingPolicy
          value:
            - name: allowedActions
              value:
                - string
            - name: allowedDataActions
              value:
                - string
        - name: deploymentPolicy
          value:
            - name: deploymentMode
              value: []
        - name: managementPolicy
          value:
            - name: mode
              value: []
        - name: policies
          value:
            - - name: name
                value: string
              - name: policyDefinitionId
                value: string
              - name: parameters
                value: string
    - name: managedBy
      value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: model
          value: string
        - name: capacity
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>application_definitions</code> resource.

```sql
/*+ update */
UPDATE azure.managed_applications.application_definitions
SET 
tags = '{{ tags }}'
WHERE 
applicationDefinitionName = '{{ applicationDefinitionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>application_definitions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_applications.application_definitions
WHERE applicationDefinitionName = '{{ applicationDefinitionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
