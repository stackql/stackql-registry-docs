---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - nginx
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.nginx.deployments" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | field from the `properties` object |
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_upgrade_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="deploymentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_diagnostics_support" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="logging" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_resource_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="nginx_app_protect" /> | `text` | field from the `properties` object |
| <CopyableCode code="nginx_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scaling_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_profile" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="identity" /> | `object` |  |
| <CopyableCode code="location" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="sku" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` |  |
| <CopyableCode code="type" /> | `string` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



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
id,
name,
auto_upgrade_profile,
deploymentName,
enable_diagnostics_support,
identity,
ip_address,
location,
logging,
managed_resource_group,
network_profile,
nginx_app_protect,
nginx_version,
provisioning_state,
resourceGroupName,
scaling_properties,
sku,
subscriptionId,
system_data,
tags,
type,
user_profile
FROM azure_isv.nginx.vw_deployments
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
location,
properties,
sku,
systemData,
tags,
type
FROM azure_isv.nginx.deployments
WHERE subscriptionId = '{{ subscriptionId }}';
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
INSERT INTO azure_isv.nginx.deployments (
deploymentName,
resourceGroupName,
subscriptionId,
identity,
properties,
tags,
sku,
location
)
SELECT 
'{{ deploymentName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ identity }}',
'{{ properties }}',
'{{ tags }}',
'{{ sku }}',
'{{ location }}'
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
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: object
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: nginxVersion
          value: string
        - name: managedResourceGroup
          value: string
        - name: networkProfile
          value:
            - name: frontEndIPConfiguration
              value:
                - name: publicIPAddresses
                  value:
                    - - name: id
                        value: string
                - name: privateIPAddresses
                  value:
                    - - name: privateIPAddress
                        value: string
                      - name: privateIPAllocationMethod
                        value: []
                      - name: subnetId
                        value: string
            - name: networkInterfaceConfiguration
              value:
                - name: subnetId
                  value: string
        - name: ipAddress
          value: string
        - name: enableDiagnosticsSupport
          value: boolean
        - name: logging
          value:
            - name: storageAccount
              value:
                - name: accountName
                  value: string
                - name: containerName
                  value: string
        - name: scalingProperties
          value:
            - name: capacity
              value: integer
            - name: autoScaleSettings
              value:
                - name: profiles
                  value:
                    - - name: name
                        value: string
                      - name: capacity
                        value:
                          - name: min
                            value: integer
                          - name: max
                            value: integer
        - name: autoUpgradeProfile
          value:
            - name: upgradeChannel
              value: string
        - name: userProfile
          value:
            - name: preferredEmail
              value: string
        - name: nginxAppProtect
          value:
            - name: webApplicationFirewallSettings
              value:
                - name: activationState
                  value: string
            - name: webApplicationFirewallStatus
              value:
                - name: attackSignaturesPackage
                  value:
                    - name: version
                      value: string
                    - name: revisionDatetime
                      value: string
                - name: componentVersions
                  value:
                    - name: wafEngineVersion
                      value: string
                    - name: wafNginxVersion
                      value: string
    - name: tags
      value: object
    - name: sku
      value:
        - name: name
          value: string
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>deployments</code> resource.

```sql
/*+ update */
UPDATE azure_isv.nginx.deployments
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
sku = '{{ sku }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>deployments</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.nginx.deployments
WHERE deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
