---
title: open_shift_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - open_shift_clusters
  - openshift_clusters
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

Creates, updates, deletes, gets or lists a <code>open_shift_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>open_shift_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.openshift_clusters.open_shift_clusters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_open_shift_clusters', value: 'view', },
        { label: 'open_shift_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiserver_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="console_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="ingress_profiles" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="master_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_principal_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="worker_profiles" /> | `text` | field from the `properties` object |
| <CopyableCode code="worker_profiles_status" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | OpenShiftClusterProperties represents an OpenShift cluster's properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | The operation returns properties of a OpenShift cluster. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The operation returns properties of each OpenShift cluster. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The operation returns properties of each OpenShift cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | The operation returns properties of a OpenShift cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | The operation returns nothing. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | The operation returns properties of a OpenShift cluster. |

## `SELECT` examples

The operation returns properties of each OpenShift cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_open_shift_clusters', value: 'view', },
        { label: 'open_shift_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
apiserver_profile,
cluster_profile,
console_profile,
ingress_profiles,
location,
master_profile,
network_profile,
provisioning_state,
resourceGroupName,
resourceName,
service_principal_profile,
subscriptionId,
system_data,
tags,
worker_profiles,
worker_profiles_status
FROM azure_isv.openshift_clusters.vw_open_shift_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
systemData,
tags
FROM azure_isv.openshift_clusters.open_shift_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>open_shift_clusters</code> resource.

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
INSERT INTO azure_isv.openshift_clusters.open_shift_clusters (
resourceGroupName,
resourceName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
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
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: clusterProfile
          value:
            - name: pullSecret
              value: string
            - name: domain
              value: string
            - name: version
              value: string
            - name: resourceGroupId
              value: string
            - name: fipsValidatedModules
              value: []
        - name: consoleProfile
          value:
            - name: url
              value: string
        - name: servicePrincipalProfile
          value:
            - name: clientId
              value: string
            - name: clientSecret
              value: string
        - name: networkProfile
          value:
            - name: podCidr
              value: string
            - name: serviceCidr
              value: string
            - name: outboundType
              value: []
            - name: loadBalancerProfile
              value:
                - name: managedOutboundIps
                  value:
                    - name: count
                      value: integer
                - name: effectiveOutboundIps
                  value:
                    - - name: id
                        value: string
            - name: preconfiguredNSG
              value: []
        - name: masterProfile
          value:
            - name: vmSize
              value: []
            - name: subnetId
              value: string
            - name: encryptionAtHost
              value: []
            - name: diskEncryptionSetId
              value: string
        - name: workerProfiles
          value:
            - - name: name
                value: string
              - name: diskSizeGB
                value: integer
              - name: subnetId
                value: string
              - name: count
                value: integer
              - name: diskEncryptionSetId
                value: string
        - name: workerProfilesStatus
          value:
            - - name: name
                value: string
              - name: diskSizeGB
                value: integer
              - name: subnetId
                value: string
              - name: count
                value: integer
              - name: diskEncryptionSetId
                value: string
        - name: apiserverProfile
          value:
            - name: visibility
              value: []
            - name: url
              value: string
            - name: ip
              value: string
        - name: ingressProfiles
          value:
            - - name: name
                value: string
              - name: ip
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

Updates a <code>open_shift_clusters</code> resource.

```sql
/*+ update */
UPDATE azure_isv.openshift_clusters.open_shift_clusters
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>open_shift_clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.openshift_clusters.open_shift_clusters
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
