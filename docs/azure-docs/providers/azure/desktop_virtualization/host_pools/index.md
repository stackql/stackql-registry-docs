---
title: host_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - host_pools
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>host_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>host_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.host_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_host_pools', value: 'view', },
        { label: 'host_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_update" /> | `text` | field from the `properties` object |
| <CopyableCode code="app_attach_package_references" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_group_references" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_pc_resource" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_rdp_property" /> | `text` | field from the `properties` object |
| <CopyableCode code="direct_udp" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.  |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_pool_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="kind" /> | `text` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="load_balancer_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_private_udp" /> | `text` | field from the `properties` object |
| <CopyableCode code="management_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_session_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="personal_desktop_assignment_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan" /> | `text` | Plan for the resource. |
| <CopyableCode code="preferred_app_group_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_udp" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="relay_udp" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ring" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="sso_client_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="sso_client_secret_key_vault_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="sso_secret_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="ssoadfs_authority" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_vm_on_connect" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="validation_environment" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_template" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.  |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="managedBy" /> | `string` | The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource. |
| <CopyableCode code="plan" /> | `object` | Plan for the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of HostPool. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | Get a host pool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List hostPools in subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List hostPools. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId, data__properties" /> | Create or update a host pool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | Remove a host pool. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | Update a host pool. |
| <CopyableCode code="retrieve_registration_token" /> | `EXEC` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | Registration token of the host pool. |

## `SELECT` examples

List hostPools in subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_host_pools', value: 'view', },
        { label: 'host_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
agent_update,
app_attach_package_references,
application_group_references,
cloud_pc_resource,
custom_rdp_property,
direct_udp,
etag,
friendly_name,
hostPoolName,
host_pool_type,
identity,
kind,
load_balancer_type,
managed_by,
managed_private_udp,
management_type,
max_session_limit,
object_id,
personal_desktop_assignment_type,
plan,
preferred_app_group_type,
private_endpoint_connections,
public_network_access,
public_udp,
registration_info,
relay_udp,
resourceGroupName,
ring,
sku,
sso_client_id,
sso_client_secret_key_vault_path,
sso_secret_type,
ssoadfs_authority,
start_vm_on_connect,
subscriptionId,
validation_environment,
vm_template
FROM azure.desktop_virtualization.vw_host_pools
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
identity,
kind,
managedBy,
plan,
properties,
sku
FROM azure.desktop_virtualization.host_pools
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>host_pools</code> resource.

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
INSERT INTO azure.desktop_virtualization.host_pools (
hostPoolName,
resourceGroupName,
subscriptionId,
data__properties,
managedBy,
kind,
identity,
sku,
plan,
properties
)
SELECT 
'{{ hostPoolName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ managedBy }}',
'{{ kind }}',
'{{ identity }}',
'{{ sku }}',
'{{ plan }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: managedBy
      value: string
    - name: kind
      value: string
    - name: etag
      value: string
    - name: identity
      value: string
    - name: sku
      value: string
    - name: plan
      value: string
    - name: properties
      value:
        - name: objectId
          value: string
        - name: friendlyName
          value: string
        - name: description
          value: string
        - name: hostPoolType
          value: string
        - name: personalDesktopAssignmentType
          value: string
        - name: customRdpProperty
          value: string
        - name: maxSessionLimit
          value: integer
        - name: loadBalancerType
          value: string
        - name: ring
          value: integer
        - name: validationEnvironment
          value: boolean
        - name: registrationInfo
          value:
            - name: expirationTime
              value: string
            - name: token
              value: string
            - name: registrationTokenOperation
              value: string
        - name: vmTemplate
          value: string
        - name: managementType
          value: string
        - name: applicationGroupReferences
          value:
            - string
        - name: appAttachPackageReferences
          value:
            - string
        - name: ssoadfsAuthority
          value: string
        - name: ssoClientId
          value: string
        - name: ssoClientSecretKeyVaultPath
          value: string
        - name: ssoSecretType
          value: string
        - name: preferredAppGroupType
          value: string
        - name: startVMOnConnect
          value: boolean
        - name: cloudPcResource
          value: boolean
        - name: publicNetworkAccess
          value: string
        - name: agentUpdate
          value:
            - name: type
              value: string
            - name: useSessionHostLocalTime
              value: boolean
            - name: maintenanceWindowTimeZone
              value: string
            - name: maintenanceWindows
              value:
                - - name: hour
                    value: integer
                  - name: dayOfWeek
                    value: string
        - name: privateEndpointConnections
          value:
            - - name: properties
                value:
                  - name: groupIds
                    value:
                      - string
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
              - name: id
                value: string
              - name: name
                value: string
              - name: type
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
        - name: managedPrivateUDP
          value: string
        - name: directUDP
          value: string
        - name: publicUDP
          value: string
        - name: relayUDP
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>host_pools</code> resource.

```sql
/*+ update */
UPDATE azure.desktop_virtualization.host_pools
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>host_pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.desktop_virtualization.host_pools
WHERE hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
