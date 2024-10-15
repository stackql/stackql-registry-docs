---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - app_service
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

Creates, updates, deletes, gets or lists a <code>environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name/identifier of the diagnostics. |
| <CopyableCode code="diagnosticsOutput" /> | `string` | Diagnostics output. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Get the properties of an App Service Environment. |
| <CopyableCode code="get_diagnostics" /> | `SELECT` | <CopyableCode code="diagnosticsName, name, resourceGroupName, subscriptionId" /> | Description for Get a diagnostics item for an App Service Environment. |
| <CopyableCode code="get_inbound_network_dependencies_endpoints" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Get the network endpoints of all inbound dependencies of an App Service Environment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for Get all App Service Environments for a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for Get all App Service Environments in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Create or update an App Service Environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Delete an App Service Environment. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Create or update an App Service Environment. |
| <CopyableCode code="approve_or_reject_private_endpoint_connection" /> | `EXEC` | <CopyableCode code="name, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Description for Approves or rejects a private endpoint connection |
| <CopyableCode code="change_vnet" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__id" /> | Description for Move an App Service Environment to a different VNET. |
| <CopyableCode code="reboot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Reboot all machines in an App Service Environment. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Resume an App Service Environment. |
| <CopyableCode code="suspend" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Suspend an App Service Environment. |
| <CopyableCode code="test_upgrade_available_notification" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Initiate an upgrade of an App Service Environment if one is available. |

## `SELECT` examples

Description for Get all App Service Environments for a subscription.


```sql
SELECT
name,
diagnosticsOutput
FROM azure.app_service.environments
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environments</code> resource.

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
INSERT INTO azure.app_service.environments (
name,
resourceGroupName,
subscriptionId,
kind,
location,
tags,
properties
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ location }}',
'{{ tags }}',
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
    - name: kind
      value: string
    - name: location
      value: string
    - name: type
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: status
          value: string
        - name: virtualNetwork
          value:
            - name: id
              value: string
            - name: name
              value: string
            - name: type
              value: string
            - name: subnet
              value: string
        - name: internalLoadBalancingMode
          value: string
        - name: multiSize
          value: string
        - name: multiRoleCount
          value: integer
        - name: ipsslAddressCount
          value: integer
        - name: dnsSuffix
          value: string
        - name: maximumNumberOfMachines
          value: integer
        - name: frontEndScaleFactor
          value: integer
        - name: suspended
          value: boolean
        - name: clusterSettings
          value:
            - - name: name
                value: string
              - name: value
                value: string
        - name: userWhitelistedIpRanges
          value:
            - string
        - name: hasLinuxWorkers
          value: boolean
        - name: upgradePreference
          value: string
        - name: dedicatedHostCount
          value: integer
        - name: zoneRedundant
          value: boolean
        - name: customDnsSuffixConfiguration
          value:
            - name: id
              value: string
            - name: name
              value: string
            - name: kind
              value: string
            - name: type
              value: string
            - name: properties
              value:
                - name: provisioningState
                  value: string
                - name: provisioningDetails
                  value: string
                - name: dnsSuffix
                  value: string
                - name: certificateUrl
                  value: string
                - name: keyVaultReferenceIdentity
                  value: string
        - name: networkingConfiguration
          value:
            - name: id
              value: string
            - name: name
              value: string
            - name: kind
              value: string
            - name: type
              value: string
            - name: properties
              value:
                - name: windowsOutboundIpAddresses
                  value:
                    - string
                - name: linuxOutboundIpAddresses
                  value:
                    - string
                - name: externalInboundIpAddresses
                  value:
                    - string
                - name: internalInboundIpAddresses
                  value:
                    - string
                - name: allowNewPrivateEndpointConnections
                  value: boolean
                - name: ftpEnabled
                  value: boolean
                - name: remoteDebugEnabled
                  value: boolean
                - name: inboundIpAddressOverride
                  value: string
        - name: upgradeAvailability
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>environments</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.environments
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>environments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.environments
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
