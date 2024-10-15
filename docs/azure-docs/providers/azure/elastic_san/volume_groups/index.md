---
title: volume_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_groups
  - elastic_san
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

Creates, updates, deletes, gets or lists a <code>volume_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.elastic_san.volume_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volume_groups', value: 'view', },
        { label: 'volume_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="elasticSanName" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="enforce_data_integrity_check_for_iscsi" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="network_acls" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="protocol_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="volumeGroupName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="properties" /> | `object` | VolumeGroup response properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName" /> | Get an VolumeGroups. |
| <CopyableCode code="list_by_elastic_san" /> | `SELECT` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId" /> | List VolumeGroups. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName" /> | Create a Volume Group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName" /> | Delete an VolumeGroup. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName" /> | Update an VolumeGroup. |

## `SELECT` examples

List VolumeGroups.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volume_groups', value: 'view', },
        { label: 'volume_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
elasticSanName,
encryption,
encryption_properties,
enforce_data_integrity_check_for_iscsi,
identity,
network_acls,
private_endpoint_connections,
protocol_type,
provisioning_state,
resourceGroupName,
subscriptionId,
volumeGroupName
FROM azure.elastic_san.vw_volume_groups
WHERE elasticSanName = '{{ elasticSanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
properties
FROM azure.elastic_san.volume_groups
WHERE elasticSanName = '{{ elasticSanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>volume_groups</code> resource.

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
INSERT INTO azure.elastic_san.volume_groups (
elasticSanName,
resourceGroupName,
subscriptionId,
volumeGroupName,
identity,
properties
)
SELECT 
'{{ elasticSanName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ volumeGroupName }}',
'{{ identity }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: protocolType
          value: []
        - name: encryption
          value: []
        - name: encryptionProperties
          value:
            - name: keyVaultProperties
              value:
                - name: keyIdentifier
                  value: string
                - name: identity
                  value: string
            - name: identity
              value:
                - name: userAssignedIdentity
                  value: string
        - name: networkAcls
          value:
            - name: virtualNetworkRules
              value:
                - - name: id
                    value: string
                  - name: action
                    value: string
        - name: privateEndpointConnections
          value:
            - - name: properties
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
                  - name: groupIds
                    value:
                      - string
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
        - name: enforceDataIntegrityCheckForIscsi
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>volume_groups</code> resource.

```sql
/*+ update */
UPDATE azure.elastic_san.volume_groups
SET 
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
elasticSanName = '{{ elasticSanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeGroupName = '{{ volumeGroupName }}';
```

## `DELETE` example

Deletes the specified <code>volume_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.elastic_san.volume_groups
WHERE elasticSanName = '{{ elasticSanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeGroupName = '{{ volumeGroupName }}';
```
