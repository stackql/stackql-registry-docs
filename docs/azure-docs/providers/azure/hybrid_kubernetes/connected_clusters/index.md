---
title: connected_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_clusters
  - hybrid_kubernetes
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

Creates, updates, deletes, gets or lists a <code>connected_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connected_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_kubernetes.connected_clusters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connected_clusters', value: 'view', },
        { label: 'connected_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aad_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_public_key_certificate" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="arc_agent_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="arc_agentry_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_hybrid_benefit" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectivity_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="distribution" /> | `text` | field from the `properties` object |
| <CopyableCode code="distribution_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the connected cluster. |
| <CopyableCode code="infrastructure" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Indicates the kind of Arc connected cluster based on host infrastructure. |
| <CopyableCode code="kubernetes_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_connectivity_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="managed_identity_certificate_expiration_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="miscellaneous_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="offering" /> | `text` | field from the `properties` object |
| <CopyableCode code="oidc_issuer_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_scope_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="total_core_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_node_count" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the connected cluster. |
| <CopyableCode code="kind" /> | `string` | Indicates the kind of Arc connected cluster based on host infrastructure. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the connected cluster. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified connected cluster, including name, identity, properties, and additional cluster details. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | API to enumerate registered connected K8s clusters under a Resource Group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | API to enumerate registered connected K8s clusters under a Subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__identity, data__properties" /> | API to register a new Kubernetes cluster and create a tracked resource in Azure Resource Manager (ARM). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Delete a connected cluster, removing the tracked resource in Azure Resource Manager (ARM). |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | API to update certain properties of the connected cluster resource |

## `SELECT` examples

API to enumerate registered connected K8s clusters under a Subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connected_clusters', value: 'view', },
        { label: 'connected_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
aad_profile,
agent_public_key_certificate,
agent_version,
arc_agent_profile,
arc_agentry_configurations,
azure_hybrid_benefit,
clusterName,
connectivity_status,
distribution,
distribution_version,
gateway,
identity,
infrastructure,
kind,
kubernetes_version,
last_connectivity_time,
location,
managed_identity_certificate_expiration_time,
miscellaneous_properties,
offering,
oidc_issuer_profile,
private_link_scope_resource_id,
private_link_state,
provisioning_state,
resourceGroupName,
security_profile,
subscriptionId,
system_data,
tags,
total_core_count,
total_node_count
FROM azure.hybrid_kubernetes.vw_connected_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
kind,
location,
properties,
systemData,
tags
FROM azure.hybrid_kubernetes.connected_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connected_clusters</code> resource.

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
INSERT INTO azure.hybrid_kubernetes.connected_clusters (
clusterName,
resourceGroupName,
subscriptionId,
data__identity,
data__properties,
identity,
kind,
properties,
tags,
location
)
SELECT 
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__identity }}',
'{{ data__properties }}',
'{{ identity }}',
'{{ kind }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
    - name: kind
      value: []
    - name: properties
      value:
        - name: agentPublicKeyCertificate
          value: string
        - name: kubernetesVersion
          value: string
        - name: totalNodeCount
          value: integer
        - name: totalCoreCount
          value: integer
        - name: agentVersion
          value: string
        - name: provisioningState
          value: []
        - name: distribution
          value: string
        - name: distributionVersion
          value: string
        - name: infrastructure
          value: string
        - name: offering
          value: string
        - name: managedIdentityCertificateExpirationTime
          value: string
        - name: lastConnectivityTime
          value: string
        - name: connectivityStatus
          value: string
        - name: privateLinkState
          value: string
        - name: privateLinkScopeResourceId
          value: string
        - name: azureHybridBenefit
          value: string
        - name: aadProfile
          value:
            - name: enableAzureRBAC
              value: boolean
            - name: adminGroupObjectIDs
              value:
                - string
            - name: tenantID
              value: string
        - name: arcAgentProfile
          value:
            - name: desiredAgentVersion
              value: string
            - name: agentAutoUpgrade
              value: string
            - name: systemComponents
              value:
                - - name: type
                    value: string
                  - name: userSpecifiedVersion
                    value: string
                  - name: majorVersion
                    value: integer
                  - name: currentVersion
                    value: string
            - name: agentErrors
              value:
                - - name: message
                    value: string
                  - name: severity
                    value: string
                  - name: component
                    value: string
                  - name: time
                    value: string
            - name: agentState
              value: string
        - name: securityProfile
          value:
            - name: workloadIdentity
              value:
                - name: enabled
                  value: boolean
        - name: oidcIssuerProfile
          value:
            - name: enabled
              value: boolean
            - name: issuerUrl
              value: string
            - name: selfHostedIssuerUrl
              value: string
        - name: gateway
          value:
            - name: enabled
              value: boolean
            - name: resourceId
              value: string
        - name: arcAgentryConfigurations
          value:
            - - name: feature
                value: string
              - name: settings
                value: object
              - name: protectedSettings
                value: object
        - name: miscellaneousProperties
          value: object
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
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>connected_clusters</code> resource.

```sql
/*+ update */
UPDATE azure.hybrid_kubernetes.connected_clusters
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>connected_clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_kubernetes.connected_clusters
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
