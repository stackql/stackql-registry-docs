---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
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

Creates, updates, deletes, gets or lists a <code>assets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.device_registry.assets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_assets', value: 'view', },
        { label: 'assets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="assetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="asset_endpoint_profile_ref" /> | `text` | field from the `properties` object |
| <CopyableCode code="attributes" /> | `text` | field from the `properties` object |
| <CopyableCode code="datasets" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_datasets_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_events_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_topic" /> | `text` | field from the `properties` object |
| <CopyableCode code="discovered_asset_refs" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="documentation_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="events" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="external_asset_id" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="uuid" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Defines the asset properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assetName, resourceGroupName, subscriptionId" /> | Get a Asset |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List Asset resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Asset resources by subscription ID |
| <CopyableCode code="create_or_replace" /> | `INSERT` | <CopyableCode code="assetName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a Asset |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="assetName, resourceGroupName, subscriptionId" /> | Delete a Asset |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="assetName, resourceGroupName, subscriptionId" /> | Update a Asset |

## `SELECT` examples

List Asset resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_assets', value: 'view', },
        { label: 'assets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
assetName,
asset_endpoint_profile_ref,
attributes,
datasets,
default_datasets_configuration,
default_events_configuration,
default_topic,
discovered_asset_refs,
display_name,
documentation_uri,
enabled,
events,
extended_location,
external_asset_id,
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
status,
subscriptionId,
tags,
uuid,
version
FROM azure.device_registry.vw_assets
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
FROM azure.device_registry.assets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>assets</code> resource.

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
INSERT INTO azure.device_registry.assets (
assetName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ assetName }}',
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
        - name: enabled
          value: boolean
        - name: externalAssetId
          value: string
        - name: displayName
          value: string
        - name: description
          value: string
        - name: assetEndpointProfileRef
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
        - name: attributes
          value: object
        - name: discoveredAssetRefs
          value:
            - string
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
                  - - name: observabilityMode
                      value: string
                    - name: name
                      value: string
                    - name: dataSource
                      value: string
                    - name: dataPointConfiguration
                      value: string
        - name: events
          value:
            - - name: observabilityMode
                value: string
              - name: name
                value: string
              - name: eventNotifier
                value: string
              - name: eventConfiguration
                value: string
        - name: status
          value:
            - name: errors
              value:
                - - name: code
                    value: integer
                  - name: message
                    value: string
            - name: version
              value: integer
            - name: datasets
              value:
                - - name: name
                    value: string
                  - name: messageSchemaReference
                    value:
                      - name: schemaRegistryNamespace
                        value: string
                      - name: schemaName
                        value: string
                      - name: schemaVersion
                        value: string
            - name: events
              value:
                - - name: name
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

Updates a <code>assets</code> resource.

```sql
/*+ update */
UPDATE azure.device_registry.assets
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
assetName = '{{ assetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>assets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.device_registry.assets
WHERE assetName = '{{ assetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
