---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_managed_clusters.services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_services', value: 'view', },
        { label: 'services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource identifier. |
| <CopyableCode code="name" /> | `text` | Azure resource name. |
| <CopyableCode code="applicationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="correlation_scheme" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_move_cost" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location depends on the parent resource. |
| <CopyableCode code="partition_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="placement_constraints" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scaling_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_dns_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_load_metrics" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_package_activation_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_placement_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_type_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Azure resource tags. |
| <CopyableCode code="type" /> | `text` | Azure resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource identifier. |
| <CopyableCode code="name" /> | `string` | Azure resource name. |
| <CopyableCode code="location" /> | `string` | Resource location depends on the parent resource. |
| <CopyableCode code="properties" /> | `object` | The service resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Azure resource tags. |
| <CopyableCode code="type" /> | `string` | Azure resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationName, clusterName, resourceGroupName, serviceName, subscriptionId" /> | Get a Service Fabric service resource created or in the process of being created in the Service Fabric managed application resource. |
| <CopyableCode code="list_by_applications" /> | `SELECT` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Gets all service resources created or in the process of being created in the Service Fabric managed application resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationName, clusterName, resourceGroupName, serviceName, subscriptionId" /> | Create or update a Service Fabric managed service resource with the specified name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationName, clusterName, resourceGroupName, serviceName, subscriptionId" /> | Delete a Service Fabric managed service resource with the specified name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="applicationName, clusterName, resourceGroupName, serviceName, subscriptionId" /> | Updates the tags of a service resource of a given managed cluster. |

## `SELECT` examples

Gets all service resources created or in the process of being created in the Service Fabric managed application resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_services', value: 'view', },
        { label: 'services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
applicationName,
clusterName,
correlation_scheme,
default_move_cost,
location,
partition_description,
placement_constraints,
provisioning_state,
resourceGroupName,
scaling_policies,
serviceName,
service_dns_name,
service_kind,
service_load_metrics,
service_package_activation_mode,
service_placement_policies,
service_type_name,
subscriptionId,
system_data,
tags,
type
FROM azure.service_fabric_managed_clusters.vw_services
WHERE applicationName = '{{ applicationName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
systemData,
tags,
type
FROM azure.service_fabric_managed_clusters.services
WHERE applicationName = '{{ applicationName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>services</code> resource.

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
INSERT INTO azure.service_fabric_managed_clusters.services (
applicationName,
clusterName,
resourceGroupName,
serviceName,
subscriptionId,
properties,
location,
tags,
systemData
)
SELECT 
'{{ applicationName }}',
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
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
    - name: properties
      value:
        - name: placementConstraints
          value: string
        - name: correlationScheme
          value: []
        - name: serviceLoadMetrics
          value: []
        - name: servicePlacementPolicies
          value: []
        - name: defaultMoveCost
          value: []
        - name: scalingPolicies
          value: []
        - name: provisioningState
          value: string
        - name: serviceKind
          value: []
        - name: serviceTypeName
          value: string
        - name: partitionDescription
          value:
            - name: partitionScheme
              value: []
        - name: servicePackageActivationMode
          value: string
        - name: serviceDnsName
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

Updates a <code>services</code> resource.

```sql
/*+ update */
UPDATE azure.service_fabric_managed_clusters.services
SET 
tags = '{{ tags }}'
WHERE 
applicationName = '{{ applicationName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_fabric_managed_clusters.services
WHERE applicationName = '{{ applicationName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
