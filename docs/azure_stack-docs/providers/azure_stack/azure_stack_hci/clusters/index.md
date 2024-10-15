---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.clusters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_clusters', value: 'view', },
        { label: 'clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aad_application_object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="aad_client_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="aad_service_principal_object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="aad_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_model" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_management_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectivity_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="desired_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="isolated_vm_attestation_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_billing_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_sync_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="reported_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_provider_object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="software_assurance_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="trial_days_remaining" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Cluster properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get HCI cluster. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all HCI clusters in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all HCI clusters in a subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Create an HCI cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Delete an HCI cluster. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Update an HCI cluster. |
| <CopyableCode code="extend_software_assurance_benefit" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Extends Software Assurance Benefit to a cluster |
| <CopyableCode code="upload_certificate" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Upload certificate. |

## `SELECT` examples

List all HCI clusters in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_clusters', value: 'view', },
        { label: 'clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
aad_application_object_id,
aad_client_id,
aad_service_principal_object_id,
aad_tenant_id,
billing_model,
cloud_id,
cloud_management_endpoint,
clusterName,
connectivity_status,
desired_properties,
identity,
isolated_vm_attestation_configuration,
last_billing_timestamp,
last_sync_timestamp,
location,
provisioning_state,
registration_timestamp,
reported_properties,
resourceGroupName,
resource_provider_object_id,
service_endpoint,
software_assurance_properties,
status,
subscriptionId,
tags,
trial_days_remaining
FROM azure_stack.azure_stack_hci.vw_clusters
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
FROM azure_stack.azure_stack_hci.clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clusters</code> resource.

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
INSERT INTO azure_stack.azure_stack_hci.clusters (
clusterName,
resourceGroupName,
subscriptionId,
tags,
location,
identity,
properties
)
SELECT 
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
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
        - name: status
          value: string
        - name: connectivityStatus
          value: string
        - name: cloudId
          value: string
        - name: cloudManagementEndpoint
          value: string
        - name: aadClientId
          value: string
        - name: aadTenantId
          value: string
        - name: aadApplicationObjectId
          value: string
        - name: aadServicePrincipalObjectId
          value: string
        - name: softwareAssuranceProperties
          value:
            - name: softwareAssuranceStatus
              value: string
            - name: softwareAssuranceIntent
              value: string
            - name: lastUpdated
              value: string
        - name: desiredProperties
          value:
            - name: windowsServerSubscription
              value: string
            - name: diagnosticLevel
              value: string
        - name: reportedProperties
          value:
            - name: clusterName
              value: string
            - name: clusterId
              value: string
            - name: clusterVersion
              value: string
            - name: nodes
              value:
                - - name: name
                    value: string
                  - name: id
                    value: number
                  - name: windowsServerSubscription
                    value: string
                  - name: nodeType
                    value: string
                  - name: ehcResourceId
                    value: string
                  - name: manufacturer
                    value: string
                  - name: model
                    value: string
                  - name: osName
                    value: string
                  - name: osVersion
                    value: string
                  - name: osDisplayVersion
                    value: string
                  - name: serialNumber
                    value: string
                  - name: coreCount
                    value: number
                  - name: memoryInGiB
                    value: number
                  - name: lastLicensingTimestamp
                    value: string
                  - name: oemActivation
                    value: string
            - name: lastUpdated
              value: string
            - name: imdsAttestation
              value: string
            - name: diagnosticLevel
              value: string
            - name: supportedCapabilities
              value:
                - string
            - name: clusterType
              value: string
            - name: manufacturer
              value: string
            - name: oemActivation
              value: string
        - name: isolatedVmAttestationConfiguration
          value:
            - name: attestationResourceId
              value: string
            - name: relyingPartyServiceEndpoint
              value: string
            - name: attestationServiceEndpoint
              value: string
        - name: trialDaysRemaining
          value: number
        - name: billingModel
          value: string
        - name: registrationTimestamp
          value: string
        - name: lastSyncTimestamp
          value: string
        - name: lastBillingTimestamp
          value: string
        - name: serviceEndpoint
          value: string
        - name: resourceProviderObjectId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>clusters</code> resource.

```sql
/*+ update */
UPDATE azure_stack.azure_stack_hci.clusters
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack_hci.clusters
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
