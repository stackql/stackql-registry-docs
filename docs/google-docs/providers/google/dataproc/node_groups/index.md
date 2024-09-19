---
title: node_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - node_groups
  - dataproc
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

Creates, updates, deletes, gets or lists a <code>node_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataproc.node_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The Node group resource name (https://aip.dev/122). |
| <CopyableCode code="labels" /> | `object` | Optional. Node group labels. Label keys must consist of from 1 to 63 characters and conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values can be empty. If specified, they must consist of from 1 to 63 characters and conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). The node group must have no more than 32 labelsn. |
| <CopyableCode code="nodeGroupConfig" /> | `object` | The config settings for Compute Engine resources in an instance group, such as a master or worker group. |
| <CopyableCode code="roles" /> | `array` | Required. Node group roles. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_regions_clusters_node_groups_get" /> | `SELECT` | <CopyableCode code="clustersId, nodeGroupsId, projectsId, regionsId" /> | Gets the resource representation for a node group in a cluster. |
| <CopyableCode code="projects_regions_clusters_node_groups_create" /> | `INSERT` | <CopyableCode code="clustersId, projectsId, regionsId" /> | Creates a node group in a cluster. The returned Operation.metadata is NodeGroupOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#nodegroupoperationmetadata). |
| <CopyableCode code="projects_regions_clusters_node_groups_repair" /> | `EXEC` | <CopyableCode code="clustersId, nodeGroupsId, projectsId, regionsId" /> | Repair nodes in a node group. |
| <CopyableCode code="projects_regions_clusters_node_groups_resize" /> | `EXEC` | <CopyableCode code="clustersId, nodeGroupsId, projectsId, regionsId" /> | Resizes a node group in a cluster. The returned Operation.metadata is NodeGroupOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#nodegroupoperationmetadata). |

## `SELECT` examples

Gets the resource representation for a node group in a cluster.

```sql
SELECT
name,
labels,
nodeGroupConfig,
roles
FROM google.dataproc.node_groups
WHERE clustersId = '{{ clustersId }}'
AND nodeGroupsId = '{{ nodeGroupsId }}'
AND projectsId = '{{ projectsId }}'
AND regionsId = '{{ regionsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>node_groups</code> resource.

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
INSERT INTO google.dataproc.node_groups (
clustersId,
projectsId,
regionsId,
name,
roles,
nodeGroupConfig,
labels
)
SELECT 
'{{ clustersId }}',
'{{ projectsId }}',
'{{ regionsId }}',
'{{ name }}',
'{{ roles }}',
'{{ nodeGroupConfig }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: roles
      value:
        - string
    - name: nodeGroupConfig
      value:
        - name: numInstances
          value: integer
        - name: instanceNames
          value:
            - string
        - name: instanceReferences
          value:
            - - name: instanceName
                value: string
              - name: instanceId
                value: string
              - name: publicKey
                value: string
              - name: publicEciesKey
                value: string
        - name: imageUri
          value: string
        - name: machineTypeUri
          value: string
        - name: diskConfig
          value:
            - name: bootDiskType
              value: string
            - name: bootDiskSizeGb
              value: integer
            - name: numLocalSsds
              value: integer
            - name: localSsdInterface
              value: string
            - name: bootDiskProvisionedIops
              value: string
            - name: bootDiskProvisionedThroughput
              value: string
        - name: isPreemptible
          value: boolean
        - name: preemptibility
          value: string
        - name: managedGroupConfig
          value:
            - name: instanceTemplateName
              value: string
            - name: instanceGroupManagerName
              value: string
            - name: instanceGroupManagerUri
              value: string
        - name: accelerators
          value:
            - - name: acceleratorTypeUri
                value: string
              - name: acceleratorCount
                value: integer
        - name: minCpuPlatform
          value: string
        - name: minNumInstances
          value: integer
        - name: instanceFlexibilityPolicy
          value:
            - name: instanceSelectionList
              value:
                - - name: machineTypes
                    value:
                      - string
                  - name: rank
                    value: integer
            - name: instanceSelectionResults
              value:
                - - name: machineType
                    value: string
                  - name: vmCount
                    value: integer
        - name: startupConfig
          value:
            - name: requiredRegistrationFraction
              value: number
    - name: labels
      value: object

```
</TabItem>
</Tabs>
