---
title: managed_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_environments
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>managed_environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.managed_environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="kind" /> | `string` | Kind of the Environment. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Managed environment resource specific properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Get the properties of a Managed Environment used to host container apps. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all the Managed Environments in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all Managed Environments for a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Creates or updates a Managed Environment used to host container apps. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Delete a Managed Environment if it does not have any container apps. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Patches a Managed Environment using JSON Merge Patch |

## `SELECT` examples

Get all Managed Environments for a subscription.


```sql
SELECT
identity,
kind,
location,
properties,
tags
FROM azure.container_apps.managed_environments
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_environments</code> resource.

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
INSERT INTO azure.container_apps.managed_environments (
environmentName,
resourceGroupName,
subscriptionId,
tags,
location,
kind,
identity,
properties
)
SELECT 
'{{ environmentName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ kind }}',
'{{ identity }}',
'{{ properties }}'
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
    - name: kind
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
          value: []
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: daprAIInstrumentationKey
          value: string
        - name: daprAIConnectionString
          value: string
        - name: vnetConfiguration
          value:
            - name: internal
              value: boolean
            - name: infrastructureSubnetId
              value: string
            - name: dockerBridgeCidr
              value: string
            - name: platformReservedCidr
              value: string
            - name: platformReservedDnsIP
              value: string
        - name: deploymentErrors
          value: string
        - name: defaultDomain
          value: string
        - name: staticIp
          value: string
        - name: appLogsConfiguration
          value:
            - name: destination
              value: string
            - name: logAnalyticsConfiguration
              value:
                - name: customerId
                  value: string
                - name: sharedKey
                  value: string
                - name: dynamicJsonColumns
                  value: boolean
        - name: appInsightsConfiguration
          value:
            - name: connectionString
              value: string
        - name: openTelemetryConfiguration
          value:
            - name: destinationsConfiguration
              value:
                - name: dataDogConfiguration
                  value:
                    - name: site
                      value: string
                    - name: key
                      value: string
                - name: otlpConfigurations
                  value:
                    - - name: name
                        value: string
                      - name: endpoint
                        value: string
                      - name: insecure
                        value: boolean
                      - name: headers
                        value:
                          - - name: key
                              value: string
                            - name: value
                              value: string
            - name: tracesConfiguration
              value:
                - name: destinations
                  value:
                    - string
            - name: logsConfiguration
              value:
                - name: destinations
                  value:
                    - string
            - name: metricsConfiguration
              value:
                - name: destinations
                  value:
                    - string
        - name: zoneRedundant
          value: boolean
        - name: customDomainConfiguration
          value:
            - name: customDomainVerificationId
              value: string
            - name: dnsSuffix
              value: string
            - name: certificateKeyVaultProperties
              value:
                - name: identity
                  value: string
                - name: keyVaultUrl
                  value: string
            - name: certificateValue
              value: string
            - name: certificatePassword
              value: string
            - name: expirationDate
              value: string
            - name: thumbprint
              value: string
            - name: subjectName
              value: string
        - name: eventStreamEndpoint
          value: string
        - name: workloadProfiles
          value:
            - - name: name
                value: []
              - name: workloadProfileType
                value: []
              - name: minimumCount
                value: integer
              - name: maximumCount
                value: integer
        - name: kedaConfiguration
          value:
            - name: version
              value: string
        - name: daprConfiguration
          value:
            - name: version
              value: string
        - name: infrastructureResourceGroup
          value: string
        - name: peerAuthentication
          value:
            - name: mtls
              value:
                - name: enabled
                  value: boolean
        - name: peerTrafficConfiguration
          value:
            - name: encryption
              value:
                - name: enabled
                  value: boolean
        - name: privateEndpointConnections
          value:
            - - name: properties
                value:
                  - name: groupIds
                    value:
                      - string
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: []
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: provisioningState
                    value: []
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
        - name: publicNetworkAccess
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>managed_environments</code> resource.

```sql
/*+ update */
UPDATE azure.container_apps.managed_environments
SET 
tags = '{{ tags }}',
location = '{{ location }}',
kind = '{{ kind }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>managed_environments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.managed_environments
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
