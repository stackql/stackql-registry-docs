---
title: provider_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_instances
  - sap_workloads
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

Creates, updates, deletes, gets or lists a <code>provider_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.sap_workloads.provider_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_provider_instances', value: 'view', },
        { label: 'provider_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | A pre-created user assigned identity with appropriate roles assigned. To learn more on identity and roles required, visit the ACSS how-to-guide. |
| <CopyableCode code="monitorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="providerInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | A pre-created user assigned identity with appropriate roles assigned. To learn more on identity and roles required, visit the ACSS how-to-guide. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a provider instance. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, providerInstanceName, resourceGroupName, subscriptionId" /> | Gets properties of a provider instance for the specified subscription, resource group, SAP monitor name, and resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Gets a list of provider instances in the specified SAP monitor. The operations returns various properties of each provider instances. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="monitorName, providerInstanceName, resourceGroupName, subscriptionId" /> | Creates a provider instance for the specified subscription, resource group, SAP monitor name, and resource name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="monitorName, providerInstanceName, resourceGroupName, subscriptionId" /> | Deletes a provider instance for the specified subscription, resource group, SAP monitor name, and resource name. |

## `SELECT` examples

Gets a list of provider instances in the specified SAP monitor. The operations returns various properties of each provider instances.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_provider_instances', value: 'view', },
        { label: 'provider_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
errors,
identity,
monitorName,
providerInstanceName,
provider_settings,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure_isv.sap_workloads.vw_provider_instances
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
properties
FROM azure_isv.sap_workloads.provider_instances
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>provider_instances</code> resource.

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
INSERT INTO azure_isv.sap_workloads.provider_instances (
monitorName,
providerInstanceName,
resourceGroupName,
subscriptionId,
identity,
properties
)
SELECT 
'{{ monitorName }}',
'{{ providerInstanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ identity }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: identity
      value:
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: errors
          value: string
        - name: providerSettings
          value:
            - name: providerType
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>provider_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.sap_workloads.provider_instances
WHERE monitorName = '{{ monitorName }}'
AND providerInstanceName = '{{ providerInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
