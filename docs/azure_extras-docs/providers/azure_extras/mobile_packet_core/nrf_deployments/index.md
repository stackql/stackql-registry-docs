---
title: nrf_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - nrf_deployments
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

Creates, updates, deletes, gets or lists a <code>nrf_deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nrf_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.mobile_packet_core.nrf_deployments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_nrf_deployments', value: 'view', },
        { label: 'nrf_deployments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cluster_service" /> | `text` | field from the `properties` object |
| <CopyableCode code="component_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="nrfDeploymentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="operational_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="release_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secrets_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | NRF Deployment Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="nrfDeploymentName, resourceGroupName, subscriptionId" /> | Get a NrfDeploymentResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all Network Repository Function Deployments by Resource Group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all Network Repository Function Deployments by Subscription ID. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="nrfDeploymentName, resourceGroupName, subscriptionId" /> | Create a NrfDeploymentResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="nrfDeploymentName, resourceGroupName, subscriptionId" /> | Delete a NrfDeploymentResource |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="nrfDeploymentName, resourceGroupName, subscriptionId" /> | Update a NrfDeploymentResource |

## `SELECT` examples

List all Network Repository Function Deployments by Subscription ID.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_nrf_deployments', value: 'view', },
        { label: 'nrf_deployments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
cluster_service,
component_parameters,
location,
nrfDeploymentName,
operational_status,
provisioning_state,
release_version,
resourceGroupName,
secrets_parameters,
subscriptionId,
tags
FROM azure_extras.mobile_packet_core.vw_nrf_deployments
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure_extras.mobile_packet_core.nrf_deployments
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>nrf_deployments</code> resource.

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
INSERT INTO azure_extras.mobile_packet_core.nrf_deployments (
nrfDeploymentName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ nrfDeploymentName }}',
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
        - name: componentParameters
          value: []
        - name: secretsParameters
          value: []
        - name: clusterService
          value: []
        - name: releaseVersion
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

Deletes the specified <code>nrf_deployments</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.mobile_packet_core.nrf_deployments
WHERE nrfDeploymentName = '{{ nrfDeploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
