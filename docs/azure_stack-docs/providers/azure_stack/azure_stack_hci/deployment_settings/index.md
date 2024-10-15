---
title: deployment_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_settings
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

Creates, updates, deletes, gets or lists a <code>deployment_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.deployment_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deployment_settings', value: 'view', },
        { label: 'deployment_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="arc_node_resource_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="deploymentSettingsName" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="reported_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | DeploymentSetting properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, deploymentSettingsName, resourceGroupName, subscriptionId" /> | Get a DeploymentSetting |
| <CopyableCode code="list_by_clusters" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | List DeploymentSetting resources by Clusters |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, deploymentSettingsName, resourceGroupName, subscriptionId" /> | Create a DeploymentSetting |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, deploymentSettingsName, resourceGroupName, subscriptionId" /> | Delete a DeploymentSetting |

## `SELECT` examples

List DeploymentSetting resources by Clusters

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deployment_settings', value: 'view', },
        { label: 'deployment_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
arc_node_resource_ids,
clusterName,
deploymentSettingsName,
deployment_configuration,
deployment_mode,
provisioning_state,
reported_properties,
resourceGroupName,
subscriptionId
FROM azure_stack.azure_stack_hci.vw_deployment_settings
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_stack.azure_stack_hci.deployment_settings
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployment_settings</code> resource.

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
INSERT INTO azure_stack.azure_stack_hci.deployment_settings (
clusterName,
deploymentSettingsName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ clusterName }}',
'{{ deploymentSettingsName }}',
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
          value: []
        - name: arcNodeResourceIds
          value:
            - string
        - name: deploymentMode
          value: []
        - name: deploymentConfiguration
          value:
            - name: version
              value: string
            - name: scaleUnits
              value:
                - - name: deploymentData
                    value:
                      - name: securitySettings
                        value:
                          - name: hvciProtection
                            value: boolean
                          - name: drtmProtection
                            value: boolean
                          - name: driftControlEnforced
                            value: boolean
                          - name: credentialGuardEnforced
                            value: boolean
                          - name: smbSigningEnforced
                            value: boolean
                          - name: smbClusterEncryption
                            value: boolean
                          - name: sideChannelMitigationEnforced
                            value: boolean
                          - name: bitlockerBootVolume
                            value: boolean
                          - name: bitlockerDataVolumes
                            value: boolean
                          - name: wdacEnforced
                            value: boolean
                      - name: observability
                        value:
                          - name: streamingDataClient
                            value: boolean
                          - name: euLocation
                            value: boolean
                          - name: episodicDataUpload
                            value: boolean
                      - name: cluster
                        value:
                          - name: name
                            value: string
                          - name: witnessType
                            value: string
                          - name: witnessPath
                            value: string
                          - name: cloudAccountName
                            value: string
                          - name: azureServiceEndpoint
                            value: string
                      - name: storage
                        value:
                          - name: configurationMode
                            value: string
                      - name: namingPrefix
                        value: string
                      - name: domainFqdn
                        value: string
                      - name: infrastructureNetwork
                        value:
                          - - name: subnetMask
                              value: string
                            - name: gateway
                              value: string
                            - name: ipPools
                              value:
                                - - name: startingAddress
                                    value: string
                                  - name: endingAddress
                                    value: string
                            - name: dnsServers
                              value:
                                - string
                            - name: useDhcp
                              value: boolean
                      - name: physicalNodes
                        value:
                          - - name: name
                              value: string
                            - name: ipv4Address
                              value: string
                      - name: hostNetwork
                        value:
                          - name: intents
                            value:
                              - - name: name
                                  value: string
                                - name: trafficType
                                  value:
                                    - string
                                - name: adapter
                                  value:
                                    - string
                                - name: overrideVirtualSwitchConfiguration
                                  value: boolean
                                - name: virtualSwitchConfigurationOverrides
                                  value:
                                    - name: enableIov
                                      value: string
                                    - name: loadBalancingAlgorithm
                                      value: string
                                - name: overrideQosPolicy
                                  value: boolean
                                - name: qosPolicyOverrides
                                  value:
                                    - name: priorityValue8021Action_Cluster
                                      value: string
                                    - name: priorityValue8021Action_SMB
                                      value: string
                                    - name: bandwidthPercentage_SMB
                                      value: string
                                - name: overrideAdapterProperty
                                  value: boolean
                                - name: adapterPropertyOverrides
                                  value:
                                    - name: jumboPacket
                                      value: string
                                    - name: networkDirect
                                      value: string
                                    - name: networkDirectTechnology
                                      value: string
                          - name: storageNetworks
                            value:
                              - - name: name
                                  value: string
                                - name: networkAdapterName
                                  value: string
                                - name: vlanId
                                  value: string
                          - name: storageConnectivitySwitchless
                            value: boolean
                          - name: enableStorageAutoIp
                            value: boolean
                      - name: adouPath
                        value: string
                      - name: secretsLocation
                        value: string
                      - name: optionalServices
                        value:
                          - name: customLocation
                            value: string
        - name: reportedProperties
          value:
            - name: validationStatus
              value:
                - name: status
                  value: string
                - name: steps
                  value:
                    - - name: name
                        value: string
                      - name: description
                        value: string
                      - name: fullStepIndex
                        value: string
                      - name: startTimeUtc
                        value: string
                      - name: endTimeUtc
                        value: string
                      - name: status
                        value: string
                      - name: steps
                        value:
                          - - name: name
                              value: string
                            - name: description
                              value: string
                            - name: fullStepIndex
                              value: string
                            - name: startTimeUtc
                              value: string
                            - name: endTimeUtc
                              value: string
                            - name: status
                              value: string
                            - name: steps
                              value:
                                - - name: name
                                    value: string
                                  - name: description
                                    value: string
                                  - name: fullStepIndex
                                    value: string
                                  - name: startTimeUtc
                                    value: string
                                  - name: endTimeUtc
                                    value: string
                                  - name: status
                                    value: string
                                  - name: steps
                                    value:
                                      - - name: name
                                          value: string
                                        - name: description
                                          value: string
                                        - name: fullStepIndex
                                          value: string
                                        - name: startTimeUtc
                                          value: string
                                        - name: endTimeUtc
                                          value: string
                                        - name: status
                                          value: string
                                        - name: steps
                                          value:
                                            - - name: name
                                                value: string
                                              - name: description
                                                value: string
                                              - name: fullStepIndex
                                                value: string
                                              - name: startTimeUtc
                                                value: string
                                              - name: endTimeUtc
                                                value: string
                                              - name: status
                                                value: string
                                              - name: steps
                                                value:
                                                  - - name: name
                                                      value: string
                                                    - name: description
                                                      value: string
                                                    - name: fullStepIndex
                                                      value: string
                                                    - name: startTimeUtc
                                                      value: string
                                                    - name: endTimeUtc
                                                      value: string
                                                    - name: status
                                                      value: string
                                                    - name: steps
                                                      value:
                                                        - - name: name
                                                            value: string
                                                          - name: description
                                                            value: string
                                                          - name: fullStepIndex
                                                            value: string
                                                          - name: startTimeUtc
                                                            value: string
                                                          - name: endTimeUtc
                                                            value: string
                                                          - name: status
                                                            value: string
                                                          - name: steps
                                                            value:
                                                              - []
                                                          - name: exception
                                                            value:
                                                              - string
                                                    - name: exception
                                                      value:
                                                        - string
                                              - name: exception
                                                value:
                                                  - string
                                        - name: exception
                                          value:
                                            - string
                                  - name: exception
                                    value:
                                      - string
                            - name: exception
                              value:
                                - string
                      - name: exception
                        value:
                          - string
            - name: deploymentStatus
              value:
                - name: status
                  value: string
                - name: steps
                  value:
                    - - name: name
                        value: string
                      - name: description
                        value: string
                      - name: fullStepIndex
                        value: string
                      - name: startTimeUtc
                        value: string
                      - name: endTimeUtc
                        value: string
                      - name: status
                        value: string
                      - name: steps
                        value:
                          - - name: name
                              value: string
                            - name: description
                              value: string
                            - name: fullStepIndex
                              value: string
                            - name: startTimeUtc
                              value: string
                            - name: endTimeUtc
                              value: string
                            - name: status
                              value: string
                            - name: steps
                              value:
                                - - name: name
                                    value: string
                                  - name: description
                                    value: string
                                  - name: fullStepIndex
                                    value: string
                                  - name: startTimeUtc
                                    value: string
                                  - name: endTimeUtc
                                    value: string
                                  - name: status
                                    value: string
                                  - name: steps
                                    value:
                                      - - name: name
                                          value: string
                                        - name: description
                                          value: string
                                        - name: fullStepIndex
                                          value: string
                                        - name: startTimeUtc
                                          value: string
                                        - name: endTimeUtc
                                          value: string
                                        - name: status
                                          value: string
                                        - name: steps
                                          value:
                                            - - name: name
                                                value: string
                                              - name: description
                                                value: string
                                              - name: fullStepIndex
                                                value: string
                                              - name: startTimeUtc
                                                value: string
                                              - name: endTimeUtc
                                                value: string
                                              - name: status
                                                value: string
                                              - name: steps
                                                value:
                                                  - - name: name
                                                      value: string
                                                    - name: description
                                                      value: string
                                                    - name: fullStepIndex
                                                      value: string
                                                    - name: startTimeUtc
                                                      value: string
                                                    - name: endTimeUtc
                                                      value: string
                                                    - name: status
                                                      value: string
                                                    - name: steps
                                                      value:
                                                        - - name: name
                                                            value: string
                                                          - name: description
                                                            value: string
                                                          - name: fullStepIndex
                                                            value: string
                                                          - name: startTimeUtc
                                                            value: string
                                                          - name: endTimeUtc
                                                            value: string
                                                          - name: status
                                                            value: string
                                                          - name: steps
                                                            value:
                                                              - []
                                                          - name: exception
                                                            value:
                                                              - string
                                                    - name: exception
                                                      value:
                                                        - string
                                              - name: exception
                                                value:
                                                  - string
                                        - name: exception
                                          value:
                                            - string
                                  - name: exception
                                    value:
                                      - string
                            - name: exception
                              value:
                                - string
                      - name: exception
                        value:
                          - string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>deployment_settings</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack_hci.deployment_settings
WHERE clusterName = '{{ clusterName }}'
AND deploymentSettingsName = '{{ deploymentSettingsName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
