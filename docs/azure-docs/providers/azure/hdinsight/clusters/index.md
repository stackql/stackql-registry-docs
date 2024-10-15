---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - hdinsight
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.clusters" /></td></tr>
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
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_definition" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_hdp_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute_isolation_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectivity_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_encryption_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_in_transit_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The ETag for the resource |
| <CopyableCode code="excluded_services_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the cluster. |
| <CopyableCode code="kafka_rest_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="min_supported_tls_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="quota_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="tier" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | The availability zones. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The ETag for the resource |
| <CopyableCode code="identity" /> | `object` | Identity for the cluster. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of cluster. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="zones" /> | `array` | The availability zones. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets the specified cluster. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the HDInsight clusters under the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the HDInsight clusters in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Creates a new HDInsight cluster with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Deletes the specified HDInsight cluster. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Patch HDInsight cluster with the specified parameters. |
| <CopyableCode code="execute_script_actions" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__persistOnSuccess" /> | Executes script actions on the specified HDInsight cluster. |
| <CopyableCode code="resize" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, roleName, subscriptionId" /> | Resizes the specified HDInsight cluster to the specified size. |
| <CopyableCode code="rotate_disk_encryption_key" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Rotate disk encryption key of the specified HDInsight cluster. |

## `SELECT` examples

Lists all the HDInsight clusters under the subscription.

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
clusterName,
cluster_definition,
cluster_hdp_version,
cluster_id,
cluster_state,
cluster_version,
compute_isolation_properties,
compute_profile,
connectivity_endpoints,
created_date,
disk_encryption_properties,
encryption_in_transit_properties,
errors,
etag,
excluded_services_config,
identity,
kafka_rest_properties,
location,
min_supported_tls_version,
network_properties,
os_type,
private_endpoint_connections,
private_link_configurations,
provisioning_state,
quota_info,
resourceGroupName,
security_profile,
storage_profile,
subscriptionId,
system_data,
tags,
tier,
zones
FROM azure.hdinsight.vw_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
identity,
location,
properties,
systemData,
tags,
zones
FROM azure.hdinsight.clusters
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
INSERT INTO azure.hdinsight.clusters (
clusterName,
resourceGroupName,
subscriptionId,
location,
tags,
zones,
properties,
identity
)
SELECT 
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ zones }}',
'{{ properties }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: zones
      value:
        - string
    - name: properties
      value:
        - name: clusterVersion
          value: string
        - name: osType
          value: string
        - name: tier
          value: string
        - name: clusterDefinition
          value:
            - name: blueprint
              value: string
            - name: kind
              value: string
            - name: componentVersion
              value: object
            - name: configurations
              value: object
        - name: kafkaRestProperties
          value:
            - name: clientGroupInfo
              value:
                - name: groupName
                  value: string
                - name: groupId
                  value: string
            - name: configurationOverride
              value: object
        - name: securityProfile
          value:
            - name: directoryType
              value: string
            - name: domain
              value: string
            - name: organizationalUnitDN
              value: string
            - name: ldapsUrls
              value:
                - string
            - name: domainUsername
              value: string
            - name: domainUserPassword
              value: string
            - name: clusterUsersGroupDNs
              value:
                - string
            - name: aaddsResourceId
              value: string
            - name: msiResourceId
              value: string
        - name: computeProfile
          value:
            - name: roles
              value:
                - - name: name
                    value: string
                  - name: minInstanceCount
                    value: integer
                  - name: targetInstanceCount
                    value: integer
                  - name: VMGroupName
                    value: string
                  - name: autoscale
                    value:
                      - name: capacity
                        value:
                          - name: minInstanceCount
                            value: integer
                          - name: maxInstanceCount
                            value: integer
                      - name: recurrence
                        value:
                          - name: timeZone
                            value: string
                          - name: schedule
                            value:
                              - - name: days
                                  value:
                                    - string
                                - name: timeAndCapacity
                                  value:
                                    - name: time
                                      value: string
                                    - name: minInstanceCount
                                      value: integer
                                    - name: maxInstanceCount
                                      value: integer
                  - name: hardwareProfile
                    value:
                      - name: vmSize
                        value: string
                  - name: osProfile
                    value:
                      - name: linuxOperatingSystemProfile
                        value:
                          - name: username
                            value: string
                          - name: password
                            value: string
                          - name: sshProfile
                            value:
                              - name: publicKeys
                                value:
                                  - - name: certificateData
                                      value: string
                  - name: virtualNetworkProfile
                    value:
                      - name: id
                        value: string
                      - name: subnet
                        value: string
                  - name: dataDisksGroups
                    value:
                      - - name: disksPerNode
                          value: integer
                        - name: storageAccountType
                          value: string
                        - name: diskSizeGB
                          value: integer
                  - name: scriptActions
                    value:
                      - - name: name
                          value: string
                        - name: uri
                          value: string
                        - name: parameters
                          value: string
                  - name: encryptDataDisks
                    value: boolean
        - name: storageProfile
          value:
            - name: storageaccounts
              value:
                - - name: name
                    value: string
                  - name: isDefault
                    value: boolean
                  - name: container
                    value: string
                  - name: fileSystem
                    value: string
                  - name: key
                    value: string
                  - name: resourceId
                    value: string
                  - name: msiResourceId
                    value: string
                  - name: saskey
                    value: string
                  - name: fileshare
                    value: string
                  - name: enableSecureChannel
                    value: boolean
        - name: diskEncryptionProperties
          value:
            - name: vaultUri
              value: string
            - name: keyName
              value: string
            - name: keyVersion
              value: string
            - name: encryptionAlgorithm
              value: string
            - name: msiResourceId
              value: string
            - name: encryptionAtHost
              value: boolean
        - name: encryptionInTransitProperties
          value:
            - name: isEncryptionInTransitEnabled
              value: boolean
        - name: minSupportedTlsVersion
          value: string
        - name: networkProperties
          value:
            - name: outboundDependenciesManagedType
              value: string
            - name: resourceProviderConnection
              value: string
            - name: privateLink
              value: string
            - name: publicIpTag
              value:
                - name: ipTagType
                  value: string
                - name: tag
                  value: string
        - name: computeIsolationProperties
          value:
            - name: enableComputeIsolation
              value: boolean
            - name: hostSku
              value: string
        - name: privateLinkConfigurations
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: properties
                value:
                  - name: groupId
                    value: string
                  - name: provisioningState
                    value: string
                  - name: ipConfigurations
                    value:
                      - - name: id
                          value: string
                        - name: name
                          value: string
                        - name: type
                          value: string
                        - name: properties
                          value:
                            - name: provisioningState
                              value: string
                            - name: primary
                              value: boolean
                            - name: privateIPAddress
                              value: string
                            - name: privateIPAllocationMethod
                              value: string
                            - name: subnet
                              value:
                                - name: id
                                  value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>clusters</code> resource.

```sql
/*+ update */
UPDATE azure.hdinsight.clusters
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hdinsight.clusters
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
