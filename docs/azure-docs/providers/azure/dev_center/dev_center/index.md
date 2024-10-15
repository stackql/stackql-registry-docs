---
title: dev_center
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_center
  - dev_center
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

Creates, updates, deletes, gets or lists a <code>dev_center</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dev_center</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.dev_center" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dev_center', value: 'view', },
        { label: 'dev_center', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="devCenterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dev_box_provisioning_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="dev_center_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="network_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="project_catalog_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restricted_resource_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the devcenter. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="devCenterName, resourceGroupName, subscriptionId" /> | Gets a devcenter. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all devcenters in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all devcenters in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="devCenterName, resourceGroupName, subscriptionId" /> | Creates or updates a devcenter resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="devCenterName, resourceGroupName, subscriptionId" /> | Deletes a devcenter |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="devCenterName, resourceGroupName, subscriptionId" /> | Partially updates a devcenter. |

## `SELECT` examples

Lists all devcenters in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dev_center', value: 'view', },
        { label: 'dev_center', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
devCenterName,
dev_box_provisioning_settings,
dev_center_uri,
display_name,
encryption,
identity,
location,
network_settings,
plan_id,
project_catalog_settings,
provisioning_state,
resourceGroupName,
restricted_resource_types,
subscriptionId,
tags
FROM azure.dev_center.vw_dev_center
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.dev_center.dev_center
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dev_center</code> resource.

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
INSERT INTO azure.dev_center.dev_center (
devCenterName,
resourceGroupName,
subscriptionId,
tags,
location,
properties,
identity
)
SELECT 
'{{ devCenterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: planId
          value: string
        - name: encryption
          value:
            - name: customerManagedKeyEncryption
              value:
                - name: keyEncryptionKeyIdentity
                  value:
                    - name: identityType
                      value: string
                    - name: userAssignedIdentityResourceId
                      value: string
                    - name: delegatedIdentityClientId
                      value: string
                - name: keyEncryptionKeyUrl
                  value: string
        - name: displayName
          value: string
        - name: projectCatalogSettings
          value:
            - name: catalogItemSyncEnableStatus
              value: []
        - name: networkSettings
          value:
            - name: microsoftHostedNetworkEnableStatus
              value: []
        - name: devBoxProvisioningSettings
          value:
            - name: installAzureMonitorAgentEnableStatus
              value: []
        - name: restrictedResourceTypes
          value:
            - []
        - name: provisioningState
          value: []
        - name: devCenterUri
          value: []
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

Updates a <code>dev_center</code> resource.

```sql
/*+ update */
UPDATE azure.dev_center.dev_center
SET 
tags = '{{ tags }}',
location = '{{ location }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>dev_center</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_center.dev_center
WHERE devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
