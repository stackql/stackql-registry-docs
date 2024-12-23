---
title: provider_analytics_dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - provider_analytics_dashboards
  - marketplace
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

Operations on a <code>provider_analytics_dashboards</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_analytics_dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.provider_analytics_dashboards" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="dashboard_id" /> | `string` |
| <CopyableCode code="version" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Get provider analytics dashboard. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Create provider analytics dashboard. Returns Marketplace specific |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="id, deployment_name" /> | Update provider analytics dashboard. |

## `SELECT` examples

```sql
SELECT
id,
dashboard_id,
version
FROM databricks_workspace.marketplace.provider_analytics_dashboards
WHERE deployment_name = '{{ deployment_name }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>provider_analytics_dashboards</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'provider_analytics_dashboards', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.marketplace.provider_analytics_dashboards (
deployment_name
)
SELECT 
'{{ deployment_name }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []  # No request body parameters required
```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>provider_analytics_dashboards</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.marketplace.provider_analytics_dashboards
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
