---
title: experiment_artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - experiment_artifacts
  - machinelearning
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

Operations on a <code>experiment_artifacts</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiment_artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.experiment_artifacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="files" /> | `array` |
| <CopyableCode code="next_page_token" /> | `string` |
| <CopyableCode code="root_uri" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listartifacts" /> | `SELECT` | <CopyableCode code="deployment_name" /> | List artifacts for a run. Takes an optional |

## `SELECT` examples

```sql
SELECT
files,
next_page_token,
root_uri
FROM databricks_workspace.machinelearning.experiment_artifacts
WHERE deployment_name = '{{ deployment_name }}';
```
