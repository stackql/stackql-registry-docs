---
title: source_control_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - source_control_configurations
  - kubernetes_configuration
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

Creates, updates, deletes, gets or lists a <code>source_control_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_control_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetes_configuration.source_control_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties to create a Source Control Configuration resource |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, resourceGroupName, sourceControlConfigurationName, subscriptionId" /> | Gets details of the Source Control Configuration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, resourceGroupName, subscriptionId" /> | List all Source Control Configurations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, resourceGroupName, sourceControlConfigurationName, subscriptionId" /> | Create a new Kubernetes Source Control Configuration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, resourceGroupName, sourceControlConfigurationName, subscriptionId" /> | This will delete the YAML file used to set up the Source control configuration, thus stopping future sync from the source repo. |

## `SELECT` examples

List all Source Control Configurations.


```sql
SELECT
properties,
systemData
FROM azure.kubernetes_configuration.source_control_configurations
WHERE clusterName = '{{ clusterName }}'
AND clusterResourceName = '{{ clusterResourceName }}'
AND clusterRp = '{{ clusterRp }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>source_control_configurations</code> resource.

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
INSERT INTO azure.kubernetes_configuration.source_control_configurations (
clusterName,
clusterResourceName,
clusterRp,
resourceGroupName,
sourceControlConfigurationName,
subscriptionId,
properties,
systemData
)
SELECT 
'{{ clusterName }}',
'{{ clusterResourceName }}',
'{{ clusterRp }}',
'{{ resourceGroupName }}',
'{{ sourceControlConfigurationName }}',
'{{ subscriptionId }}',
'{{ properties }}',
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
        - name: repositoryUrl
          value: string
        - name: operatorNamespace
          value: string
        - name: operatorInstanceName
          value: string
        - name: operatorType
          value: []
        - name: operatorParams
          value: string
        - name: configurationProtectedSettings
          value: []
        - name: operatorScope
          value: []
        - name: repositoryPublicKey
          value: string
        - name: sshKnownHostsContents
          value: string
        - name: enableHelmOperator
          value: boolean
        - name: helmOperatorProperties
          value:
            - name: chartVersion
              value: []
            - name: chartValues
              value: []
        - name: provisioningState
          value: string
        - name: complianceStatus
          value:
            - name: complianceState
              value: string
            - name: lastConfigApplied
              value: string
            - name: message
              value: string
            - name: messageLevel
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

Deletes the specified <code>source_control_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.kubernetes_configuration.source_control_configurations
WHERE clusterName = '{{ clusterName }}'
AND clusterResourceName = '{{ clusterResourceName }}'
AND clusterRp = '{{ clusterRp }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sourceControlConfigurationName = '{{ sourceControlConfigurationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
