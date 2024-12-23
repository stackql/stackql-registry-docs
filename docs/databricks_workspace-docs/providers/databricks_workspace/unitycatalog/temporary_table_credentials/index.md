---
title: temporary_table_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - temporary_table_credentials
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

Operations on a <code>temporary_table_credentials</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>temporary_table_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.temporary_table_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="aws_temp_credentials" /> | `object` |
| <CopyableCode code="azure_user_delegation_sas" /> | `object` |
| <CopyableCode code="expiration_time" /> | `integer` |
| <CopyableCode code="gcp_oauth_token" /> | `object` |
| <CopyableCode code="r2_temp_credentials" /> | `object` |
| <CopyableCode code="url" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="generatetemporarytablecredentials" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Get a short-lived credential for directly accessing the table data on cloud storage. The metastore must have external_access_enabled flag set to true (default false). The caller must have EXTERNAL_USE_SCHEMA privilege on the parent schema and this privilege can only be granted by catalog owners. |

## `SELECT` examples

```sql
SELECT
aws_temp_credentials,
azure_user_delegation_sas,
expiration_time,
gcp_oauth_token,
r2_temp_credentials,
url
FROM databricks_workspace.unitycatalog.temporary_table_credentials
WHERE deployment_name = '{{ deployment_name }}';
```
