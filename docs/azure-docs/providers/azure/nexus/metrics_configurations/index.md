---
title: metrics_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics_configurations
  - nexus
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

Creates, updates, deletes, gets or lists a <code>metrics_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metrics_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.metrics_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_metrics_configurations', value: 'view', },
        { label: 'metrics_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="collection_interval" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="disabled_metrics" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_metrics" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="metricsConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, metricsConfigurationName, resourceGroupName, subscriptionId" /> | Get metrics configuration of the provided cluster. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get a list of metrics configurations for the provided cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, metricsConfigurationName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties" /> | Create new or update the existing metrics configuration of the provided cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, metricsConfigurationName, resourceGroupName, subscriptionId" /> | Delete the metrics configuration of the provided cluster. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, metricsConfigurationName, resourceGroupName, subscriptionId" /> | Patch properties of metrics configuration for the provided cluster, or update the tags associated with it. Properties and tag updates can be done independently. |

## `SELECT` examples

Get a list of metrics configurations for the provided cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_metrics_configurations', value: 'view', },
        { label: 'metrics_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
clusterName,
collection_interval,
detailed_status,
detailed_status_message,
disabled_metrics,
enabled_metrics,
extended_location,
location,
metricsConfigurationName,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.nexus.vw_metrics_configurations
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.nexus.metrics_configurations
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>metrics_configurations</code> resource.

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
INSERT INTO azure.nexus.metrics_configurations (
clusterName,
metricsConfigurationName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
data__properties,
extendedLocation,
properties,
tags,
location
)
SELECT 
'{{ clusterName }}',
'{{ metricsConfigurationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
'{{ data__properties }}',
'{{ extendedLocation }}',
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
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: string
    - name: properties
      value:
        - name: collectionInterval
          value: integer
        - name: detailedStatus
          value: string
        - name: detailedStatusMessage
          value: string
        - name: disabledMetrics
          value:
            - string
        - name: enabledMetrics
          value:
            - string
        - name: provisioningState
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>metrics_configurations</code> resource.

```sql
/*+ update */
UPDATE azure.nexus.metrics_configurations
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
clusterName = '{{ clusterName }}'
AND metricsConfigurationName = '{{ metricsConfigurationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>metrics_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.nexus.metrics_configurations
WHERE clusterName = '{{ clusterName }}'
AND metricsConfigurationName = '{{ metricsConfigurationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
