---
title: libraries
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - libraries
  - compute
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>libraries</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>libraries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.libraries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="cluster_id" /> | `string` |
| <CopyableCode code="library_statuses" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="allclusterlibrarystatuses" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Get the status of all libraries on all clusters. A status is returned for all libraries installed on this cluster via the API or the libraries UI. |
| <CopyableCode code="clusterstatus" /> | `SELECT` | <CopyableCode code="cluster_id, deployment_name" /> | Get the status of libraries on a cluster. A status is returned for all libraries installed on this cluster via the API or the libraries UI. The order of returned libraries is as follows: |
| <CopyableCode code="install" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Add libraries to install on a cluster. The installation is asynchronous; it happens in the background after the completion of this request. |
| <CopyableCode code="uninstall" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Set libraries to uninstall from a cluster. The libraries won't be uninstalled until the cluster is restarted. A request to uninstall a library that is not currently installed is ignored. |

## `SELECT` examples

<Tabs
    defaultValue="allclusterlibrarystatuses"
    values={[
        { label: 'libraries (allclusterlibrarystatuses)', value: 'allclusterlibrarystatuses' },
        { label: 'libraries (clusterstatus)', value: 'clusterstatus' }
    ]
}>
<TabItem value="allclusterlibrarystatuses">

```sql
SELECT
cluster_id,
library_statuses
FROM databricks_workspace.compute.libraries
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="clusterstatus">

```sql
SELECT
cluster_id,
library_statuses
FROM databricks_workspace.compute.libraries
WHERE cluster_id = '{{ cluster_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>libraries</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'libraries', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.compute.libraries (
deployment_name,
data__cluster_id,
data__libraries
)
SELECT 
'{{ deployment_name }}',
'{{ cluster_id }}',
'{{ libraries }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: cluster_id
    value: 1234-56789-abcde
  - name: libraries
    value:
    - pypi:
        package: numpy
        repo: http://my-pypi-repo.com
    - jar: /Workspace/path/to/library.jar
    - whl: /Workspace/path/to/library.whl
    - maven:
        coordinates: com.databricks:spark-csv_2.11:1.5.0
        exclusions:
        - org.slf4j:slf4j-log4j12
        repo: http://my-maven-repo.com
    - cran:
        package: ggplot2
        repo: http://cran.us.r-project.org
    - requirements: /Workspace/path/to/requirements.txt

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>libraries</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.compute.libraries
WHERE deployment_name = '{{ deployment_name }}';
```
