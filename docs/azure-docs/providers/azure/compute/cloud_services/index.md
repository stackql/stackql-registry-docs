---
title: cloud_services
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_services
  - compute
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

Creates, updates, deletes, gets or lists a <code>cloud_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.cloud_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_services', value: 'view', },
        { label: 'cloud_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="allow_model_override" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloudServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="extension_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_cloud_service" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="unique_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="upgrade_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | List of logical availability zone of the resource. List should contain only 1 zone where cloud service should be provisioned. This field is optional. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Cloud service properties |
| <CopyableCode code="systemData" /> | `object` | The system meta data relating to this resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="zones" /> | `array` | List of logical availability zone of the resource. List should contain only 1 zone where cloud service should be provisioned. This field is optional. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Display information about a cloud service. |
| <CopyableCode code="get_instance_view" /> | `SELECT` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Gets the status of a cloud service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of all cloud services under a resource group. Use nextLink property in the response to get the next page of Cloud Services. Do this till nextLink is null to fetch all the Cloud Services. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of all cloud services in the subscription, regardless of the associated resource group. Use nextLink property in the response to get the next page of Cloud Services. Do this till nextLink is null to fetch all the Cloud Services. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId, data__location" /> | Create or update a cloud service. Please note some properties can be set only during cloud service creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Deletes a cloud service. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Update a cloud service. |
| <CopyableCode code="delete_instances" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId, data__roleInstances" /> | Deletes role instances in a cloud service. |
| <CopyableCode code="power_off" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Power off the cloud service. Note that resources are still attached and you are getting charged for the resources. |
| <CopyableCode code="rebuild" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId, data__roleInstances" /> | Rebuild Role Instances reinstalls the operating system on instances of web roles or worker roles and initializes the storage resources that are used by them. If you do not want to initialize storage resources, you can use Reimage Role Instances. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId, data__roleInstances" /> | Reimage asynchronous operation reinstalls the operating system on instances of web roles or worker roles. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId, data__roleInstances" /> | Restarts one or more role instances in a cloud service. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Starts the cloud service. |

## `SELECT` examples

Gets a list of all cloud services in the subscription, regardless of the associated resource group. Use nextLink property in the response to get the next page of Cloud Services. Do this till nextLink is null to fetch all the Cloud Services.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_services', value: 'view', },
        { label: 'cloud_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allow_model_override,
cloudServiceName,
configuration,
configuration_url,
extension_profile,
location,
network_profile,
os_profile,
package_url,
provisioning_state,
resourceGroupName,
role_profile,
start_cloud_service,
subscriptionId,
system_data,
tags,
type,
unique_id,
upgrade_mode,
zones
FROM azure.compute.vw_cloud_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
systemData,
tags,
type,
zones
FROM azure.compute.cloud_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cloud_services</code> resource.

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
INSERT INTO azure.compute.cloud_services (
cloudServiceName,
resourceGroupName,
subscriptionId,
data__location,
location,
tags,
properties,
systemData,
zones
)
SELECT 
'{{ cloudServiceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ systemData }}',
'{{ zones }}'
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
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: packageUrl
          value: string
        - name: configuration
          value: string
        - name: configurationUrl
          value: string
        - name: startCloudService
          value: boolean
        - name: allowModelOverride
          value: boolean
        - name: upgradeMode
          value: []
        - name: roleProfile
          value:
            - name: roles
              value:
                - - name: name
                    value: string
                  - name: sku
                    value:
                      - name: name
                        value: string
                      - name: tier
                        value: string
                      - name: capacity
                        value: integer
        - name: osProfile
          value:
            - name: secrets
              value:
                - - name: sourceVault
                    value:
                      - name: id
                        value: string
                  - name: vaultCertificates
                    value:
                      - - name: certificateUrl
                          value: string
        - name: networkProfile
          value:
            - name: loadBalancerConfigurations
              value:
                - - name: id
                    value: string
                  - name: name
                    value: string
                  - name: properties
                    value:
                      - name: frontendIpConfigurations
                        value:
                          - - name: name
                              value: string
                            - name: properties
                              value:
                                - name: privateIPAddress
                                  value: string
            - name: slotType
              value: []
        - name: extensionProfile
          value:
            - name: extensions
              value:
                - - name: name
                    value: string
                  - name: properties
                    value:
                      - name: publisher
                        value: string
                      - name: type
                        value: string
                      - name: typeHandlerVersion
                        value: string
                      - name: autoUpgradeMinorVersion
                        value: boolean
                      - name: settings
                        value: object
                      - name: protectedSettings
                        value: object
                      - name: protectedSettingsFromKeyVault
                        value:
                          - name: secretUrl
                            value: string
                      - name: forceUpdateTag
                        value: string
                      - name: provisioningState
                        value: string
                      - name: rolesAppliedTo
                        value:
                          - string
        - name: provisioningState
          value: string
        - name: uniqueId
          value: string
    - name: systemData
      value:
        - name: createdAt
          value: string
        - name: lastModifiedAt
          value: string
    - name: zones
      value:
        - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>cloud_services</code> resource.

```sql
/*+ update */
UPDATE azure.compute.cloud_services
SET 
tags = '{{ tags }}'
WHERE 
cloudServiceName = '{{ cloudServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>cloud_services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.cloud_services
WHERE cloudServiceName = '{{ cloudServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
