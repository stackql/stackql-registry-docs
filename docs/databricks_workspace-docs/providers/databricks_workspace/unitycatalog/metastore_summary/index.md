---
title: metastore_summary
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - metastore_summary
  - unitycatalog
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

Operations on a <code>metastore_summary</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metastore_summary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.metastore_summary" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="cloud" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="default_data_access_config_id" /> | `string` |
| <CopyableCode code="delta_sharing_organization_name" /> | `string` |
| <CopyableCode code="delta_sharing_recipient_token_lifetime_in_seconds" /> | `integer` |
| <CopyableCode code="delta_sharing_scope" /> | `string` |
| <CopyableCode code="external_access_enabled" /> | `boolean` |
| <CopyableCode code="global_metastore_id" /> | `string` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="owner" /> | `string` |
| <CopyableCode code="privilege_model_version" /> | `string` |
| <CopyableCode code="region" /> | `string` |
| <CopyableCode code="storage_root" /> | `string` |
| <CopyableCode code="storage_root_credential_id" /> | `string` |
| <CopyableCode code="storage_root_credential_name" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="summary" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets information about a metastore. This summary includes the storage credential, the cloud vendor, the cloud region, and the global metastore ID. |

## `SELECT` examples

```sql
SELECT
name,
cloud,
created_at,
created_by,
default_data_access_config_id,
delta_sharing_organization_name,
delta_sharing_recipient_token_lifetime_in_seconds,
delta_sharing_scope,
external_access_enabled,
global_metastore_id,
metastore_id,
owner,
privilege_model_version,
region,
storage_root,
storage_root_credential_id,
storage_root_credential_name,
updated_at,
updated_by
FROM databricks_workspace.unitycatalog.metastore_summary
WHERE deployment_name = '{{ deployment_name }}';
```
