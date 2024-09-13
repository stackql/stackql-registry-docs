---
title: models_version
hide_title: false
hide_table_of_contents: false
keywords:
  - models_version
  - aiplatform
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

Creates, updates, deletes or gets an <code>models_version</code> resource or lists <code>models_version</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>models_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.models_version" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete_version" /> | `DELETE` | <CopyableCode code="locationsId, modelsId, projectsId" /> | Deletes a Model version. Model version can only be deleted if there are no DeployedModels created from it. Deleting the only version in the Model is not allowed. Use DeleteModel for deleting the Model instead. |

## `DELETE` example

Deletes the specified models_version resource.

```sql
DELETE FROM google.aiplatform.models_version
WHERE locationsId = '{{ locationsId }}'
AND modelsId = '{{ modelsId }}'
AND projectsId = '{{ projectsId }}';
```
