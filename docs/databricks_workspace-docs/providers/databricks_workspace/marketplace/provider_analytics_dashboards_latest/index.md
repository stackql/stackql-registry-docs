---
title: provider_analytics_dashboards_latest
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - provider_analytics_dashboards_latest
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

Operations on a <code>provider_analytics_dashboards_latest</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_analytics_dashboards_latest</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.provider_analytics_dashboards_latest" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="version" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getlatestversion" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Get latest version of provider analytics dashboard. |

## `SELECT` examples

```sql
SELECT
version
FROM databricks_workspace.marketplace.provider_analytics_dashboards_latest
WHERE deployment_name = '{{ deployment_name }}';
```
