---
title: monitoring_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - monitoring_configs
  - data_box_edge
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

Creates, updates, deletes, gets or lists a <code>monitoring_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitoring_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.monitoring_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The object name. |
| <CopyableCode code="properties" /> | `object` | Metrics properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, roleName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, roleName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, resourceGroupName, roleName, subscriptionId, data__properties" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, resourceGroupName, roleName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_box_edge.monitoring_configs
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND roleName = '{{ roleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>monitoring_configs</code> resource.

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
INSERT INTO azure.data_box_edge.monitoring_configs (
deviceName,
resourceGroupName,
roleName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ deviceName }}',
'{{ resourceGroupName }}',
'{{ roleName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
    - name: properties
      value:
        - name: metricConfigurations
          value:
            - - name: resourceId
                value: string
              - name: mdmAccount
                value: string
              - name: metricNameSpace
                value: string
              - name: counterSets
                value:
                  - - name: counters
                      value:
                        - - name: name
                            value: string
                          - name: instance
                            value: string
                          - name: dimensionFilter
                            value:
                              - - name: sourceType
                                  value: string
                                - name: sourceName
                                  value: string
                          - name: additionalDimensions
                            value:
                              - - name: sourceType
                                  value: string
                                - name: sourceName
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

Deletes the specified <code>monitoring_configs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_box_edge.monitoring_configs
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND roleName = '{{ roleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
