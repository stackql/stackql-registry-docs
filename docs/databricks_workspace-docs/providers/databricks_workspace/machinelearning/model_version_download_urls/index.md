---
title: model_version_download_urls
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - model_version_download_urls
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

Operations on a <code>model_version_download_urls</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_version_download_urls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_version_download_urls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="artifact_uri" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getmodelversiondownloaduri" /> | `SELECT` | <CopyableCode code="name, version, deployment_name" /> | Gets a URI to download the model version. |

## `SELECT` examples

```sql
SELECT
artifact_uri
FROM databricks_workspace.machinelearning.model_version_download_urls
WHERE name = '{{ name }}' AND
version = '{{ version }}' AND
deployment_name = '{{ deployment_name }}';
```
