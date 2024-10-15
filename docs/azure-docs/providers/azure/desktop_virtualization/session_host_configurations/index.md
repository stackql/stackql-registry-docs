---
title: session_host_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - session_host_configurations
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>session_host_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>session_host_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.session_host_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_session_host_configurations', value: 'view', },
        { label: 'session_host_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="availability_zones" /> | `text` | field from the `properties` object |
| <CopyableCode code="boot_diagnostics_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_configuration_script_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="image_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_admin_credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_name_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_resource_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_size_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_tags" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Session host configurations of HostPool. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | Get a SessionHostConfiguration. |
| <CopyableCode code="list_by_host_pool" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | List sessionHostConfigurations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId, data__properties" /> | Create or update a SessionHostConfiguration. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | Update a SessionHostConfiguration. |

## `SELECT` examples

Get a SessionHostConfiguration.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_session_host_configurations', value: 'view', },
        { label: 'session_host_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
availability_zones,
boot_diagnostics_info,
custom_configuration_script_url,
disk_info,
domain_info,
friendly_name,
hostPoolName,
image_info,
network_info,
provisioning_state,
resourceGroupName,
security_info,
subscriptionId,
system_data,
type,
version,
vm_admin_credentials,
vm_location,
vm_name_prefix,
vm_resource_group,
vm_size_id,
vm_tags
FROM azure.desktop_virtualization.vw_session_host_configurations
WHERE hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.desktop_virtualization.session_host_configurations
WHERE hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>session_host_configurations</code> resource.

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
INSERT INTO azure.desktop_virtualization.session_host_configurations (
hostPoolName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ hostPoolName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
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
        - name: version
          value: string
        - name: friendlyName
          value: string
        - name: provisioningState
          value: string
        - name: vmTags
          value: object
        - name: vmLocation
          value: string
        - name: vmResourceGroup
          value: string
        - name: vmNamePrefix
          value: string
        - name: availabilityZones
          value:
            - integer
        - name: networkInfo
          value:
            - name: subnetId
              value: string
            - name: securityGroupId
              value: string
        - name: vmSizeId
          value: string
        - name: diskInfo
          value:
            - name: type
              value: string
        - name: customConfigurationScriptUrl
          value: string
        - name: imageInfo
          value:
            - name: type
              value: string
            - name: marketplaceInfo
              value:
                - name: offer
                  value: string
                - name: publisher
                  value: string
                - name: sku
                  value: string
                - name: exactVersion
                  value: string
            - name: customInfo
              value:
                - name: resourceId
                  value: string
        - name: domainInfo
          value:
            - name: joinType
              value: string
            - name: activeDirectoryInfo
              value:
                - name: domainCredentials
                  value:
                    - name: usernameKeyVaultSecretUri
                      value: string
                    - name: passwordKeyVaultSecretUri
                      value: string
                - name: ouPath
                  value: string
                - name: domainName
                  value: string
            - name: azureActiveDirectoryInfo
              value:
                - name: mdmProviderGuid
                  value: string
        - name: securityInfo
          value:
            - name: type
              value: string
            - name: secureBootEnabled
              value: boolean
            - name: vTpmEnabled
              value: boolean
        - name: bootDiagnosticsInfo
          value:
            - name: enabled
              value: boolean
            - name: storageUri
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>session_host_configurations</code> resource.

```sql
/*+ update */
UPDATE azure.desktop_virtualization.session_host_configurations
SET 
properties = '{{ properties }}'
WHERE 
hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
