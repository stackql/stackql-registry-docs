---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - service_fabric_managed_clusters
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

Creates, updates, deletes, gets or lists a <code>applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_managed_clusters.applications" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_applications', value: 'view', },
        { label: 'applications', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource identifier. |
| <CopyableCode code="name" /> | `text` | Azure resource name. |
| <CopyableCode code="applicationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Describes the managed identities for an Azure resource. |
| <CopyableCode code="location" /> | `text` | Resource location depends on the parent resource. |
| <CopyableCode code="managed_identities" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Azure resource tags. |
| <CopyableCode code="type" /> | `text` | Azure resource type. |
| <CopyableCode code="upgrade_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource identifier. |
| <CopyableCode code="name" /> | `string` | Azure resource name. |
| <CopyableCode code="identity" /> | `object` | Describes the managed identities for an Azure resource. |
| <CopyableCode code="location" /> | `string` | Resource location depends on the parent resource. |
| <CopyableCode code="properties" /> | `object` | The application resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Azure resource tags. |
| <CopyableCode code="type" /> | `string` | Azure resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Get a Service Fabric managed application resource created or in the process of being created in the Service Fabric cluster resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets all managed application resources created or in the process of being created in the Service Fabric cluster resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Create or update a Service Fabric managed application resource with the specified name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Delete a Service Fabric managed application resource with the specified name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Updates the tags of an application resource of a given managed cluster. |
| <CopyableCode code="read_upgrade" /> | `EXEC` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Get the status of the latest application upgrade. It will query the cluster to find the status of the latest application upgrade. |
| <CopyableCode code="resume_upgrade" /> | `EXEC` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Send a request to resume the current application upgrade. This will resume the application upgrade from where it was paused. |
| <CopyableCode code="start_rollback" /> | `EXEC` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Send a request to start a rollback of the current application upgrade. This will start rolling back the application to the previous version. |

## `SELECT` examples

Gets all managed application resources created or in the process of being created in the Service Fabric cluster resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_applications', value: 'view', },
        { label: 'applications', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
applicationName,
clusterName,
identity,
location,
managed_identities,
parameters,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
tags,
type,
upgrade_policy,
version
FROM azure.service_fabric_managed_clusters.vw_applications
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
systemData,
tags,
type
FROM azure.service_fabric_managed_clusters.applications
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>applications</code> resource.

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
INSERT INTO azure.service_fabric_managed_clusters.applications (
applicationName,
clusterName,
resourceGroupName,
subscriptionId,
identity,
properties,
location,
tags,
systemData
)
SELECT 
'{{ applicationName }}',
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ identity }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}',
'{{ systemData }}'
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
          value: []
        - name: userAssignedIdentities
          value: []
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: version
          value: []
        - name: parameters
          value: []
        - name: upgradePolicy
          value:
            - name: applicationHealthPolicy
              value:
                - name: considerWarningAsError
                  value: boolean
                - name: maxPercentUnhealthyDeployedApplications
                  value: integer
                - name: defaultServiceTypeHealthPolicy
                  value:
                    - name: maxPercentUnhealthyServices
                      value: integer
                    - name: maxPercentUnhealthyPartitionsPerService
                      value: integer
                    - name: maxPercentUnhealthyReplicasPerPartition
                      value: integer
                - name: serviceTypeHealthPolicyMap
                  value: []
            - name: forceRestart
              value: []
            - name: rollingUpgradeMonitoringPolicy
              value:
                - name: failureAction
                  value: string
                - name: healthCheckWaitDuration
                  value: []
                - name: healthCheckStableDuration
                  value: []
                - name: healthCheckRetryTimeout
                  value: []
                - name: upgradeTimeout
                  value: []
                - name: upgradeDomainTimeout
                  value: []
            - name: instanceCloseDelayDuration
              value: integer
            - name: upgradeMode
              value: []
            - name: upgradeReplicaSetCheckTimeout
              value: integer
            - name: recreateApplication
              value: boolean
        - name: managedIdentities
          value:
            - - name: name
                value: string
              - name: principalId
                value: string
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

Updates a <code>applications</code> resource.

```sql
/*+ update */
UPDATE azure.service_fabric_managed_clusters.applications
SET 
tags = '{{ tags }}'
WHERE 
applicationName = '{{ applicationName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>applications</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_fabric_managed_clusters.applications
WHERE applicationName = '{{ applicationName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
