---
title: security_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - security_settings
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

Creates, updates, deletes, gets or lists a <code>security_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.security_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_security_settings', value: 'view', },
        { label: 'security_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secured_core_compliance_assignment" /> | `text` | field from the `properties` object |
| <CopyableCode code="securitySettingsName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_compliance_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Security properties of the resource |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, securitySettingsName, subscriptionId" /> | Get a SecuritySetting |
| <CopyableCode code="list_by_clusters" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | List SecuritySetting resources by Clusters |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, securitySettingsName, subscriptionId" /> | Create a security setting |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, securitySettingsName, subscriptionId" /> | Delete a SecuritySetting |

## `SELECT` examples

List SecuritySetting resources by Clusters

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_security_settings', value: 'view', },
        { label: 'security_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
clusterName,
provisioning_state,
resourceGroupName,
secured_core_compliance_assignment,
securitySettingsName,
security_compliance_status,
subscriptionId
FROM azure_stack.azure_stack_hci.vw_security_settings
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_stack.azure_stack_hci.security_settings
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_settings</code> resource.

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
INSERT INTO azure_stack.azure_stack_hci.security_settings (
clusterName,
resourceGroupName,
securitySettingsName,
subscriptionId,
properties
)
SELECT 
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ securitySettingsName }}',
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
        - name: securedCoreComplianceAssignment
          value: []
        - name: securityComplianceStatus
          value:
            - name: securedCoreCompliance
              value: []
            - name: lastUpdated
              value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>security_settings</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack_hci.security_settings
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND securitySettingsName = '{{ securitySettingsName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
