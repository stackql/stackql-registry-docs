---
title: features
hide_title: false
hide_table_of_contents: false
keywords:
  - features
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.features" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the feature. |
| <CopyableCode code="etags" /> | `string` | ETag of the resource. |
| <CopyableCode code="kind" /> | `string` | Kind of resource this is. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customer, featureKey" /> | Retrieves a feature. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customer" /> | Retrieves a list of features for an account. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="customer" /> | Inserts a feature. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customer, featureKey" /> | Deletes a feature. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="customer" /> | Retrieves a list of features for an account. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="customer, featureKey" /> | Patches a feature. |
| <CopyableCode code="rename" /> | `EXEC` | <CopyableCode code="customer, oldName" /> | Renames a feature. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="customer, featureKey" /> | Updates a feature. |
