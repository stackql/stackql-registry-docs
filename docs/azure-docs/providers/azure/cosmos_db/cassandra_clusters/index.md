---
title: cassandra_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_clusters
  - cosmos_db
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

Creates, updates, deletes, gets or lists a <code>cassandra_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cassandra_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.cassandra_clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the ARM resource. |
| <CopyableCode code="name" /> | `string` | The name of the ARM resource. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource group to which the resource belongs. |
| <CopyableCode code="properties" /> | `object` | Properties of a managed Cassandra cluster. |
| <CopyableCode code="tags" /> | `object` | Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB". |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get the properties of a managed Cassandra cluster. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all managed Cassandra clusters in this resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all managed Cassandra clusters in this subscription. |
| <CopyableCode code="create_update" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Create or update a managed Cassandra cluster. When updating, you must specify all writable properties. To update only some properties, use PATCH. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Deletes a managed Cassandra cluster. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Updates some of the properties of a managed Cassandra cluster. |
| <CopyableCode code="deallocate" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Deallocate the Managed Cassandra Cluster and Associated Data Centers. Deallocation will deallocate the host virtual machine of this cluster, and reserved the data disk. This won't do anything on an already deallocated cluster. Use Start to restart the cluster. |
| <CopyableCode code="invoke_command" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__command, data__host" /> | Invoke a command like nodetool for cassandra maintenance |
| <CopyableCode code="invoke_command_async" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__command, data__host" /> | Invoke a command like nodetool for cassandra maintenance asynchronously |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Start the Managed Cassandra Cluster and Associated Data Centers. Start will start the host virtual machine of this cluster with reserved data disk. This won't do anything on an already running cluster. Use Deallocate to deallocate the cluster. |
| <CopyableCode code="status" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets the CPU, memory, and disk usage statistics for each Cassandra node in a cluster. |

## `SELECT` examples

List all managed Cassandra clusters in this subscription.


```sql
SELECT
id,
name,
identity,
location,
properties,
tags,
type
FROM azure.cosmos_db.cassandra_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cassandra_clusters</code> resource.

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
INSERT INTO azure.cosmos_db.cassandra_clusters (
clusterName,
resourceGroupName,
subscriptionId,
location,
tags,
identity,
properties
)
SELECT 
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ identity }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: []
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: restoreFromBackupId
          value: string
        - name: delegatedManagementSubnetId
          value: string
        - name: cassandraVersion
          value: string
        - name: clusterNameOverride
          value: string
        - name: authenticationMethod
          value: string
        - name: initialCassandraAdminPassword
          value: string
        - name: prometheusEndpoint
          value:
            - name: ipAddress
              value: string
        - name: repairEnabled
          value: boolean
        - name: autoReplicate
          value: string
        - name: clientCertificates
          value:
            - - name: pem
                value: string
        - name: externalGossipCertificates
          value:
            - - name: pem
                value: string
        - name: gossipCertificates
          value:
            - - name: pem
                value: string
        - name: externalSeedNodes
          value:
            - - name: ipAddress
                value: string
        - name: seedNodes
          value:
            - - name: ipAddress
                value: string
        - name: externalDataCenters
          value:
            - string
        - name: hoursBetweenBackups
          value: integer
        - name: deallocated
          value: boolean
        - name: cassandraAuditLoggingEnabled
          value: boolean
        - name: clusterType
          value: string
        - name: provisionError
          value:
            - name: code
              value: string
            - name: message
              value: string
            - name: target
              value: string
            - name: additionalErrorInfo
              value: string
        - name: extensions
          value:
            - string
        - name: backupSchedules
          value:
            - - name: scheduleName
                value: string
              - name: cronExpression
                value: string
              - name: retentionInHours
                value: integer
        - name: scheduledEventStrategy
          value: string
        - name: azureConnectionMethod
          value: string
        - name: privateLinkResourceId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>cassandra_clusters</code> resource.

```sql
/*+ update */
UPDATE azure.cosmos_db.cassandra_clusters
SET 
location = '{{ location }}',
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>cassandra_clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cosmos_db.cassandra_clusters
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
