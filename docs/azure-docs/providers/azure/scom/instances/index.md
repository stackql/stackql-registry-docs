---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - scom
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

Creates, updates, deletes, gets or lists a <code>instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.scom.instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_instances', value: 'view', },
        { label: 'instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azure_hybrid_benefit" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_instance" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_controller" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_user_credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="gmsa_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Azure Active Directory identity configuration for a resource. |
| <CopyableCode code="instanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="log_analytics_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="management_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="operations_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="vnet_subnet_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Azure Active Directory identity configuration for a resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a SCOM instance resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Get SCOM managed instance details |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all SCOM managed instances in a resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all SCOM managed instances in a subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Create or update SCOM managed instance |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Delete a SCOM managed instance |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Patch SCOM managed instance |
| <CopyableCode code="link_log_analytics" /> | `EXEC` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Link Log Analytics workspace for SCOM monitoring instance |
| <CopyableCode code="patch_servers" /> | `EXEC` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Update SCOM servers with latest scom software. |
| <CopyableCode code="scale" /> | `EXEC` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Scaling SCOM managed instance. |
| <CopyableCode code="unlink_log_analytics" /> | `EXEC` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Unlink Log Analytics workspace for SCOM monitoring instance |

## `SELECT` examples

Lists all SCOM managed instances in a subscription 

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_instances', value: 'view', },
        { label: 'instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
azure_hybrid_benefit,
database_instance,
domain_controller,
domain_user_credentials,
gmsa_details,
identity,
instanceName,
location,
log_analytics_properties,
management_endpoints,
operations_status,
product_version,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
vnet_subnet_id
FROM azure.scom.vw_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.scom.instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instances</code> resource.

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
INSERT INTO azure.scom.instances (
instanceName,
resourceGroupName,
subscriptionId,
tags,
location,
properties,
identity
)
SELECT 
'{{ instanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
    - name: properties
      value:
        - name: productVersion
          value: string
        - name: vNetSubnetId
          value: string
        - name: managementEndpoints
          value:
            - - name: serverName
                value: string
              - name: vmResId
                value: string
              - name: fqdn
                value: string
              - name: serverRoles
                value: string
              - name: healthState
                value: string
        - name: databaseInstance
          value:
            - name: databaseInstanceId
              value: string
            - name: databaseFqdn
              value: string
            - name: dwDatabaseName
              value: string
            - name: operationalDatabaseId
              value: string
            - name: dwDatabaseId
              value: string
        - name: domainController
          value:
            - name: domainName
              value: string
            - name: dnsServer
              value: string
            - name: ouPath
              value: string
        - name: domainUserCredentials
          value:
            - name: keyVaultUrl
              value: string
            - name: userNameSecret
              value: string
            - name: passwordSecret
              value: string
        - name: gmsaDetails
          value:
            - name: loadBalancerIP
              value: string
            - name: gmsaAccount
              value: string
            - name: managementServerGroupName
              value: string
            - name: dnsName
              value: string
        - name: azureHybridBenefit
          value:
            - name: scomLicenseType
              value: []
        - name: provisioningState
          value: string
        - name: logAnalyticsProperties
          value:
            - name: workspaceId
              value: string
            - name: dataTypes
              value:
                - string
            - name: importData
              value: boolean
        - name: operationsStatus
          value:
            - - name: operationName
                value: string
              - name: operationState
                value: string
              - name: id
                value: string
    - name: identity
      value:
        - name: type
          value: string
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: userAssignedIdentities
          value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>instances</code> resource.

```sql
/*+ update */
UPDATE azure.scom.instances
SET 
identity = '{{ identity }}',
tags = '{{ tags }}'
WHERE 
instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure.scom.instances
WHERE instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
