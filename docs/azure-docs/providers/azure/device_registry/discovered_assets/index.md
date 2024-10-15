---
title: discovered_assets
hide_title: false
hide_table_of_contents: false
keywords:
  - discovered_assets
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

Creates, updates, deletes, gets or lists a <code>discovered_assets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>discovered_assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.device_registry.discovered_assets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_discovered_assets', value: 'view', },
        { label: 'discovered_assets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="asset_endpoint_profile_ref" /> | `text` | field from the `properties` object |
| <CopyableCode code="datasets" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_datasets_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_events_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_topic" /> | `text` | field from the `properties` object |
| <CopyableCode code="discoveredAssetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="discovery_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="documentation_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="events" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="hardware_revision" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="manufacturer" /> | `text` | field from the `properties` object |
| <CopyableCode code="manufacturer_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="model" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serial_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="software_revision" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Defines the discovered asset properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="discoveredAssetName, resourceGroupName, subscriptionId" /> | Get a DiscoveredAsset |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List DiscoveredAsset resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List DiscoveredAsset resources by subscription ID |
| <CopyableCode code="create_or_replace" /> | `INSERT` | <CopyableCode code="discoveredAssetName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a DiscoveredAsset |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="discoveredAssetName, resourceGroupName, subscriptionId" /> | Delete a DiscoveredAsset |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="discoveredAssetName, resourceGroupName, subscriptionId" /> | Update a DiscoveredAsset |

## `SELECT` examples

List DiscoveredAsset resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_discovered_assets', value: 'view', },
        { label: 'discovered_assets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
asset_endpoint_profile_ref,
datasets,
default_datasets_configuration,
default_events_configuration,
default_topic,
discoveredAssetName,
discovery_id,
documentation_uri,
events,
extended_location,
hardware_revision,
location,
manufacturer,
manufacturer_uri,
model,
product_code,
provisioning_state,
resourceGroupName,
serial_number,
software_revision,
subscriptionId,
tags,
version
FROM azure.device_registry.vw_discovered_assets
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
FROM azure.device_registry.discovered_assets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>discovered_assets</code> resource.

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
INSERT INTO azure.device_registry.discovered_assets (
discoveredAssetName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ discoveredAssetName }}',
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
        - name: assetEndpointProfileRef
          value: string
        - name: discoveryId
          value: string
        - name: version
          value: integer
        - name: manufacturer
          value: string
        - name: manufacturerUri
          value: string
        - name: model
          value: string
        - name: productCode
          value: string
        - name: hardwareRevision
          value: string
        - name: softwareRevision
          value: string
        - name: documentationUri
          value: string
        - name: serialNumber
          value: string
        - name: defaultDatasetsConfiguration
          value: string
        - name: defaultEventsConfiguration
          value: string
        - name: defaultTopic
          value:
            - name: path
              value: string
            - name: retain
              value: string
        - name: datasets
          value:
            - - name: name
                value: string
              - name: datasetConfiguration
                value: string
              - name: dataPoints
                value:
                  - - name: name
                      value: string
                    - name: dataSource
                      value: string
                    - name: dataPointConfiguration
                      value: string
                    - name: lastUpdatedOn
                      value: string
        - name: events
          value:
            - - name: name
                value: string
              - name: eventNotifier
                value: string
              - name: eventConfiguration
                value: string
              - name: lastUpdatedOn
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

Updates a <code>discovered_assets</code> resource.

```sql
/*+ update */
UPDATE azure.device_registry.discovered_assets
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
discoveredAssetName = '{{ discoveredAssetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>discovered_assets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.device_registry.discovered_assets
WHERE discoveredAssetName = '{{ discoveredAssetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
