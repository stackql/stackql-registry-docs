---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
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

Creates, updates, deletes, gets or lists a <code>applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.applications" /></td></tr>
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
| <CopyableCode code="applicationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The ETag for the application |
| <CopyableCode code="https_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="install_script_actions" /> | `text` | field from the `properties` object |
| <CopyableCode code="marketplace_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ssh_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags for the application. |
| <CopyableCode code="uninstall_script_actions" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The ETag for the application |
| <CopyableCode code="properties" /> | `object` | The HDInsight cluster application GET response. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | The tags for the application. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Gets properties of the specified application. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Lists all of the applications for the HDInsight cluster. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Creates applications for the HDInsight cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Deletes the specified application on the HDInsight cluster. |

## `SELECT` examples

Lists all of the applications for the HDInsight cluster.

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
applicationName,
application_state,
application_type,
clusterName,
compute_profile,
created_date,
errors,
etag,
https_endpoints,
install_script_actions,
marketplace_identifier,
private_link_configurations,
provisioning_state,
resourceGroupName,
ssh_endpoints,
subscriptionId,
system_data,
tags,
uninstall_script_actions
FROM azure.hdinsight.vw_applications
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties,
systemData,
tags
FROM azure.hdinsight.applications
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
INSERT INTO azure.hdinsight.applications (
applicationName,
clusterName,
resourceGroupName,
subscriptionId,
etag,
tags,
properties
)
SELECT 
'{{ applicationName }}',
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ etag }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: tags
      value: object
    - name: properties
      value:
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
        - name: installScriptActions
          value:
            - - name: name
                value: string
              - name: uri
                value: string
              - name: parameters
                value: string
              - name: roles
                value:
                  - string
              - name: applicationName
                value: string
        - name: uninstallScriptActions
          value:
            - - name: name
                value: string
              - name: uri
                value: string
              - name: parameters
                value: string
              - name: roles
                value:
                  - string
              - name: applicationName
                value: string
        - name: httpsEndpoints
          value:
            - - name: accessModes
                value:
                  - string
              - name: location
                value: string
              - name: destinationPort
                value: integer
              - name: publicPort
                value: integer
              - name: privateIPAddress
                value: string
              - name: subDomainSuffix
                value: string
              - name: disableGatewayAuth
                value: boolean
        - name: sshEndpoints
          value:
            - - name: location
                value: string
              - name: destinationPort
                value: integer
              - name: publicPort
                value: integer
              - name: privateIPAddress
                value: string
        - name: provisioningState
          value: string
        - name: applicationType
          value: string
        - name: applicationState
          value: string
        - name: errors
          value:
            - - name: code
                value: string
              - name: message
                value: string
        - name: createdDate
          value: string
        - name: marketplaceIdentifier
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

## `DELETE` example

Deletes the specified <code>applications</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hdinsight.applications
WHERE applicationName = '{{ applicationName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
