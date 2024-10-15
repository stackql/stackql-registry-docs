---
title: cloud_hsm_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_hsm_clusters
  - hardware_security_modules
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

Creates, updates, deletes, gets or lists a <code>cloud_hsm_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_hsm_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hardware_security_modules.cloud_hsm_clusters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_hsm_clusters', value: 'view', },
        { label: 'cloud_hsm_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activation_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_generated_domain_name_label_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloudHsmClusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="fips_approved_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="hsms" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Cloud Hsm Cluster SKU information |
| <CopyableCode code="status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="properties" /> | `object` | Properties of a Cloud HSM Cluster. |
| <CopyableCode code="sku" /> | `object` | Cloud Hsm Cluster SKU information |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudHsmClusterName, resourceGroupName, subscriptionId" /> | Gets the specified Cloud HSM Cluster |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The List operation gets information about the Cloud HSM Clusters associated with the subscription and within the specified resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The List operation gets information about the Cloud HSM Clusters associated with the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cloudHsmClusterName, resourceGroupName, subscriptionId" /> | Create or Update a Cloud HSM Cluster in the specified subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudHsmClusterName, resourceGroupName, subscriptionId" /> | Deletes the specified Cloud HSM Cluster |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="cloudHsmClusterName, resourceGroupName, subscriptionId" /> | Update a Cloud HSM Cluster in the specified subscription. |
| <CopyableCode code="backup" /> | `EXEC` | <CopyableCode code="cloudHsmClusterName, resourceGroupName, subscriptionId" /> | Create a backup of the Cloud HSM Cluster in the specified subscription |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="cloudHsmClusterName, resourceGroupName, subscriptionId, data__backupId" /> | Restores all key materials of a specified Cloud HSM Cluster |
| <CopyableCode code="validate_backup_properties" /> | `EXEC` | <CopyableCode code="cloudHsmClusterName, resourceGroupName, subscriptionId" /> | Pre Backup operation to validate whether the customer can perform a backup on the Cloud HSM Cluster resource in the specified subscription. |
| <CopyableCode code="validate_restore_properties" /> | `EXEC` | <CopyableCode code="cloudHsmClusterName, resourceGroupName, subscriptionId, data__backupId" /> | Queued validating pre restore operation |

## `SELECT` examples

The List operation gets information about the Cloud HSM Clusters associated with the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_hsm_clusters', value: 'view', },
        { label: 'cloud_hsm_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
activation_state,
auto_generated_domain_name_label_scope,
cloudHsmClusterName,
fips_approved_mode,
hsms,
identity,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
sku,
status_message,
subscriptionId
FROM azure.hardware_security_modules.vw_cloud_hsm_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
properties,
sku
FROM azure.hardware_security_modules.cloud_hsm_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cloud_hsm_clusters</code> resource.

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
INSERT INTO azure.hardware_security_modules.cloud_hsm_clusters (
cloudHsmClusterName,
resourceGroupName,
subscriptionId,
properties,
identity,
sku
)
SELECT 
'{{ cloudHsmClusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
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
        - name: activationState
          value: string
        - name: autoGeneratedDomainNameLabelScope
          value: string
        - name: fipsApprovedMode
          value: boolean
        - name: hsms
          value:
            - - name: fqdn
                value: string
              - name: state
                value: string
              - name: stateMessage
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
        - name: provisioningState
          value: string
        - name: publicNetworkAccess
          value: string
        - name: statusMessage
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
          value: object
    - name: sku
      value:
        - name: family
          value: string
        - name: name
          value: string
        - name: capacity
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>cloud_hsm_clusters</code> resource.

```sql
/*+ update */
UPDATE azure.hardware_security_modules.cloud_hsm_clusters
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
cloudHsmClusterName = '{{ cloudHsmClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>cloud_hsm_clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hardware_security_modules.cloud_hsm_clusters
WHERE cloudHsmClusterName = '{{ cloudHsmClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
