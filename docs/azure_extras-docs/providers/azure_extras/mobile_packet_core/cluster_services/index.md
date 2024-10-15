---
title: cluster_services
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_services
  - mobile_packet_core
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

Creates, updates, deletes, gets or lists a <code>cluster_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.mobile_packet_core.cluster_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cluster_services', value: 'view', },
        { label: 'cluster_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clusterServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_type_specific_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="component_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="operational_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="release_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Cluster Service Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterServiceName, resourceGroupName, subscriptionId" /> | Get a ClusterServiceResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all Cluster Services by Resource Group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all Cluster Services by Subscription ID. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterServiceName, resourceGroupName, subscriptionId" /> | Create a ClusterServiceResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterServiceName, resourceGroupName, subscriptionId" /> | Delete a ClusterServiceResource |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="clusterServiceName, resourceGroupName, subscriptionId" /> | Update a ClusterServiceResource |

## `SELECT` examples

List all Cluster Services by Subscription ID.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cluster_services', value: 'view', },
        { label: 'cluster_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
clusterServiceName,
cluster_type_specific_data,
component_parameters,
deployment_type,
location,
operational_status,
provisioning_state,
release_version,
resourceGroupName,
subscriptionId,
tags
FROM azure_extras.mobile_packet_core.vw_cluster_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure_extras.mobile_packet_core.cluster_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cluster_services</code> resource.

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
INSERT INTO azure_extras.mobile_packet_core.cluster_services (
clusterServiceName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ clusterServiceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: deploymentType
          value: []
        - name: releaseVersion
          value: []
        - name: clusterTypeSpecificData
          value:
            - name: type
              value: []
            - name: customLocationId
              value: []
        - name: componentParameters
          value:
            - - name: type
                value: []
              - name: parameters
                value: []
              - name: secrets
                value: []
        - name: operationalStatus
          value:
            - name: workload
              value: string
            - name: healthCheck
              value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>cluster_services</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.mobile_packet_core.cluster_services
WHERE clusterServiceName = '{{ clusterServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
