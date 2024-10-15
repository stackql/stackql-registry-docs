---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - log_analytics
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.clusters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_clusters', value: 'view', },
        { label: 'clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="associated_workspaces" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacity_reservation_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="is_availability_zones_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_double_encryption_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The cluster sku definition. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Cluster properties. |
| <CopyableCode code="sku" /> | `object` | The cluster sku definition. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets a Log Analytics cluster instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the Log Analytics clusters in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets Log Analytics clusters in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Create or update a Log Analytics cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Deletes a cluster instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Updates a Log Analytics cluster. |

## `SELECT` examples

Gets the Log Analytics clusters in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_clusters', value: 'view', },
        { label: 'clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
associated_workspaces,
billing_type,
capacity_reservation_properties,
clusterName,
cluster_id,
created_date,
identity,
is_availability_zones_enabled,
is_double_encryption_enabled,
key_vault_properties,
last_modified_date,
location,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
tags
FROM azure.log_analytics.vw_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
sku,
tags
FROM azure.log_analytics.clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clusters</code> resource.

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
INSERT INTO azure.log_analytics.clusters (
clusterName,
resourceGroupName,
subscriptionId,
identity,
sku,
properties,
tags,
location
)
SELECT 
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ identity }}',
'{{ sku }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
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
          value: []
        - name: userAssignedIdentities
          value: []
    - name: sku
      value:
        - name: capacity
          value: integer
        - name: name
          value: string
    - name: properties
      value:
        - name: clusterId
          value: string
        - name: provisioningState
          value: string
        - name: isDoubleEncryptionEnabled
          value: boolean
        - name: isAvailabilityZonesEnabled
          value: boolean
        - name: billingType
          value: []
        - name: keyVaultProperties
          value:
            - name: keyVaultUri
              value: string
            - name: keyName
              value: string
            - name: keyVersion
              value: string
            - name: keyRsaSize
              value: integer
        - name: lastModifiedDate
          value: string
        - name: createdDate
          value: string
        - name: associatedWorkspaces
          value:
            - - name: workspaceId
                value: string
              - name: workspaceName
                value: string
              - name: resourceId
                value: string
              - name: associateDate
                value: string
        - name: capacityReservationProperties
          value:
            - name: lastSkuUpdate
              value: string
            - name: minCapacity
              value: integer
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>clusters</code> resource.

```sql
/*+ update */
UPDATE azure.log_analytics.clusters
SET 
properties = '{{ properties }}',
identity = '{{ identity }}',
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure.log_analytics.clusters
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
