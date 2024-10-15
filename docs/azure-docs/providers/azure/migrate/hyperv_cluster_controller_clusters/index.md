---
title: hyperv_cluster_controller_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - hyperv_cluster_controller_clusters
  - migrate
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

Creates, updates, deletes, gets or lists a <code>hyperv_cluster_controller_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hyperv_cluster_controller_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.hyperv_cluster_controller_clusters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hyperv_cluster_controller_clusters', value: 'view', },
        { label: 'hyperv_cluster_controller_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="functional_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_fqdn_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_as_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_timestamp" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of Hyperv Cluster |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, siteName, subscriptionId" /> | Method to get a Hyper-V cluster. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, siteName, subscriptionId" /> | Method to create or update a Hyper-V cluster. |

## `SELECT` examples

Method to get a Hyper-V cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hyperv_cluster_controller_clusters', value: 'view', },
        { label: 'hyperv_cluster_controller_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
clusterName,
created_timestamp,
errors,
fqdn,
functional_level,
host_fqdn_list,
provisioning_state,
resourceGroupName,
run_as_account_id,
siteName,
status,
subscriptionId,
updated_timestamp
FROM azure.migrate.vw_hyperv_cluster_controller_clusters
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.hyperv_cluster_controller_clusters
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hyperv_cluster_controller_clusters</code> resource.

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
INSERT INTO azure.migrate.hyperv_cluster_controller_clusters (
clusterName,
resourceGroupName,
siteName,
subscriptionId,
properties
)
SELECT 
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ siteName }}',
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
        - name: createdTimestamp
          value: string
        - name: updatedTimestamp
          value: string
        - name: fqdn
          value: string
        - name: functionalLevel
          value: integer
        - name: status
          value: string
        - name: runAsAccountId
          value: string
        - name: hostFqdnList
          value:
            - string
        - name: errors
          value:
            - - name: message
                value: string
              - name: messageParameters
                value: object
              - name: applianceName
                value: string
              - name: id
                value: integer
              - name: code
                value: string
              - name: possibleCauses
                value: string
              - name: recommendedAction
                value: string
              - name: severity
                value: string
              - name: summaryMessage
                value: string
              - name: source
                value: []
              - name: updatedTimeStamp
                value: string
              - name: runAsAccountId
                value: string
              - name: discoveryScope
                value: []
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>
