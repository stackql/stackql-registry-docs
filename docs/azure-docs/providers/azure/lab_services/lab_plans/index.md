---
title: lab_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - lab_plans
  - lab_services
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

Creates, updates, deletes, gets or lists a <code>lab_plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lab_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.lab_services.lab_plans" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_lab_plans', value: 'view', },
        { label: 'lab_plans', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allowed_regions" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_auto_shutdown_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_connection_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="labPlanName" /> | `text` | field from the `properties` object |
| <CopyableCode code="linked_lms_instance" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_operation_error" /> | `text` | field from the `properties` object |
| <CopyableCode code="shared_gallery_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="support_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Lab plan resource properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="labPlanName, resourceGroupName, subscriptionId" /> | Retrieves the properties of a Lab Plan. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns a list of all lab plans for a subscription and resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns a list of all lab plans within a subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="labPlanName, resourceGroupName, subscriptionId, data__properties" /> | Operation to create or update a Lab Plan resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="labPlanName, resourceGroupName, subscriptionId" /> | Operation to delete a Lab Plan resource. Deleting a lab plan does not delete labs associated with a lab plan, nor does it delete shared images added to a gallery via the lab plan permission container. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="labPlanName, resourceGroupName, subscriptionId" /> | Operation to update a Lab Plan resource. |
| <CopyableCode code="save_image" /> | `EXEC` | <CopyableCode code="labPlanName, resourceGroupName, subscriptionId" /> | Saves an image from a lab VM to the attached shared image gallery. |

## `SELECT` examples

Returns a list of all lab plans within a subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_lab_plans', value: 'view', },
        { label: 'lab_plans', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
allowed_regions,
default_auto_shutdown_profile,
default_connection_profile,
default_network_profile,
identity,
labPlanName,
linked_lms_instance,
location,
provisioning_state,
resourceGroupName,
resource_operation_error,
shared_gallery_id,
subscriptionId,
support_info,
system_data,
tags
FROM azure.lab_services.vw_lab_plans
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
systemData,
tags
FROM azure.lab_services.lab_plans
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>lab_plans</code> resource.

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
INSERT INTO azure.lab_services.lab_plans (
labPlanName,
resourceGroupName,
subscriptionId,
data__properties,
tags,
location,
properties,
identity
)
SELECT 
'{{ labPlanName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
    - name: properties
      value:
        - name: defaultConnectionProfile
          value:
            - name: webSshAccess
              value: []
        - name: defaultAutoShutdownProfile
          value:
            - name: shutdownOnDisconnect
              value: []
            - name: shutdownOnIdle
              value: []
            - name: disconnectDelay
              value: string
            - name: noConnectDelay
              value: string
            - name: idleDelay
              value: string
        - name: defaultNetworkProfile
          value:
            - name: subnetId
              value: []
        - name: allowedRegions
          value:
            - string
        - name: supportInfo
          value:
            - name: email
              value: []
            - name: phone
              value: []
            - name: instructions
              value: string
        - name: provisioningState
          value: []
        - name: resourceOperationError
          value:
            - name: timestamp
              value: string
            - name: code
              value: string
            - name: message
              value: string
            - name: action
              value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>lab_plans</code> resource.

```sql
/*+ update */
UPDATE azure.lab_services.lab_plans
SET 
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
labPlanName = '{{ labPlanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>lab_plans</code> resource.

```sql
/*+ delete */
DELETE FROM azure.lab_services.lab_plans
WHERE labPlanName = '{{ labPlanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
