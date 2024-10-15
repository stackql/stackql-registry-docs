---
title: managed_hsms
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_hsms
  - key_vault
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

Creates, updates, deletes, gets or lists a <code>managed_hsms</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_hsms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.managed_hsms" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_hsms', value: 'view', },
        { label: 'managed_hsms', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The Azure Resource Manager resource ID for the managed HSM Pool. |
| <CopyableCode code="name" /> | `text` | The name of the managed HSM Pool. |
| <CopyableCode code="create_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_purge_protection" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_soft_delete" /> | `text` | field from the `properties` object |
| <CopyableCode code="hsm_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="initial_admin_object_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The supported Azure location where the managed HSM Pool should be created. |
| <CopyableCode code="network_acls" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="regions" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduled_purge_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_domain_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | SKU details |
| <CopyableCode code="soft_delete_retention_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type of the managed HSM Pool. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Azure Resource Manager resource ID for the managed HSM Pool. |
| <CopyableCode code="name" /> | `string` | The name of the managed HSM Pool. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The supported Azure location where the managed HSM Pool should be created. |
| <CopyableCode code="properties" /> | `object` | Properties of the managed HSM Pool |
| <CopyableCode code="sku" /> | `object` | SKU details |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the key vault resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | The resource type of the managed HSM Pool. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Gets the specified managed HSM Pool. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The List operation gets information about the managed HSM Pools associated with the subscription and within the specified resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The List operation gets information about the managed HSM Pools associated with the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Create or update a managed HSM Pool in the specified subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Deletes the specified managed HSM Pool. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Update a managed HSM Pool in the specified subscription. |
| <CopyableCode code="check_mhsm_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name" /> | Checks that the managed hsm name is valid and is not already in use. |
| <CopyableCode code="purge_deleted" /> | `EXEC` | <CopyableCode code="location, name, subscriptionId" /> | Permanently deletes the specified managed HSM. |

## `SELECT` examples

The List operation gets information about the managed HSM Pools associated with the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_hsms', value: 'view', },
        { label: 'managed_hsms', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
create_mode,
enable_purge_protection,
enable_soft_delete,
hsm_uri,
identity,
initial_admin_object_ids,
location,
network_acls,
private_endpoint_connections,
provisioning_state,
public_network_access,
regions,
resourceGroupName,
scheduled_purge_date,
security_domain_properties,
sku,
soft_delete_retention_in_days,
status_message,
subscriptionId,
system_data,
tags,
tenant_id,
type
FROM azure.key_vault.vw_managed_hsms
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
location,
properties,
sku,
systemData,
tags,
type
FROM azure.key_vault.managed_hsms
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_hsms</code> resource.

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
INSERT INTO azure.key_vault.managed_hsms (
name,
resourceGroupName,
subscriptionId,
properties,
location,
sku,
tags,
systemData,
identity
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ location }}',
'{{ sku }}',
'{{ tags }}',
'{{ systemData }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: tenantId
          value: string
        - name: initialAdminObjectIds
          value:
            - string
        - name: hsmUri
          value: string
        - name: enableSoftDelete
          value: boolean
        - name: softDeleteRetentionInDays
          value: integer
        - name: enablePurgeProtection
          value: boolean
        - name: createMode
          value: string
        - name: statusMessage
          value: string
        - name: provisioningState
          value: string
        - name: networkAcls
          value:
            - name: bypass
              value: string
            - name: defaultAction
              value: string
            - name: ipRules
              value:
                - - name: value
                    value: string
            - name: virtualNetworkRules
              value:
                - - name: id
                    value: string
        - name: regions
          value:
            - - name: name
                value: string
              - name: provisioningState
                value: []
              - name: isPrimary
                value: boolean
        - name: privateEndpointConnections
          value:
            - - name: id
                value: string
              - name: etag
                value: string
              - name: properties
                value:
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: []
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: provisioningState
                    value: []
        - name: publicNetworkAccess
          value: string
        - name: scheduledPurgeDate
          value: string
        - name: securityDomainProperties
          value:
            - name: activationStatus
              value: string
            - name: activationStatusMessage
              value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: sku
      value:
        - name: family
          value: string
        - name: name
          value: string
    - name: tags
      value: object
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: []
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedAt
          value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>managed_hsms</code> resource.

```sql
/*+ update */
UPDATE azure.key_vault.managed_hsms
SET 
properties = '{{ properties }}',
location = '{{ location }}',
sku = '{{ sku }}',
tags = '{{ tags }}',
systemData = '{{ systemData }}',
identity = '{{ identity }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>managed_hsms</code> resource.

```sql
/*+ delete */
DELETE FROM azure.key_vault.managed_hsms
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
