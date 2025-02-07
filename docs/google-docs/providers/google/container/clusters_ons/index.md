---
title: clusters_ons
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_ons
  - container
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

Creates, updates, deletes, gets or lists a <code>clusters_ons</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_ons</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.container.clusters_ons" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_zones_clusters_addons" /> | `INSERT` | <CopyableCode code="clusterId, projectId, zone" /> | Sets the addons for a specific cluster. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clusters_ons</code> resource.

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
INSERT INTO google.container.clusters_ons (
clusterId,
projectId,
zone,
projectId,
zone,
clusterId,
addonsConfig,
name
)
SELECT 
'{{ clusterId }}',
'{{ projectId }}',
'{{ zone }}',
'{{ projectId }}',
'{{ zone }}',
'{{ clusterId }}',
'{{ addonsConfig }}',
'{{ name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: projectId
      value: string
    - name: zone
      value: string
    - name: clusterId
      value: string
    - name: addonsConfig
      value:
        - name: httpLoadBalancing
          value:
            - name: disabled
              value: boolean
        - name: horizontalPodAutoscaling
          value:
            - name: disabled
              value: boolean
        - name: kubernetesDashboard
          value:
            - name: disabled
              value: boolean
        - name: networkPolicyConfig
          value:
            - name: disabled
              value: boolean
        - name: cloudRunConfig
          value:
            - name: disabled
              value: boolean
            - name: loadBalancerType
              value: string
        - name: dnsCacheConfig
          value:
            - name: enabled
              value: boolean
        - name: configConnectorConfig
          value:
            - name: enabled
              value: boolean
        - name: gcePersistentDiskCsiDriverConfig
          value:
            - name: enabled
              value: boolean
        - name: gcpFilestoreCsiDriverConfig
          value:
            - name: enabled
              value: boolean
        - name: gkeBackupAgentConfig
          value:
            - name: enabled
              value: boolean
        - name: gcsFuseCsiDriverConfig
          value:
            - name: enabled
              value: boolean
        - name: statefulHaConfig
          value:
            - name: enabled
              value: boolean
        - name: rayOperatorConfig
          value:
            - name: enabled
              value: boolean
            - name: rayClusterLoggingConfig
              value:
                - name: enabled
                  value: boolean
            - name: rayClusterMonitoringConfig
              value:
                - name: enabled
                  value: boolean
    - name: name
      value: string

```
</TabItem>
</Tabs>
