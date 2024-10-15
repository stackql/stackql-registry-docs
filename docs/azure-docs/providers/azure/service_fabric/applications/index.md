---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - service_fabric
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric.applications" /></td></tr>
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
| <CopyableCode code="etag" /> | `text` | Azure resource etag. |
| <CopyableCode code="identity" /> | `text` | Describes the managed identities for an Azure resource. |
| <CopyableCode code="location" /> | `text` | It will be deprecated in New API, resource location depends on the parent resource. |
| <CopyableCode code="managed_identities" /> | `text` | field from the `properties` object |
| <CopyableCode code="maximum_nodes" /> | `text` | field from the `properties` object |
| <CopyableCode code="metrics" /> | `text` | field from the `properties` object |
| <CopyableCode code="minimum_nodes" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="remove_application_capacity" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Azure resource tags. |
| <CopyableCode code="type" /> | `text` | Azure resource type. |
| <CopyableCode code="type_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="type_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="upgrade_policy" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource identifier. |
| <CopyableCode code="name" /> | `string` | Azure resource name. |
| <CopyableCode code="etag" /> | `string` | Azure resource etag. |
| <CopyableCode code="identity" /> | `object` | Describes the managed identities for an Azure resource. |
| <CopyableCode code="location" /> | `string` | It will be deprecated in New API, resource location depends on the parent resource. |
| <CopyableCode code="properties" /> | `object` | The application resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Azure resource tags. |
| <CopyableCode code="type" /> | `string` | Azure resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Get a Service Fabric application resource created or in the process of being created in the Service Fabric cluster resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets all application resources created or in the process of being created in the Service Fabric cluster resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Create or update a Service Fabric application resource with the specified name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Delete a Service Fabric application resource with the specified name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Update a Service Fabric application resource with the specified name. |

## `SELECT` examples

Gets all application resources created or in the process of being created in the Service Fabric cluster resource.

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
etag,
identity,
location,
managed_identities,
maximum_nodes,
metrics,
minimum_nodes,
parameters,
provisioning_state,
remove_application_capacity,
resourceGroupName,
subscriptionId,
system_data,
tags,
type,
type_name,
type_version,
upgrade_policy
FROM azure.service_fabric.vw_applications
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
etag,
identity,
location,
properties,
systemData,
tags,
type
FROM azure.service_fabric.applications
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
INSERT INTO azure.service_fabric.applications (
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
        - name: typeVersion
          value: []
        - name: parameters
          value: []
        - name: upgradePolicy
          value:
            - name: upgradeReplicaSetCheckTimeout
              value: string
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
            - name: upgradeMode
              value: []
            - name: recreateApplication
              value: boolean
        - name: minimumNodes
          value: integer
        - name: maximumNodes
          value: integer
        - name: removeApplicationCapacity
          value: boolean
        - name: metrics
          value: []
        - name: managedIdentities
          value:
            - - name: name
                value: string
              - name: principalId
                value: string
        - name: provisioningState
          value: string
        - name: typeName
          value: []
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
    - name: etag
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

Updates a <code>applications</code> resource.

```sql
/*+ update */
UPDATE azure.service_fabric.applications
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}',
systemData = '{{ systemData }}'
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
DELETE FROM azure.service_fabric.applications
WHERE applicationName = '{{ applicationName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
