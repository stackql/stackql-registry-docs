---
title: provisioning_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - provisioning_configs
  - baremetalsolution
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

Creates, updates, deletes, gets or lists a <code>provisioning_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provisioning_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.baremetalsolution.provisioning_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The system-generated name of the provisioning config. This follows the UUID format. |
| <CopyableCode code="cloudConsoleUri" /> | `string` | Output only. URI to Cloud Console UI view of this provisioning config. |
| <CopyableCode code="customId" /> | `string` | Optional. The user-defined identifier of the provisioning config. |
| <CopyableCode code="email" /> | `string` | Email provided to send a confirmation with provisioning config to. Deprecated in favour of email field in request messages. |
| <CopyableCode code="handoverServiceAccount" /> | `string` | A service account to enable customers to access instance credentials upon handover. |
| <CopyableCode code="instances" /> | `array` | Instances to be created. |
| <CopyableCode code="location" /> | `string` | Optional. Location name of this ProvisioningConfig. It is optional only for Intake UI transition period. |
| <CopyableCode code="networks" /> | `array` | Networks to be created. |
| <CopyableCode code="pod" /> | `string` | Optional. Pod name. Pod is an independent part of infrastructure. Instance can be connected to the assets (networks, volumes, nfsshares) allocated in the same pod only. |
| <CopyableCode code="state" /> | `string` | Output only. State of ProvisioningConfig. |
| <CopyableCode code="statusMessage" /> | `string` | Optional status messages associated with the FAILED state. |
| <CopyableCode code="ticketId" /> | `string` | A generated ticket id to track provisioning request. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update timestamp. |
| <CopyableCode code="volumes" /> | `array` | Volumes to be created. |
| <CopyableCode code="vpcScEnabled" /> | `boolean` | If true, VPC SC is enabled for the cluster. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, provisioningConfigsId" /> | Get ProvisioningConfig by name. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create new ProvisioningConfig. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, provisioningConfigsId" /> | Update existing ProvisioningConfig. |
| <CopyableCode code="submit" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Submit a provisiong configuration for a given project. |

## `SELECT` examples

Get ProvisioningConfig by name.

```sql
SELECT
name,
cloudConsoleUri,
customId,
email,
handoverServiceAccount,
instances,
location,
networks,
pod,
state,
statusMessage,
ticketId,
updateTime,
volumes,
vpcScEnabled
FROM google.baremetalsolution.provisioning_configs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND provisioningConfigsId = '{{ provisioningConfigsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>provisioning_configs</code> resource.

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
INSERT INTO google.baremetalsolution.provisioning_configs (
locationsId,
projectsId,
instances,
networks,
volumes,
ticketId,
handoverServiceAccount,
email,
location,
vpcScEnabled,
statusMessage,
customId,
pod
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ instances }}',
'{{ networks }}',
'{{ volumes }}',
'{{ ticketId }}',
'{{ handoverServiceAccount }}',
'{{ email }}',
'{{ location }}',
{{ vpcScEnabled }},
'{{ statusMessage }}',
'{{ customId }}',
'{{ pod }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: instances
      value:
        - - name: name
            value: string
          - name: id
            value: string
          - name: instanceType
            value: string
          - name: hyperthreading
            value: boolean
          - name: osImage
            value: string
          - name: clientNetwork
            value:
              - name: networkId
                value: string
              - name: address
                value: string
              - name: existingNetworkId
                value: string
          - name: userNote
            value: string
          - name: accountNetworksEnabled
            value: boolean
          - name: networkConfig
            value: string
          - name: networkTemplate
            value: string
          - name: logicalInterfaces
            value:
              - - name: logicalNetworkInterfaces
                  value:
                    - - name: network
                        value: string
                      - name: ipAddress
                        value: string
                      - name: defaultGateway
                        value: boolean
                      - name: networkType
                        value: string
                      - name: id
                        value: string
                - name: name
                  value: string
                - name: interfaceIndex
                  value: integer
          - name: sshKeyNames
            value:
              - string
          - name: kmsKeyVersion
            value: string
    - name: networks
      value:
        - - name: name
            value: string
          - name: id
            value: string
          - name: type
            value: string
          - name: bandwidth
            value: string
          - name: vlanAttachments
            value:
              - - name: id
                  value: string
                - name: pairingKey
                  value: string
          - name: vrf
            value: string
          - name: cidr
            value: string
          - name: serviceCidr
            value: string
          - name: userNote
            value: string
          - name: gcpService
            value: string
          - name: vlanSameProject
            value: boolean
          - name: jumboFramesEnabled
            value: boolean
    - name: volumes
      value:
        - - name: name
            value: string
          - name: id
            value: string
          - name: snapshotsEnabled
            value: boolean
          - name: type
            value: string
          - name: protocol
            value: string
          - name: sizeGb
            value: integer
          - name: lunRanges
            value:
              - - name: quantity
                  value: integer
                - name: sizeGb
                  value: integer
          - name: machineIds
            value:
              - string
          - name: nfsExports
            value:
              - - name: networkId
                  value: string
                - name: machineId
                  value: string
                - name: cidr
                  value: string
                - name: permissions
                  value: string
                - name: noRootSquash
                  value: boolean
                - name: allowSuid
                  value: boolean
                - name: allowDev
                  value: boolean
          - name: userNote
            value: string
          - name: gcpService
            value: string
          - name: performanceTier
            value: string
    - name: ticketId
      value: string
    - name: handoverServiceAccount
      value: string
    - name: email
      value: string
    - name: state
      value: string
    - name: location
      value: string
    - name: updateTime
      value: string
    - name: cloudConsoleUri
      value: string
    - name: vpcScEnabled
      value: boolean
    - name: statusMessage
      value: string
    - name: customId
      value: string
    - name: pod
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>provisioning_configs</code> resource.

```sql
/*+ update */
UPDATE google.baremetalsolution.provisioning_configs
SET 
instances = '{{ instances }}',
networks = '{{ networks }}',
volumes = '{{ volumes }}',
ticketId = '{{ ticketId }}',
handoverServiceAccount = '{{ handoverServiceAccount }}',
email = '{{ email }}',
location = '{{ location }}',
vpcScEnabled = true|false,
statusMessage = '{{ statusMessage }}',
customId = '{{ customId }}',
pod = '{{ pod }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND provisioningConfigsId = '{{ provisioningConfigsId }}';
```
