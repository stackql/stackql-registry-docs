---
title: arc_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - arc_settings
  - azure_stack_hci
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

Creates, updates, deletes, gets or lists a <code>arc_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>arc_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.arc_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_arc_settings', value: 'view', },
        { label: 'arc_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aggregate_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="arcSettingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="arc_application_client_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="arc_application_object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="arc_application_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="arc_instance_resource_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="arc_service_principal_object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectivity_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_extensions" /> | `text` | field from the `properties` object |
| <CopyableCode code="per_node_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | ArcSetting properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | Get ArcSetting resource details of HCI Cluster. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get ArcSetting resources of HCI Cluster. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | Create ArcSetting for HCI cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | Delete ArcSetting resource details of HCI Cluster. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | Update ArcSettings for HCI cluster. |
| <CopyableCode code="consent_and_install_default_extensions" /> | `EXEC` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | Add consent time for default extensions and initiate extensions installation |
| <CopyableCode code="generate_password" /> | `EXEC` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | Generate password for arc settings. |
| <CopyableCode code="initialize_disable_process" /> | `EXEC` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | Initializes ARC Disable process on the cluster |

## `SELECT` examples

Get ArcSetting resources of HCI Cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_arc_settings', value: 'view', },
        { label: 'arc_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
aggregate_state,
arcSettingName,
arc_application_client_id,
arc_application_object_id,
arc_application_tenant_id,
arc_instance_resource_group,
arc_service_principal_object_id,
clusterName,
connectivity_properties,
default_extensions,
per_node_details,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure_stack.azure_stack_hci.vw_arc_settings
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_stack.azure_stack_hci.arc_settings
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>arc_settings</code> resource.

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
INSERT INTO azure_stack.azure_stack_hci.arc_settings (
arcSettingName,
clusterName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ arcSettingName }}',
'{{ clusterName }}',
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
        - name: provisioningState
          value: string
        - name: arcInstanceResourceGroup
          value: string
        - name: arcApplicationClientId
          value: string
        - name: arcApplicationTenantId
          value: string
        - name: arcServicePrincipalObjectId
          value: string
        - name: arcApplicationObjectId
          value: string
        - name: aggregateState
          value: string
        - name: perNodeDetails
          value:
            - - name: name
                value: string
              - name: arcInstance
                value: string
              - name: arcNodeServicePrincipalObjectId
                value: string
              - name: state
                value: string
        - name: connectivityProperties
          value: object
        - name: defaultExtensions
          value:
            - - name: category
                value: string
              - name: consentTime
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>arc_settings</code> resource.

```sql
/*+ update */
UPDATE azure_stack.azure_stack_hci.arc_settings
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
arcSettingName = '{{ arcSettingName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>arc_settings</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack_hci.arc_settings
WHERE arcSettingName = '{{ arcSettingName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
