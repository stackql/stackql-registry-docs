---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - deployments
  - apps
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

Operations on a <code>deployments</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.apps.deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="create_time" /> | `string` |
| <CopyableCode code="creator" /> | `string` |
| <CopyableCode code="deployment_artifacts" /> | `object` |
| <CopyableCode code="deployment_id" /> | `string` |
| <CopyableCode code="mode" /> | `string` |
| <CopyableCode code="source_code_path" /> | `string` |
| <CopyableCode code="status" /> | `object` |
| <CopyableCode code="update_time" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getdeployment" /> | `SELECT` | <CopyableCode code="app_name, deployment_id, deployment_name" /> | Retrieves information for the app deployment with the supplied name and deployment id. |
| <CopyableCode code="listdeployments" /> | `SELECT` | <CopyableCode code="app_name, deployment_name" /> | Lists all app deployments for the app with the supplied name. |

## `SELECT` examples

<Tabs
    defaultValue="listdeployments"
    values={[
        { label: 'deployments (listdeployments)', value: 'listdeployments' },
        { label: 'deployments (getdeployment)', value: 'getdeployment' }
    ]
}>
<TabItem value="listdeployments">

```sql
SELECT
create_time,
creator,
deployment_artifacts,
deployment_id,
mode,
source_code_path,
status,
update_time
FROM databricks_workspace.apps.deployments
WHERE app_name = '{{ app_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getdeployment">

```sql
SELECT
create_time,
creator,
deployment_artifacts,
deployment_id,
mode,
source_code_path,
status,
update_time
FROM databricks_workspace.apps.deployments
WHERE app_name = '{{ app_name }}' AND
deployment_id = '{{ deployment_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>
