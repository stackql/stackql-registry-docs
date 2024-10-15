---
title: replication_recovery_services_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_recovery_services_providers
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>replication_recovery_services_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_recovery_services_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_recovery_services_providers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_recovery_services_providers', value: 'view', },
        { label: 'replication_recovery_services_providers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="allowed_scenarios" /> | `text` | field from the `properties` object |
| <CopyableCode code="authentication_identity_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="bios_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_plane_authentication_identity_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="dra_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabric_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabric_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_error_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_heart_beat" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="machine_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="protected_item_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="providerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_version_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_version_expiry_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_version_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_access_identity_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Recovery services provider properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, providerName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of registered recovery services provider. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Lists the registered recovery services providers in the vault. |
| <CopyableCode code="list_by_replication_fabrics" /> | `SELECT` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId" /> | Lists the registered recovery services providers for the specified fabric. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fabricName, providerName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to add a recovery services provider. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fabricName, providerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to removes/delete(unregister) a recovery services provider from the vault. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="fabricName, providerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to purge(force delete) a recovery services provider from the vault. |
| <CopyableCode code="refresh_provider" /> | `EXEC` | <CopyableCode code="fabricName, providerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to refresh the information from the recovery services provider. |

## `SELECT` examples

Lists the registered recovery services providers in the vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_recovery_services_providers', value: 'view', },
        { label: 'replication_recovery_services_providers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allowed_scenarios,
authentication_identity_details,
bios_id,
connection_status,
data_plane_authentication_identity_details,
dra_identifier,
fabricName,
fabric_friendly_name,
fabric_type,
friendly_name,
health_error_details,
last_heart_beat,
location,
machine_id,
machine_name,
protected_item_count,
providerName,
provider_version,
provider_version_details,
provider_version_expiry_date,
provider_version_state,
resourceGroupName,
resourceName,
resource_access_identity_details,
server_version,
subscriptionId,
type
FROM azure.recovery_services_site_recovery.vw_replication_recovery_services_providers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure.recovery_services_site_recovery.replication_recovery_services_providers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_recovery_services_providers</code> resource.

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
INSERT INTO azure.recovery_services_site_recovery.replication_recovery_services_providers (
fabricName,
providerName,
resourceGroupName,
resourceName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ fabricName }}',
'{{ providerName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: machineName
          value: string
        - name: machineId
          value: string
        - name: biosId
          value: string
        - name: authenticationIdentityInput
          value:
            - name: tenantId
              value: string
            - name: applicationId
              value: string
            - name: objectId
              value: string
            - name: audience
              value: string
            - name: aadAuthority
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>replication_recovery_services_providers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.recovery_services_site_recovery.replication_recovery_services_providers
WHERE fabricName = '{{ fabricName }}'
AND providerName = '{{ providerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
