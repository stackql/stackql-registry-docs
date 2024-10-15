---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - sphere
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

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sphere.deployments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deployments', value: 'view', },
        { label: 'deployments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="catalogName" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployed_images" /> | `text` | field from the `properties` object |
| <CopyableCode code="deploymentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_date_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="productName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of deployment |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, deploymentName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | Get a Deployment. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| <CopyableCode code="list_by_device_group" /> | `SELECT` | <CopyableCode code="catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | List Deployment resources by DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="catalogName, deploymentName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | Create a Deployment. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogName, deploymentName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | Delete a Deployment. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |

## `SELECT` examples

List Deployment resources by DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deployments', value: 'view', },
        { label: 'deployments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
catalogName,
deployed_images,
deploymentName,
deployment_date_utc,
deployment_id,
deviceGroupName,
productName,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.sphere.vw_deployments
WHERE catalogName = '{{ catalogName }}'
AND deviceGroupName = '{{ deviceGroupName }}'
AND productName = '{{ productName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sphere.deployments
WHERE catalogName = '{{ catalogName }}'
AND deviceGroupName = '{{ deviceGroupName }}'
AND productName = '{{ productName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployments</code> resource.

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
INSERT INTO azure.sphere.deployments (
catalogName,
deploymentName,
deviceGroupName,
productName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ catalogName }}',
'{{ deploymentName }}',
'{{ deviceGroupName }}',
'{{ productName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: deploymentId
          value: string
        - name: deployedImages
          value:
            - - name: properties
                value:
                  - name: image
                    value: string
                  - name: imageId
                    value: string
                  - name: imageName
                    value: string
                  - name: regionalDataBoundary
                    value: []
                  - name: uri
                    value: string
                  - name: description
                    value: string
                  - name: componentId
                    value: string
                  - name: imageType
                    value: []
                  - name: provisioningState
                    value: []
        - name: deploymentDateUtc
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>deployments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sphere.deployments
WHERE catalogName = '{{ catalogName }}'
AND deploymentName = '{{ deploymentName }}'
AND deviceGroupName = '{{ deviceGroupName }}'
AND productName = '{{ productName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
