
---
title: user_workloads_config_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - user_workloads_config_maps
  - composer
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

Creates, updates, deletes or gets an <code>user_workloads_config_map</code> resource or lists <code>user_workloads_config_maps</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_workloads_config_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.composer.user_workloads_config_maps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the ConfigMap, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}" |
| <CopyableCode code="data" /> | `object` | Optional. The "data" field of Kubernetes ConfigMap, organized in key-value pairs. For details see: https://kubernetes.io/docs/concepts/configuration/configmap/ |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentsId, locationsId, projectsId, userWorkloadsConfigMapsId" /> | Gets an existing user workloads ConfigMap. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Lists user workloads ConfigMaps. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Creates a user workloads ConfigMap. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentsId, locationsId, projectsId, userWorkloadsConfigMapsId" /> | Deletes a user workloads ConfigMap. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId, userWorkloadsConfigMapsId" /> | Updates a user workloads ConfigMap. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. |

## `SELECT` examples

Lists user workloads ConfigMaps. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

```sql
SELECT
name,
data
FROM google.composer.user_workloads_config_maps
WHERE environmentsId = '{{ environmentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_workloads_config_maps</code> resource.

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
INSERT INTO google.composer.user_workloads_config_maps (
environmentsId,
locationsId,
projectsId,
name,
data
)
SELECT 
'{{ environmentsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ data }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: data
        value: '{{ data }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified user_workloads_config_map resource.

```sql
DELETE FROM google.composer.user_workloads_config_maps
WHERE environmentsId = '{{ environmentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND userWorkloadsConfigMapsId = '{{ userWorkloadsConfigMapsId }}';
```
