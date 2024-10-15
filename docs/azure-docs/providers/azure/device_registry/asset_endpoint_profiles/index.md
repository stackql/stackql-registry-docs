---
title: asset_endpoint_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - asset_endpoint_profiles
  - device_registry
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

Creates, updates, deletes, gets or lists a <code>asset_endpoint_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>asset_endpoint_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.device_registry.asset_endpoint_profiles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_asset_endpoint_profiles', value: 'view', },
        { label: 'asset_endpoint_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="additional_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="assetEndpointProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="authentication" /> | `text` | field from the `properties` object |
| <CopyableCode code="discovered_asset_endpoint_profile_ref" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint_profile_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="target_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="uuid" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Defines the Asset Endpoint Profile properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assetEndpointProfileName, resourceGroupName, subscriptionId" /> | Get a AssetEndpointProfile |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List AssetEndpointProfile resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List AssetEndpointProfile resources by subscription ID |
| <CopyableCode code="create_or_replace" /> | `INSERT` | <CopyableCode code="assetEndpointProfileName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a AssetEndpointProfile |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="assetEndpointProfileName, resourceGroupName, subscriptionId" /> | Delete a AssetEndpointProfile |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="assetEndpointProfileName, resourceGroupName, subscriptionId" /> | Update a AssetEndpointProfile |

## `SELECT` examples

List AssetEndpointProfile resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_asset_endpoint_profiles', value: 'view', },
        { label: 'asset_endpoint_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
additional_configuration,
assetEndpointProfileName,
authentication,
discovered_asset_endpoint_profile_ref,
endpoint_profile_type,
extended_location,
location,
provisioning_state,
resourceGroupName,
status,
subscriptionId,
tags,
target_address,
uuid
FROM azure.device_registry.vw_asset_endpoint_profiles
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.device_registry.asset_endpoint_profiles
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>asset_endpoint_profiles</code> resource.

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
INSERT INTO azure.device_registry.asset_endpoint_profiles (
assetEndpointProfileName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ assetEndpointProfileName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: uuid
          value: string
        - name: targetAddress
          value: string
        - name: endpointProfileType
          value: string
        - name: authentication
          value:
            - name: method
              value: string
            - name: usernamePasswordCredentials
              value:
                - name: usernameSecretName
                  value: string
                - name: passwordSecretName
                  value: string
            - name: x509Credentials
              value:
                - name: certificateSecretName
                  value: string
        - name: additionalConfiguration
          value: string
        - name: discoveredAssetEndpointProfileRef
          value: string
        - name: status
          value:
            - name: errors
              value:
                - - name: code
                    value: integer
                  - name: message
                    value: string
        - name: provisioningState
          value: []
    - name: extendedLocation
      value:
        - name: type
          value: string
        - name: name
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>asset_endpoint_profiles</code> resource.

```sql
/*+ update */
UPDATE azure.device_registry.asset_endpoint_profiles
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
assetEndpointProfileName = '{{ assetEndpointProfileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>asset_endpoint_profiles</code> resource.

```sql
/*+ delete */
DELETE FROM azure.device_registry.asset_endpoint_profiles
WHERE assetEndpointProfileName = '{{ assetEndpointProfileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
